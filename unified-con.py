import numpy as np
from scipy.signal import convolve2d
from sklearn.metrics import mutual_info_score
import matplotlib.pyplot as plt

# ---------------------------
# Configuration - OBSERVER RESET FOCUS
# ---------------------------
N = 128
T = 1000
eta = 0.06  # Conservative learning rate
alpha = 0.2
a, b = -0.5, 0.2  # Gentle potential
lambda_C = 0.3  # LOWER self-coupling to prevent observer collapse
lambda_D = 0.4
lambda_E = 0.15  # Minimal controller
lambda_S = 0.2
beta_obs = 0.2  # Low observer bias
kappa = 0.3
gamma = 0.2  # Lower KL weight to reduce pressure
xi = 0.02

np.random.seed(11)

# ---------------------------
# CRITICAL FIX: Observer with Emergency Reset
# ---------------------------
class RobustObserver:
    def __init__(self):
        self.reset_count = 0
        self.last_kl = 0
        self.kl_increase_streak = 0
        
    def adaptive_kernel(self, Psi, eps=1e-6):
        gx = np.roll(Psi,-1,1) - Psi
        gy = np.roll(Psi,-1,0) - Psi
        gmag = np.sqrt(np.clip(gx*gx + gy*gy, 0, 1e6))
        w = gmag/(np.mean(gmag)+eps)
        K = np.array([[0.1,0.15,0.1],
                      [0.15,0.0,0.15],   # CENTER ZERO - critical change
                      [0.1,0.15,0.1]], dtype=float)
        K /= K.sum()
        return K
    
    def observe(self, Psi, beta=beta_obs, t=0, current_kl=0):
        """Observer with EMERGENCY RESET capability"""
        
        # CRITICAL: Detect observer collapse
        if current_kl > 20 and self.last_kl > 15:
            self.kl_increase_streak += 1
        else:
            self.kl_increase_streak = max(0, self.kl_increase_streak - 1)
            
        # EMERGENCY RESET if observer is failing
        if self.kl_increase_streak > 10 or current_kl > 25:
            print(f"   🚨 OBSERVER EMERGENCY RESET (KL: {current_kl:.1f})")
            self.reset_count += 1
            self.kl_increase_streak = 0
            # Return simple observation to force reset
            return np.tanh(Psi * 0.5 + 0.1 * np.random.randn(N, N))
        
        K = self.adaptive_kernel(Psi)
        sm = convolve2d(Psi, K, mode='same', boundary='wrap')
        
        # Very conservative observation
        observed = np.tanh(0.3 * sm + 0.1 * beta * Psi.mean())
        self.last_kl = current_kl
        
        return np.clip(observed, -1.5, 1.5)

# Initialize robust observer
observer = RobustObserver()

# ---------------------------
# Conservative Core Functions
# ---------------------------
def laplacian(Z):
    return (-4*Z + np.roll(Z,1,0) + np.roll(Z,-1,0) + 
            np.roll(Z,1,1) + np.roll(Z,-1,1))

def U_prime(x):
    x_clipped = np.clip(x, -6, 6)
    return a*x_clipped + b*np.clip(x_clipped**3, -100, 100)

def sigmoid(x):
    x = np.clip(x, -50, 50)
    return np.where(x >= 0, 1/(1+np.exp(-x)), np.exp(x)/(1+np.exp(x)))

def hist_probs(X, bins=32):
    X_clean = np.nan_to_num(X, nan=0.0, posinf=6.0, neginf=-6.0)
    X_clean = np.clip(X_clean, -4, 4)
    h, _ = np.histogram(X_clean.ravel(), bins=bins, range=(-3, 3), density=False)
    p = h.astype(float) + 1e-12
    p /= p.sum()
    return p

def kl(p, q):
    p = np.clip(p, 1e-12, 1.0)
    q = np.clip(q, 1e-12, 1.0)
    return np.sum(p*(np.log(p)-np.log(q)))

def mi_estimate(X, Y, bins=32):
    X_clean = np.clip(np.nan_to_num(X), -3, 3)
    Y_clean = np.clip(np.nan_to_num(Y), -3, 3)
    x = np.digitize(X_clean.ravel(), np.linspace(-3, 3, bins+1)) - 1
    y = np.digitize(Y_clean.ravel(), np.linspace(-3, 3, bins+1)) - 1
    return mutual_info_score(x, y)

def field_energy(Psi):
    Psi_clipped = np.clip(Psi, -3, 3)
    gx = np.roll(Psi_clipped,-1,1) - Psi_clipped
    gy = np.roll(Psi_clipped,-1,0) - Psi_clipped
    grad = np.clip(gx*gx + gy*gy, 0, 20)
    U = 0.5*a*(Psi_clipped**2) + 0.25*b*np.clip(Psi_clipped**4, 0, 20)
    return (kappa*0.5*np.mean(grad) + np.mean(U))

def drive_process(t, N, strength=0.8):
    base = np.random.randn(N, N) * 0.5
    wave1 = np.sin(2*np.pi*(t/60.0)) * np.linspace(-1, 1, N)
    wave = np.tile(wave1, (N, 1))
    return strength * (0.8*base + 0.2*wave)

def global_constraints(Psi):
    Psi_clipped = np.clip(Psi, -2, 2)
    gx = np.roll(Psi_clipped, -1, 1) - Psi_clipped
    gy = np.roll(Psi_clipped, -1, 0) - Psi_clipped
    curvature = np.abs(gx) + np.abs(gy)
    boundary = np.maximum(np.abs(Psi_clipped) - 1.0, 0.0)
    curv_norm = curvature / (np.mean(curvature) + 1e-6)
    bound_norm = boundary / (np.mean(boundary) + 1e-6)
    return 0.2*curv_norm + 0.5*bound_norm

class ConservativeController:
    def __init__(self, theta=0.3):
        self.theta = theta

    def act(self, Psi, D):
        Psi_clipped = np.clip(Psi, -2, 2)
        D_clipped = np.clip(D, -1, 1)
        pred = np.tanh(Psi_clipped + 0.2*D_clipped)
        E = self.theta * (pred - Psi_clipped)
        return np.clip(E, -0.5, 0.5)

def controller_dominance_index(Psi, E):
    Psi_clean = np.nan_to_num(Psi, nan=0.0)
    E_clean = np.nan_to_num(E, nan=0.0)
    num = np.mean(E_clean**2)
    den = np.mean(Psi_clean**2) + 1e-6
    return np.clip(num/(den + 1e-6), 0, 10)

def free_energy(Psi, O, E, gamma=gamma, xi=xi):
    try:
        pPsi = hist_probs(Psi)
        pO = hist_probs(O)
        F_field = field_energy(Psi)
        mismatch = kl(pPsi, pO)
        ctrl_dom = controller_dominance_index(Psi, E)
        
        # GENTLE rewards only
        novelty_bonus = -0.1 * np.mean(np.abs(Psi - O))
        
        total_F = F_field + gamma*mismatch + xi*ctrl_dom + novelty_bonus
        return total_F, mismatch, ctrl_dom
    except:
        return 5.0, 5.0, 0.5

def adapt_meta(lambda_E, lambda_S, ctrl_dom, mismatch, t, lr=0.005):
    """VERY conservative adaptation"""
    if mismatch > 15:  # If high KL, reduce everything
        dE = -0.05
        dS = -0.03
    else:
        dE = 0.02 * ctrl_dom
        dS = 0.01 * mismatch
    
    lambda_E_new = np.clip(lambda_E + lr*dE, 0.01, 0.5)
    lambda_S_new = np.clip(lambda_S + lr*dS, 0.01, 0.5)
    return lambda_E_new, lambda_S_new

def adaptive_trauma(t, Psi, base_strength=0.8):
    stability = np.std(Psi) / (np.mean(np.abs(Psi)) + 1e-6)
    strength_multiplier = 0.5 + (0.3 / (stability + 0.5))
    pattern = np.random.randn(N, N)
    trauma_pattern = base_strength * strength_multiplier * pattern
    trauma_magnitude = np.mean(np.abs(trauma_pattern))
    return trauma_pattern, trauma_magnitude

# ---------------------------
# MAIN SIMULATION - OBSERVER PROTECTION
# ---------------------------
def run_simulation_with_observer_protection():
    Psi = 0.05 * np.random.randn(N, N)  # Start smaller
    controller = ConservativeController(theta=0.3)
    
    F_list, KL_list, MI_list, CtrlDom_list = [], [], [], []
    lamE_hist, lamS_hist = [], []
    trauma_points = []
    best_F = float('inf')
    observer_resets = []
    
    lambda_E_local, lambda_S_local = lambda_E, lambda_S

    for t in range(T):
        # System integrity check
        if np.any(np.isnan(Psi)) or np.mean(np.abs(Psi)) > 5:
            print(f"🌀 FIELD RESET at step {t}")
            Psi = 0.05 * np.random.randn(N, N)
        
        # Gentle trauma tests
        if t == 300 or t == 600:
            trauma_pattern, trauma_magnitude = adaptive_trauma(t, Psi, base_strength=0.8)
            Psi += trauma_pattern
            trauma_points.append(t)
            print(f"💥 GENTLE TRAUMA at step {t} (strength: {trauma_magnitude:.1f})")
        
        # Field boundary enforcement
        Psi = np.clip(Psi, -2.5, 2.5)
        
        # Get observation FROM ROBUST OBSERVER
        O = observer.observe(Psi, beta_obs, t, KL_list[-1] if KL_list else 0)
        
        D = drive_process(t, N, strength=0.8)
        E = controller.act(Psi, D)
        S = global_constraints(Psi)

        # Conservative field update
        delta_Psi = eta * (alpha * laplacian(Psi) - U_prime(Psi) + 
                      lambda_C * (O - Psi) + lambda_D * D - 
                      lambda_E_local * E - lambda_S_local * S)
        delta_Psi = np.clip(delta_Psi, -0.3, 0.3)
        Psi = Psi + delta_Psi

        # Track observer resets
        if observer.reset_count > len(observer_resets):
            observer_resets.append(t)

        # Performance metrics
        F, mismatch, ctrl_dom = free_energy(Psi, O, E, gamma=gamma, xi=xi)
        mi = mi_estimate(Psi, O)

        F_list.append(F)
        KL_list.append(mismatch)
        MI_list.append(mi)
        CtrlDom_list.append(ctrl_dom)

        # Very slow meta-adaptation
        lambda_E_local, lambda_S_local = adapt_meta(
            lambda_E_local, lambda_S_local, ctrl_dom, mismatch, t, lr=0.005)
        lamE_hist.append(lambda_E_local)
        lamS_hist.append(lambda_S_local)
        
        # Progress monitoring
        if (t % 100 == 0 or t in trauma_points or t in observer_resets or
            (t < 100 and t % 25 == 0)):
            avg_psi = np.mean(np.abs(Psi))
            trauma_indicator = " 💥" if t in trauma_points else ""
            observer_reset_indicator = " 🚨" if t in observer_resets else ""
            
            if F < best_F + 0.1:
                trend = " 📈" 
            elif F > best_F + 1.0:
                trend = " 📉"
            else:
                trend = " ➡️"
                
            print(f"Step {t}: F={F:.3f}, KL={mismatch:.1f}, MI={mi:.3f}, "
                  f"|Ψ|={avg_psi:.3f}{trauma_indicator}{observer_reset_indicator}{trend}")

        if F < best_F:
            best_F = F

    return (Psi, F_list, KL_list, MI_list, CtrlDom_list, 
            lamE_hist, lamS_hist, trauma_points, observer_resets)

# ---------------------------
# Visualization and Analysis
# ---------------------------
if __name__ == "__main__":
    print("🚀 Starting OBSERVER-PROTECTED Cognitive Simulation")
    print("   (with Emergency Observer Reset)")
    print("=" * 60)
    
    results = run_simulation_with_observer_protection()
    (Psi, F_list, KL_list, MI_list, CtrlDom_list, 
     lamE_hist, lamS_hist, trauma_points, observer_resets) = results
    
    print("\n" + "=" * 60)
    print("📊 OBSERVER-PROTECTED PERFORMANCE ANALYSIS")
    print("=" * 60)
    
    print(f"Total steps: {len(F_list)}")
    print(f"Trauma events: {len(trauma_points)}")
    print(f"Observer emergency resets: {len(observer_resets)}")
    print(f"Best Free Energy: {min(F_list):.3f}")
    print(f"Final Free Energy: {F_list[-1]:.3f}")
    print(f"Final KL divergence: {KL_list[-1]:.1f}")
    print(f"Final Mutual Information: {MI_list[-1]:.3f}")
    print(f"Final Controller Dominance: {CtrlDom_list[-1]:.3f}")
    
    performance_delta = F_list[-1] - F_list[0]
    print(f"Performance evolution: {F_list[0]:.3f} → {F_list[-1]:.3f} (Δ = {performance_delta:.3f})")
    
    # KL and MI analysis
    kl_improvement = KL_list[0] - KL_list[-1] if len(KL_list) > 1 else 0
    mi_improvement = MI_list[-1] - MI_list[0] if len(MI_list) > 1 else 0
    
    print(f"\n🔍 OBSERVER HEALTH METRICS:")
    print(f"  KL Divergence: {KL_list[0]:.1f} → {KL_list[-1]:.1f} (Δ = {kl_improvement:+.1f})")
    print(f"  Mutual Information: {MI_list[0]:.3f} → {MI_list[-1]:.3f} (Δ = {mi_improvement:+.3f})")
    
    if observer_resets:
        print(f"  Observer emergency resets at: {observer_resets}")
    
    # Performance evaluation
    if KL_list[-1] < 10 and MI_list[-1] > 0.05:
        print(f"\n🎉 OBSERVER HEALTHY - Good integration!")
    elif KL_list[-1] < 15 and MI_list[-1] > 0.02:
        print(f"\n✅ OBSERVER STABLE - Moderate integration")
    elif performance_delta < 2:
        print(f"\n⚠️  SYSTEM STABLE but observer needs work")
    else:
        print(f"\n🔧 OBSERVER NEEDS ATTENTION - High KL divergence")
    
    if trauma_points:
        print(f"💥 Trauma points: {trauma_points}")
    
    # Enhanced visualization
    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 3, 1)
    plt.plot(F_list, color='blue', linewidth=1.5, label='Free Energy')
    for trauma_t in trauma_points:
        if trauma_t < len(F_list):
            plt.axvline(x=trauma_t, color='orange', alpha=0.6, linestyle='-', linewidth=2)
    for reset_t in observer_resets:
        if reset_t < len(F_list):
            plt.axvline(x=reset_t, color='red', alpha=0.4, linestyle='--', linewidth=2)
    plt.title('Free Energy - Observer Protected')
    plt.xlabel('Time Step')
    plt.ylabel('Free Energy')
    plt.legend(['Free Energy', 'Trauma', 'Observer Reset'])
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 3, 2)
    plt.plot(KL_list, color='green', linewidth=1.5)
    plt.axhline(y=10, color='r', linestyle='--', alpha=0.7, label='Healthy Threshold')
    plt.title('KL Divergence')
    plt.xlabel('Time Step')
    plt.ylabel('KL')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 3, 3)
    plt.plot(MI_list, color='purple', linewidth=2)
    plt.title('Mutual Information')
    plt.xlabel('Time Step')
    plt.ylabel('MI')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 3, 4)
    plt.plot(CtrlDom_list, color='orange', linewidth=1.5)
    plt.title('Controller Dominance')
    plt.xlabel('Time Step')
    plt.ylabel('Dominance')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 3, 5)
    plt.plot(lamE_hist, label='λ_E', linewidth=2, color='red')
    plt.plot(lamS_hist, label='λ_S', linewidth=2, color='darkgreen')
    plt.title('Meta-Controller Parameters')
    plt.xlabel('Time Step')
    plt.ylabel('Gain')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 3, 6)
    plt.imshow(Psi, cmap='RdBu_r', aspect='auto')
    plt.title('Final Field State Ψ')
    plt.colorbar()
    
    plt.tight_layout()
    plt.show()
    
    print("\n🎉 OBSERVER-PROTECTED simulation completed!")
