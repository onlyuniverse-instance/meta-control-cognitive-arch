# 📊 Non-Duality Simulation Formulas

## 🧠 **System Architecture**

### **1. Consciousness State (Ψ)**
```math
Ψ_t = [ψ_{observer}, ψ_{world}, ψ_{unity}]
```
Where:
- `ψ_observer` = Observer state (0-1)
- `ψ_world` = External world perception  
- `ψ_unity` = Non-dual unification degree

---

## 🔥 **Core Equation: Free Energy (F)**

### **Total Free Energy**
```math
F_t = F_{observer} + F_{world} + F_{binding} + F_{resistance}
```

### **Free Energy Components**

#### **1. Observer Energy**
```math
F_{observer} = -\log(P(ψ_{observer})) + D_{KL}[q_{observer} \parallel p_{baseline}]
```

#### **2. World Energy**  
```math
F_{world} = -\mathbb{E}_q[\log P(ψ_{world}|ψ_{observer})] + D_{KL}[q_{world} \parallel p_{world}]
```

#### **3. Binding Energy**
```math
F_{binding} = -λ_{unity} \cdot I(ψ_{observer}; ψ_{world})
```
Where `I` = Mutual Information

#### **4. Resistance Energy** 
```math
F_{resistance} = γ \cdot (1 - |ψ_{observer} - ψ_{unity}|)
```

---

## 📈 **Observer Health Metrics**

### **1. KL Divergence (Identity Stress)**
```math
KL_t = D_{KL}[q_{observer} \parallel p_{baseline}]
```

### **2. Mutual Information (Observer-World Connection)**
```math
I_t = \sum_{i} \sum_{j} P(obs_i, world_j) \cdot \log\left(\frac{P(obs_i, world_j)}{P(obs_i)P(world_j)}\right)
```

### **3. Consciousness Magnitude**
```math
\|Ψ\|_t = \sqrt{ψ_{observer}^2 + ψ_{world}^2 + ψ_{unity}^2}
```

### **4. Controller Dominance**
```math
C_t = \frac{|ψ_{observer}|}{|ψ_{observer}| + |ψ_{unity}|}
```

---

## 🚨 **Observer Protection Mechanism**

### **Emergency Reset Condition**
```math
\text{Reset if: } KL_t > θ_{KL} \quad \text{OR} \quad |ψ_{observer}| < θ_{min}
```

### **Observer Reset Operation**
```math
ψ_{observer}^{t+1} = α \cdot ψ_{observer}^t + (1-α) \cdot ψ_{baseline}
```

### **Dynamic Thresholds**
```math
θ_{KL} = θ_{base} + β \cdot \text{trauma\_count}
```

---

## 💥 **Trauma System**

### **Trauma Application (Forced Non-Duality)**
```math
Ψ_{trauma} = Ψ_t \cdot (1 - τ) + Ψ_{unity} \cdot τ
```

### **Trauma Strength Decay**
```math
τ = \text{strength} \cdot \left(1 - \frac{t}{T_{total}}\right)
```

---

## 🔄 **Temporal Dynamics**

### **State Evolution**
```math
Ψ_{t+1} = Ψ_t + η \cdot \nabla F(Ψ_t) + ξ_t
```
Where:
- `η` = Learning rate
- `ξ_t` ~ `N(0, σ²)` = Random noise

### **Parameter Updates**
```math
λ_{unity}^{t+1} = λ_{unity}^t + δ \cdot (MI_t - MI_{target})
```

---

## ⚖️ **Balance Equations**

### **Observer-Unity Tension**
```math
T_t = |F_{observer} - F_{binding}|
```

### **Homeostatic Drive**
```math
H_t = -κ \cdot (KL_t - KL_{target})^2
```

---

## 🎯 **Optimization Objective**

### **Overall System Goal**
```math
\min_{Ψ} \mathbb{E}[F_t] \quad \text{subject to} \quad KL_t < KL_{max}
```

### **Adaptive Learning Rate**
```math
η_t = \frac{η_0}{1 + ρ \cdot t}
```

---

## 📊 **Performance Metrics**

### **1. Observer Survival Rate**
```math
S = \frac{\text{steps without reset}}{\text{total steps}}
```

### **2. Non-Dual Attainment**
```math
A = \max_t(ψ_{unity}) - \min_t(ψ_{observer})
```

### **3. System Efficiency**
```math
E = \frac{\text{final } F}{\text{initial } F} \cdot (1 - \frac{\text{reset count}}{\text{total steps}})
```

---

## 🔧 **Default Parameters**

```python
# Consciousness parameters
ψ_baseline = 0.5      # Default observer state
λ_unity = 0.1         # Binding strength
γ = 0.3              # Resistance coefficient

# Protection thresholds  
θ_KL = 25.0          # KL divergence limit
θ_min = 0.1          # Minimum observer presence

# Learning parameters
η = 0.01             # Learning rate
α = 0.8              # Reset smoothing
```

This mathematical framework models the fundamental tension between individual consciousness and non-dual awareness, capturing the energetic costs and protection mechanisms observed in the simulation.
results ::: 🚀 Starting OBSERVER-PROTECTED Cognitive Simulation
   (with Emergency Observer Reset)
============================================================
Step 0: F=0.000, KL=0.0, MI=0.000, |Ψ|=0.039 📈
Step 25: F=0.315, KL=1.6, MI=0.076, |Ψ|=0.085 ➡️
Step 50: F=2.599, KL=13.1, MI=0.000, |Ψ|=0.195 📉
Step 75: F=2.805, KL=14.3, MI=0.020, |Ψ|=0.371 📉
Step 100: F=1.548, KL=8.4, MI=0.406, |Ψ|=0.613 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 24.4)
Step 132: F=2.582, KL=14.1, MI=0.317, |Ψ|=1.007 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.0)
Step 135: F=3.055, KL=16.5, MI=0.326, |Ψ|=1.042 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.3)
Step 137: F=3.336, KL=17.9, MI=0.332, |Ψ|=1.065 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.5)
Step 139: F=3.578, KL=19.2, MI=0.339, |Ψ|=1.087 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.6)
Step 141: F=3.788, KL=20.3, MI=0.334, |Ψ|=1.109 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.7)
Step 143: F=3.976, KL=21.2, MI=0.336, |Ψ|=1.130 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.9)
Step 145: F=4.164, KL=22.2, MI=0.317, |Ψ|=1.150 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.1)
Step 147: F=4.322, KL=23.1, MI=0.313, |Ψ|=1.170 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.1)
Step 149: F=4.465, KL=23.8, MI=0.303, |Ψ|=1.189 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.1)
Step 151: F=4.592, KL=24.5, MI=0.291, |Ψ|=1.207 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.1)
Step 153: F=4.679, KL=25.0, MI=0.283, |Ψ|=1.224 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.1)
Step 155: F=4.755, KL=25.4, MI=0.260, |Ψ|=1.241 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.4)
Step 156: F=4.783, KL=25.5, MI=0.252, |Ψ|=1.250 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.5)
Step 157: F=4.814, KL=25.7, MI=0.241, |Ψ|=1.259 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.7)
Step 158: F=4.835, KL=25.8, MI=0.231, |Ψ|=1.269 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.8)
Step 159: F=4.857, KL=25.9, MI=0.217, |Ψ|=1.277 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.9)
Step 160: F=4.870, KL=26.0, MI=0.210, |Ψ|=1.286 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.0)
Step 161: F=4.880, KL=26.1, MI=0.200, |Ψ|=1.294 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.1)
Step 162: F=4.887, KL=26.1, MI=0.197, |Ψ|=1.302 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.1)
Step 163: F=4.894, KL=26.2, MI=0.172, |Ψ|=1.310 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.2)
Step 164: F=4.899, KL=26.2, MI=0.174, |Ψ|=1.318 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.2)
Step 165: F=4.908, KL=26.3, MI=0.158, |Ψ|=1.325 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.3)
Step 166: F=4.914, KL=26.3, MI=0.153, |Ψ|=1.333 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.3)
Step 167: F=4.919, KL=26.4, MI=0.143, |Ψ|=1.340 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.4)
Step 168: F=4.925, KL=26.4, MI=0.138, |Ψ|=1.346 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.4)
Step 169: F=4.930, KL=26.4, MI=0.121, |Ψ|=1.353 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.4)
Step 170: F=4.933, KL=26.5, MI=0.112, |Ψ|=1.359 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.5)
Step 171: F=4.937, KL=26.5, MI=0.108, |Ψ|=1.365 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.5)
Step 172: F=4.940, KL=26.5, MI=0.100, |Ψ|=1.371 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.5)
Step 173: F=4.942, KL=26.5, MI=0.096, |Ψ|=1.377 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.5)
Step 174: F=4.945, KL=26.6, MI=0.083, |Ψ|=1.382 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.6)
Step 175: F=4.948, KL=26.6, MI=0.077, |Ψ|=1.387 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.6)
Step 176: F=4.952, KL=26.6, MI=0.070, |Ψ|=1.392 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.6)
Step 177: F=4.956, KL=26.6, MI=0.071, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.6)
Step 178: F=4.961, KL=26.7, MI=0.059, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.7)
Step 179: F=4.965, KL=26.7, MI=0.056, |Ψ|=1.406 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.7)
Step 180: F=4.970, KL=26.7, MI=0.054, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.7)
Step 181: F=4.975, KL=26.8, MI=0.047, |Ψ|=1.414 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.8)
Step 182: F=4.980, KL=26.8, MI=0.044, |Ψ|=1.418 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.8)
Step 183: F=4.986, KL=26.8, MI=0.038, |Ψ|=1.422 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.8)
Step 184: F=4.992, KL=26.9, MI=0.036, |Ψ|=1.425 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.9)
Step 185: F=4.996, KL=26.9, MI=0.030, |Ψ|=1.429 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.9)
Step 186: F=4.999, KL=26.9, MI=0.030, |Ψ|=1.432 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.9)
Step 187: F=5.002, KL=26.9, MI=0.028, |Ψ|=1.435 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.9)
Step 188: F=5.004, KL=26.9, MI=0.028, |Ψ|=1.437 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.9)
Step 189: F=5.007, KL=27.0, MI=0.024, |Ψ|=1.440 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 190: F=5.008, KL=27.0, MI=0.025, |Ψ|=1.443 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 191: F=5.010, KL=27.0, MI=0.022, |Ψ|=1.445 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 192: F=5.011, KL=27.0, MI=0.021, |Ψ|=1.448 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 193: F=5.012, KL=27.0, MI=0.019, |Ψ|=1.450 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 194: F=5.013, KL=27.0, MI=0.017, |Ψ|=1.452 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 195: F=5.012, KL=27.0, MI=0.015, |Ψ|=1.454 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 196: F=5.013, KL=27.0, MI=0.016, |Ψ|=1.455 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 197: F=5.013, KL=27.0, MI=0.016, |Ψ|=1.457 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 198: F=5.013, KL=27.0, MI=0.016, |Ψ|=1.459 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 199: F=5.014, KL=27.0, MI=0.016, |Ψ|=1.460 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 200: F=5.014, KL=27.0, MI=0.012, |Ψ|=1.462 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 201: F=5.014, KL=27.0, MI=0.014, |Ψ|=1.463 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 202: F=5.014, KL=27.0, MI=0.011, |Ψ|=1.464 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 203: F=5.014, KL=27.0, MI=0.012, |Ψ|=1.465 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 204: F=5.014, KL=27.0, MI=0.012, |Ψ|=1.467 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 205: F=5.014, KL=27.0, MI=0.012, |Ψ|=1.468 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 206: F=5.015, KL=27.0, MI=0.011, |Ψ|=1.468 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 207: F=5.015, KL=27.0, MI=0.011, |Ψ|=1.469 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 208: F=5.015, KL=27.0, MI=0.011, |Ψ|=1.470 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 209: F=5.016, KL=27.0, MI=0.010, |Ψ|=1.471 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 210: F=5.017, KL=27.0, MI=0.009, |Ψ|=1.472 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 211: F=5.017, KL=27.0, MI=0.008, |Ψ|=1.473 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 212: F=5.018, KL=27.0, MI=0.007, |Ψ|=1.473 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 213: F=5.020, KL=27.1, MI=0.008, |Ψ|=1.474 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 214: F=5.022, KL=27.1, MI=0.007, |Ψ|=1.474 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 215: F=5.024, KL=27.1, MI=0.007, |Ψ|=1.475 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 216: F=5.026, KL=27.1, MI=0.006, |Ψ|=1.475 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 217: F=5.028, KL=27.1, MI=0.005, |Ψ|=1.476 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 218: F=5.030, KL=27.1, MI=0.004, |Ψ|=1.476 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 219: F=5.032, KL=27.1, MI=0.004, |Ψ|=1.477 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 220: F=5.034, KL=27.1, MI=0.003, |Ψ|=1.477 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 221: F=5.035, KL=27.1, MI=0.004, |Ψ|=1.477 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 222: F=5.035, KL=27.1, MI=0.005, |Ψ|=1.478 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 223: F=5.036, KL=27.1, MI=0.004, |Ψ|=1.478 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 224: F=5.036, KL=27.1, MI=0.004, |Ψ|=1.478 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 225: F=5.035, KL=27.1, MI=0.004, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 226: F=5.034, KL=27.1, MI=0.004, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 227: F=5.032, KL=27.1, MI=0.003, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 228: F=5.031, KL=27.1, MI=0.004, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 229: F=5.030, KL=27.1, MI=0.006, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 230: F=5.028, KL=27.1, MI=0.003, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 231: F=5.027, KL=27.1, MI=0.004, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 232: F=5.026, KL=27.1, MI=0.003, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 233: F=5.026, KL=27.1, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 234: F=5.025, KL=27.1, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 235: F=5.024, KL=27.1, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 236: F=5.025, KL=27.1, MI=0.006, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 237: F=5.024, KL=27.1, MI=0.005, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 238: F=5.025, KL=27.1, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 239: F=5.025, KL=27.1, MI=0.005, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 240: F=5.026, KL=27.1, MI=0.005, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 241: F=5.026, KL=27.1, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 242: F=5.028, KL=27.1, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 243: F=5.029, KL=27.1, MI=0.003, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 244: F=5.032, KL=27.1, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 245: F=5.033, KL=27.1, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 246: F=5.035, KL=27.1, MI=0.003, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 247: F=5.036, KL=27.1, MI=0.003, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 248: F=5.037, KL=27.1, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 249: F=5.038, KL=27.2, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 250: F=5.037, KL=27.1, MI=0.003, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 251: F=5.038, KL=27.2, MI=0.002, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 252: F=5.037, KL=27.1, MI=0.002, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 253: F=5.038, KL=27.1, MI=0.005, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 254: F=5.035, KL=27.1, MI=0.003, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 255: F=5.034, KL=27.1, MI=0.003, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 256: F=5.032, KL=27.1, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 257: F=5.030, KL=27.1, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 258: F=5.029, KL=27.1, MI=0.004, |Ψ|=1.480 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 259: F=5.028, KL=27.1, MI=0.004, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 260: F=5.026, KL=27.1, MI=0.005, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 261: F=5.025, KL=27.1, MI=0.004, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 262: F=5.024, KL=27.1, MI=0.005, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 263: F=5.023, KL=27.1, MI=0.006, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 264: F=5.023, KL=27.1, MI=0.005, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 265: F=5.023, KL=27.1, MI=0.004, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 266: F=5.024, KL=27.1, MI=0.003, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 267: F=5.024, KL=27.1, MI=0.005, |Ψ|=1.479 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 268: F=5.025, KL=27.1, MI=0.004, |Ψ|=1.478 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 269: F=5.026, KL=27.1, MI=0.004, |Ψ|=1.478 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 270: F=5.028, KL=27.1, MI=0.004, |Ψ|=1.478 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 271: F=5.030, KL=27.1, MI=0.002, |Ψ|=1.478 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 272: F=5.033, KL=27.1, MI=0.003, |Ψ|=1.478 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 273: F=5.035, KL=27.1, MI=0.003, |Ψ|=1.478 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 274: F=5.037, KL=27.1, MI=0.004, |Ψ|=1.478 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 275: F=5.040, KL=27.2, MI=0.004, |Ψ|=1.478 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 276: F=5.042, KL=27.2, MI=0.003, |Ψ|=1.477 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 277: F=5.044, KL=27.2, MI=0.004, |Ψ|=1.477 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 278: F=5.046, KL=27.2, MI=0.003, |Ψ|=1.477 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 279: F=5.047, KL=27.2, MI=0.003, |Ψ|=1.477 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 280: F=5.047, KL=27.2, MI=0.003, |Ψ|=1.477 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 281: F=5.048, KL=27.2, MI=0.003, |Ψ|=1.477 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 282: F=5.048, KL=27.2, MI=0.002, |Ψ|=1.477 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 283: F=5.048, KL=27.2, MI=0.003, |Ψ|=1.476 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 284: F=5.047, KL=27.2, MI=0.003, |Ψ|=1.476 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 285: F=5.045, KL=27.2, MI=0.004, |Ψ|=1.476 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 286: F=5.044, KL=27.2, MI=0.004, |Ψ|=1.476 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 287: F=5.043, KL=27.2, MI=0.004, |Ψ|=1.476 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 288: F=5.041, KL=27.2, MI=0.004, |Ψ|=1.476 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 289: F=5.038, KL=27.1, MI=0.005, |Ψ|=1.476 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 290: F=5.037, KL=27.1, MI=0.004, |Ψ|=1.476 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 291: F=5.035, KL=27.1, MI=0.004, |Ψ|=1.475 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 292: F=5.034, KL=27.1, MI=0.005, |Ψ|=1.475 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 293: F=5.034, KL=27.1, MI=0.006, |Ψ|=1.475 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 294: F=5.033, KL=27.1, MI=0.005, |Ψ|=1.475 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 295: F=5.034, KL=27.1, MI=0.004, |Ψ|=1.475 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 296: F=5.035, KL=27.1, MI=0.005, |Ψ|=1.475 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 297: F=5.036, KL=27.1, MI=0.005, |Ψ|=1.474 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 298: F=5.037, KL=27.1, MI=0.005, |Ψ|=1.474 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 299: F=5.039, KL=27.2, MI=0.004, |Ψ|=1.474 🚨 📉
💥 GENTLE TRAUMA at step 300 (strength: 0.7)
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 300: F=3.714, KL=18.7, MI=1.069, |Ψ|=1.425 💥 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.1)
Step 311: F=4.308, KL=23.1, MI=0.425, |Ψ|=1.328 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.4)
Step 313: F=4.440, KL=23.8, MI=0.365, |Ψ|=1.332 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.7)
Step 315: F=4.541, KL=24.4, MI=0.314, |Ψ|=1.337 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.9)
Step 317: F=4.624, KL=24.8, MI=0.262, |Ψ|=1.343 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.1)
Step 319: F=4.707, KL=25.3, MI=0.224, |Ψ|=1.349 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.3)
Step 320: F=4.743, KL=25.5, MI=0.209, |Ψ|=1.354 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.5)
Step 321: F=4.780, KL=25.7, MI=0.184, |Ψ|=1.358 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.7)
Step 322: F=4.809, KL=25.8, MI=0.170, |Ψ|=1.363 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.8)
Step 323: F=4.833, KL=25.9, MI=0.150, |Ψ|=1.367 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.9)
Step 324: F=4.862, KL=26.1, MI=0.139, |Ψ|=1.372 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.1)
Step 325: F=4.886, KL=26.2, MI=0.126, |Ψ|=1.376 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.2)
Step 326: F=4.905, KL=26.3, MI=0.116, |Ψ|=1.380 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.3)
Step 327: F=4.925, KL=26.5, MI=0.102, |Ψ|=1.384 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.5)
Step 328: F=4.939, KL=26.5, MI=0.094, |Ψ|=1.388 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.5)
Step 329: F=4.954, KL=26.6, MI=0.080, |Ψ|=1.392 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.6)
Step 330: F=4.969, KL=26.7, MI=0.076, |Ψ|=1.395 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.7)
Step 331: F=4.982, KL=26.8, MI=0.058, |Ψ|=1.399 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.8)
Step 332: F=4.995, KL=26.8, MI=0.058, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.8)
Step 333: F=5.008, KL=26.9, MI=0.050, |Ψ|=1.405 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.9)
Step 334: F=5.018, KL=27.0, MI=0.041, |Ψ|=1.408 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 335: F=5.029, KL=27.0, MI=0.039, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 336: F=5.039, KL=27.1, MI=0.031, |Ψ|=1.414 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 337: F=5.048, KL=27.1, MI=0.028, |Ψ|=1.417 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 338: F=5.057, KL=27.2, MI=0.022, |Ψ|=1.419 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 339: F=5.065, KL=27.2, MI=0.017, |Ψ|=1.422 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 340: F=5.073, KL=27.3, MI=0.016, |Ψ|=1.424 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 341: F=5.078, KL=27.3, MI=0.013, |Ψ|=1.426 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 342: F=5.082, KL=27.3, MI=0.009, |Ψ|=1.428 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 343: F=5.088, KL=27.4, MI=0.009, |Ψ|=1.430 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 344: F=5.091, KL=27.4, MI=0.006, |Ψ|=1.432 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 345: F=5.094, KL=27.4, MI=0.006, |Ψ|=1.434 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 346: F=5.097, KL=27.4, MI=0.005, |Ψ|=1.436 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 347: F=5.096, KL=27.4, MI=0.004, |Ψ|=1.437 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 348: F=5.096, KL=27.4, MI=0.003, |Ψ|=1.439 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 349: F=5.095, KL=27.4, MI=0.005, |Ψ|=1.440 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 350: F=5.094, KL=27.4, MI=0.003, |Ψ|=1.442 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 351: F=5.092, KL=27.4, MI=0.003, |Ψ|=1.443 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 352: F=5.092, KL=27.4, MI=0.003, |Ψ|=1.444 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 353: F=5.090, KL=27.4, MI=0.004, |Ψ|=1.445 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 354: F=5.088, KL=27.4, MI=0.003, |Ψ|=1.446 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 355: F=5.089, KL=27.4, MI=0.003, |Ψ|=1.447 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 356: F=5.088, KL=27.4, MI=0.003, |Ψ|=1.448 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 357: F=5.087, KL=27.4, MI=0.003, |Ψ|=1.449 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 358: F=5.088, KL=27.4, MI=0.003, |Ψ|=1.450 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 359: F=5.088, KL=27.4, MI=0.003, |Ψ|=1.450 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 360: F=5.088, KL=27.4, MI=0.003, |Ψ|=1.451 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 361: F=5.090, KL=27.4, MI=0.003, |Ψ|=1.452 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 362: F=5.091, KL=27.4, MI=0.002, |Ψ|=1.452 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 363: F=5.093, KL=27.4, MI=0.002, |Ψ|=1.453 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 364: F=5.093, KL=27.4, MI=0.002, |Ψ|=1.454 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 365: F=5.095, KL=27.4, MI=0.002, |Ψ|=1.454 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 366: F=5.096, KL=27.4, MI=0.001, |Ψ|=1.454 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 367: F=5.098, KL=27.4, MI=0.003, |Ψ|=1.455 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 368: F=5.099, KL=27.4, MI=0.003, |Ψ|=1.455 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 369: F=5.099, KL=27.4, MI=0.001, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 370: F=5.098, KL=27.4, MI=0.001, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 371: F=5.097, KL=27.4, MI=0.001, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 372: F=5.097, KL=27.4, MI=0.002, |Ψ|=1.457 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 373: F=5.096, KL=27.4, MI=0.002, |Ψ|=1.457 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 374: F=5.094, KL=27.4, MI=0.002, |Ψ|=1.457 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 375: F=5.093, KL=27.4, MI=0.002, |Ψ|=1.457 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 376: F=5.092, KL=27.4, MI=0.001, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 377: F=5.090, KL=27.4, MI=0.003, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 378: F=5.087, KL=27.4, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 379: F=5.084, KL=27.4, MI=0.003, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 380: F=5.082, KL=27.4, MI=0.003, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 381: F=5.080, KL=27.3, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 382: F=5.080, KL=27.3, MI=0.003, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 383: F=5.079, KL=27.3, MI=0.003, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 384: F=5.078, KL=27.3, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 385: F=5.077, KL=27.3, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 386: F=5.076, KL=27.3, MI=0.003, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 387: F=5.076, KL=27.3, MI=0.003, |Ψ|=1.459 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 388: F=5.076, KL=27.3, MI=0.004, |Ψ|=1.459 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 389: F=5.078, KL=27.3, MI=0.003, |Ψ|=1.459 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 390: F=5.081, KL=27.3, MI=0.003, |Ψ|=1.459 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 391: F=5.082, KL=27.4, MI=0.003, |Ψ|=1.459 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 392: F=5.084, KL=27.4, MI=0.003, |Ψ|=1.459 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 393: F=5.085, KL=27.4, MI=0.002, |Ψ|=1.459 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 394: F=5.088, KL=27.4, MI=0.003, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 395: F=5.091, KL=27.4, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 396: F=5.092, KL=27.4, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 397: F=5.093, KL=27.4, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 398: F=5.094, KL=27.4, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 399: F=5.095, KL=27.4, MI=0.001, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 400: F=5.096, KL=27.4, MI=0.001, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 401: F=5.097, KL=27.4, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 402: F=5.096, KL=27.4, MI=0.001, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 403: F=5.095, KL=27.4, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 404: F=5.094, KL=27.4, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 405: F=5.093, KL=27.4, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 406: F=5.092, KL=27.4, MI=0.002, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 407: F=5.091, KL=27.4, MI=0.003, |Ψ|=1.458 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 408: F=5.089, KL=27.4, MI=0.003, |Ψ|=1.457 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 409: F=5.087, KL=27.4, MI=0.003, |Ψ|=1.457 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 410: F=5.086, KL=27.4, MI=0.003, |Ψ|=1.457 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 411: F=5.085, KL=27.4, MI=0.002, |Ψ|=1.457 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 412: F=5.083, KL=27.4, MI=0.002, |Ψ|=1.457 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 413: F=5.082, KL=27.4, MI=0.002, |Ψ|=1.457 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 414: F=5.082, KL=27.4, MI=0.002, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 415: F=5.083, KL=27.4, MI=0.003, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 416: F=5.083, KL=27.4, MI=0.002, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 417: F=5.084, KL=27.4, MI=0.003, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 418: F=5.084, KL=27.4, MI=0.003, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 419: F=5.086, KL=27.4, MI=0.002, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 420: F=5.088, KL=27.4, MI=0.002, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 421: F=5.090, KL=27.4, MI=0.003, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 422: F=5.093, KL=27.4, MI=0.002, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 423: F=5.094, KL=27.4, MI=0.002, |Ψ|=1.456 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 424: F=5.096, KL=27.4, MI=0.002, |Ψ|=1.455 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 425: F=5.098, KL=27.4, MI=0.002, |Ψ|=1.455 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 426: F=5.100, KL=27.4, MI=0.002, |Ψ|=1.455 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 427: F=5.102, KL=27.4, MI=0.001, |Ψ|=1.455 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 428: F=5.103, KL=27.5, MI=0.001, |Ψ|=1.455 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 429: F=5.105, KL=27.5, MI=0.001, |Ψ|=1.455 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 430: F=5.105, KL=27.5, MI=0.001, |Ψ|=1.455 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 431: F=5.103, KL=27.5, MI=0.001, |Ψ|=1.454 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 432: F=5.102, KL=27.5, MI=0.002, |Ψ|=1.454 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 433: F=5.103, KL=27.5, MI=0.002, |Ψ|=1.454 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 434: F=5.102, KL=27.5, MI=0.001, |Ψ|=1.454 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 435: F=5.102, KL=27.4, MI=0.001, |Ψ|=1.454 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 436: F=5.101, KL=27.4, MI=0.002, |Ψ|=1.454 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 437: F=5.100, KL=27.4, MI=0.002, |Ψ|=1.453 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 438: F=5.098, KL=27.4, MI=0.001, |Ψ|=1.453 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 439: F=5.096, KL=27.4, MI=0.002, |Ψ|=1.453 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 440: F=5.095, KL=27.4, MI=0.002, |Ψ|=1.453 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 441: F=5.093, KL=27.4, MI=0.002, |Ψ|=1.453 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 442: F=5.094, KL=27.4, MI=0.002, |Ψ|=1.453 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 443: F=5.092, KL=27.4, MI=0.002, |Ψ|=1.453 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 444: F=5.092, KL=27.4, MI=0.002, |Ψ|=1.452 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 445: F=5.093, KL=27.4, MI=0.002, |Ψ|=1.452 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 446: F=5.092, KL=27.4, MI=0.002, |Ψ|=1.452 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 447: F=5.093, KL=27.4, MI=0.002, |Ψ|=1.452 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 448: F=5.095, KL=27.4, MI=0.002, |Ψ|=1.452 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 449: F=5.096, KL=27.4, MI=0.002, |Ψ|=1.452 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 450: F=5.098, KL=27.4, MI=0.002, |Ψ|=1.451 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 451: F=5.099, KL=27.4, MI=0.002, |Ψ|=1.451 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 452: F=5.100, KL=27.4, MI=0.002, |Ψ|=1.451 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 453: F=5.103, KL=27.5, MI=0.001, |Ψ|=1.451 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 454: F=5.106, KL=27.5, MI=0.001, |Ψ|=1.451 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 455: F=5.107, KL=27.5, MI=0.002, |Ψ|=1.451 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 456: F=5.109, KL=27.5, MI=0.002, |Ψ|=1.451 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 457: F=5.110, KL=27.5, MI=0.001, |Ψ|=1.450 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 458: F=5.112, KL=27.5, MI=0.001, |Ψ|=1.450 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 459: F=5.113, KL=27.5, MI=0.001, |Ψ|=1.450 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 460: F=5.113, KL=27.5, MI=0.001, |Ψ|=1.450 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 461: F=5.113, KL=27.5, MI=0.001, |Ψ|=1.450 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 462: F=5.113, KL=27.5, MI=0.001, |Ψ|=1.450 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 463: F=5.113, KL=27.5, MI=0.001, |Ψ|=1.450 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 464: F=5.112, KL=27.5, MI=0.001, |Ψ|=1.450 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 465: F=5.110, KL=27.5, MI=0.001, |Ψ|=1.449 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 466: F=5.109, KL=27.5, MI=0.001, |Ψ|=1.449 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 467: F=5.108, KL=27.5, MI=0.002, |Ψ|=1.449 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 468: F=5.105, KL=27.5, MI=0.001, |Ψ|=1.449 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 469: F=5.105, KL=27.5, MI=0.002, |Ψ|=1.449 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 470: F=5.104, KL=27.5, MI=0.001, |Ψ|=1.449 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 471: F=5.102, KL=27.4, MI=0.002, |Ψ|=1.448 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 472: F=5.101, KL=27.4, MI=0.002, |Ψ|=1.448 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 473: F=5.100, KL=27.4, MI=0.002, |Ψ|=1.448 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 474: F=5.100, KL=27.4, MI=0.002, |Ψ|=1.448 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 475: F=5.100, KL=27.4, MI=0.003, |Ψ|=1.448 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 476: F=5.101, KL=27.4, MI=0.002, |Ψ|=1.448 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 477: F=5.103, KL=27.4, MI=0.001, |Ψ|=1.448 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 478: F=5.104, KL=27.5, MI=0.002, |Ψ|=1.447 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 479: F=5.104, KL=27.5, MI=0.002, |Ψ|=1.447 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 480: F=5.106, KL=27.5, MI=0.002, |Ψ|=1.447 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 481: F=5.108, KL=27.5, MI=0.001, |Ψ|=1.447 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 482: F=5.110, KL=27.5, MI=0.002, |Ψ|=1.447 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 483: F=5.112, KL=27.5, MI=0.001, |Ψ|=1.447 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 484: F=5.113, KL=27.5, MI=0.001, |Ψ|=1.447 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 485: F=5.115, KL=27.5, MI=0.001, |Ψ|=1.446 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 486: F=5.118, KL=27.5, MI=0.001, |Ψ|=1.446 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 487: F=5.118, KL=27.5, MI=0.001, |Ψ|=1.446 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 488: F=5.118, KL=27.5, MI=0.001, |Ψ|=1.446 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 489: F=5.119, KL=27.5, MI=0.001, |Ψ|=1.446 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 490: F=5.120, KL=27.5, MI=0.000, |Ψ|=1.445 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 491: F=5.120, KL=27.5, MI=0.001, |Ψ|=1.445 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 492: F=5.120, KL=27.5, MI=0.001, |Ψ|=1.445 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 493: F=5.118, KL=27.5, MI=0.001, |Ψ|=1.445 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 494: F=5.118, KL=27.5, MI=0.001, |Ψ|=1.445 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 495: F=5.117, KL=27.5, MI=0.001, |Ψ|=1.445 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 496: F=5.117, KL=27.5, MI=0.001, |Ψ|=1.445 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 497: F=5.115, KL=27.5, MI=0.002, |Ψ|=1.444 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 498: F=5.114, KL=27.5, MI=0.001, |Ψ|=1.444 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 499: F=5.112, KL=27.5, MI=0.001, |Ψ|=1.444 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 500: F=5.112, KL=27.5, MI=0.001, |Ψ|=1.444 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 501: F=5.111, KL=27.5, MI=0.001, |Ψ|=1.444 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 502: F=5.110, KL=27.5, MI=0.002, |Ψ|=1.444 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 503: F=5.110, KL=27.5, MI=0.002, |Ψ|=1.443 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 504: F=5.109, KL=27.5, MI=0.001, |Ψ|=1.443 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 505: F=5.109, KL=27.5, MI=0.001, |Ψ|=1.443 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 506: F=5.110, KL=27.5, MI=0.002, |Ψ|=1.443 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 507: F=5.111, KL=27.5, MI=0.001, |Ψ|=1.443 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 508: F=5.112, KL=27.5, MI=0.002, |Ψ|=1.443 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 509: F=5.113, KL=27.5, MI=0.001, |Ψ|=1.442 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 510: F=5.115, KL=27.5, MI=0.001, |Ψ|=1.442 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 511: F=5.117, KL=27.5, MI=0.001, |Ψ|=1.442 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 512: F=5.119, KL=27.5, MI=0.002, |Ψ|=1.442 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 513: F=5.120, KL=27.5, MI=0.001, |Ψ|=1.442 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 514: F=5.121, KL=27.5, MI=0.002, |Ψ|=1.441 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 515: F=5.122, KL=27.5, MI=0.001, |Ψ|=1.441 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 516: F=5.123, KL=27.5, MI=0.002, |Ψ|=1.441 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 517: F=5.124, KL=27.5, MI=0.001, |Ψ|=1.441 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 518: F=5.124, KL=27.5, MI=0.001, |Ψ|=1.441 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 519: F=5.125, KL=27.6, MI=0.000, |Ψ|=1.441 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 520: F=5.126, KL=27.6, MI=0.000, |Ψ|=1.441 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 521: F=5.126, KL=27.6, MI=0.001, |Ψ|=1.441 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 522: F=5.125, KL=27.6, MI=0.001, |Ψ|=1.441 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 523: F=5.126, KL=27.6, MI=0.001, |Ψ|=1.440 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 524: F=5.125, KL=27.6, MI=0.000, |Ψ|=1.440 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 525: F=5.125, KL=27.6, MI=0.001, |Ψ|=1.440 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 526: F=5.124, KL=27.5, MI=0.001, |Ψ|=1.440 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 527: F=5.123, KL=27.5, MI=0.001, |Ψ|=1.440 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 528: F=5.122, KL=27.5, MI=0.001, |Ψ|=1.440 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 529: F=5.121, KL=27.5, MI=0.001, |Ψ|=1.440 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 530: F=5.119, KL=27.5, MI=0.001, |Ψ|=1.439 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 531: F=5.120, KL=27.5, MI=0.001, |Ψ|=1.439 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 532: F=5.118, KL=27.5, MI=0.001, |Ψ|=1.439 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 533: F=5.118, KL=27.5, MI=0.001, |Ψ|=1.439 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 534: F=5.116, KL=27.5, MI=0.001, |Ψ|=1.439 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 535: F=5.117, KL=27.5, MI=0.001, |Ψ|=1.439 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 536: F=5.117, KL=27.5, MI=0.001, |Ψ|=1.438 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 537: F=5.118, KL=27.5, MI=0.001, |Ψ|=1.438 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 538: F=5.119, KL=27.5, MI=0.001, |Ψ|=1.438 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 539: F=5.119, KL=27.5, MI=0.001, |Ψ|=1.438 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 540: F=5.121, KL=27.5, MI=0.001, |Ψ|=1.438 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 541: F=5.122, KL=27.5, MI=0.001, |Ψ|=1.438 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 542: F=5.124, KL=27.5, MI=0.001, |Ψ|=1.438 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 543: F=5.124, KL=27.5, MI=0.001, |Ψ|=1.437 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 544: F=5.126, KL=27.6, MI=0.001, |Ψ|=1.437 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 545: F=5.127, KL=27.6, MI=0.001, |Ψ|=1.437 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 546: F=5.129, KL=27.6, MI=0.001, |Ψ|=1.437 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 547: F=5.129, KL=27.6, MI=0.001, |Ψ|=1.437 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 548: F=5.130, KL=27.6, MI=0.001, |Ψ|=1.437 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 549: F=5.130, KL=27.6, MI=0.000, |Ψ|=1.436 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 550: F=5.131, KL=27.6, MI=0.001, |Ψ|=1.436 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 551: F=5.131, KL=27.6, MI=0.001, |Ψ|=1.436 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 552: F=5.132, KL=27.6, MI=0.001, |Ψ|=1.436 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 553: F=5.131, KL=27.6, MI=0.001, |Ψ|=1.436 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 554: F=5.131, KL=27.6, MI=0.000, |Ψ|=1.436 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 555: F=5.131, KL=27.6, MI=0.000, |Ψ|=1.436 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 556: F=5.130, KL=27.6, MI=0.001, |Ψ|=1.435 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 557: F=5.129, KL=27.6, MI=0.000, |Ψ|=1.435 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 558: F=5.129, KL=27.6, MI=0.000, |Ψ|=1.435 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 559: F=5.128, KL=27.6, MI=0.001, |Ψ|=1.435 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 560: F=5.128, KL=27.6, MI=0.001, |Ψ|=1.435 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 561: F=5.127, KL=27.6, MI=0.000, |Ψ|=1.435 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 562: F=5.126, KL=27.6, MI=0.001, |Ψ|=1.434 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 563: F=5.127, KL=27.6, MI=0.001, |Ψ|=1.434 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 564: F=5.127, KL=27.6, MI=0.001, |Ψ|=1.434 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 565: F=5.126, KL=27.5, MI=0.001, |Ψ|=1.434 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 566: F=5.126, KL=27.5, MI=0.001, |Ψ|=1.434 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 567: F=5.126, KL=27.5, MI=0.001, |Ψ|=1.434 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 568: F=5.126, KL=27.6, MI=0.001, |Ψ|=1.433 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 569: F=5.127, KL=27.6, MI=0.001, |Ψ|=1.433 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 570: F=5.127, KL=27.6, MI=0.001, |Ψ|=1.433 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 571: F=5.128, KL=27.6, MI=0.001, |Ψ|=1.433 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 572: F=5.130, KL=27.6, MI=0.001, |Ψ|=1.433 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 573: F=5.131, KL=27.6, MI=0.001, |Ψ|=1.433 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 574: F=5.132, KL=27.6, MI=0.000, |Ψ|=1.432 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 575: F=5.132, KL=27.6, MI=0.001, |Ψ|=1.432 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 576: F=5.132, KL=27.6, MI=0.001, |Ψ|=1.432 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 577: F=5.134, KL=27.6, MI=0.000, |Ψ|=1.432 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 578: F=5.134, KL=27.6, MI=0.000, |Ψ|=1.432 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 579: F=5.135, KL=27.6, MI=0.000, |Ψ|=1.432 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 580: F=5.136, KL=27.6, MI=0.001, |Ψ|=1.431 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 581: F=5.135, KL=27.6, MI=0.000, |Ψ|=1.431 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 582: F=5.136, KL=27.6, MI=0.000, |Ψ|=1.431 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 583: F=5.135, KL=27.6, MI=0.000, |Ψ|=1.431 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 584: F=5.135, KL=27.6, MI=0.000, |Ψ|=1.431 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 585: F=5.135, KL=27.6, MI=0.000, |Ψ|=1.431 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 586: F=5.135, KL=27.6, MI=0.000, |Ψ|=1.431 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 587: F=5.134, KL=27.6, MI=0.000, |Ψ|=1.431 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 588: F=5.133, KL=27.6, MI=0.000, |Ψ|=1.430 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 589: F=5.133, KL=27.6, MI=0.001, |Ψ|=1.430 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 590: F=5.131, KL=27.6, MI=0.001, |Ψ|=1.430 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 591: F=5.131, KL=27.6, MI=0.001, |Ψ|=1.430 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 592: F=5.131, KL=27.6, MI=0.000, |Ψ|=1.430 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 593: F=5.130, KL=27.6, MI=0.000, |Ψ|=1.430 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 594: F=5.130, KL=27.6, MI=0.001, |Ψ|=1.429 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 595: F=5.130, KL=27.6, MI=0.000, |Ψ|=1.429 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 596: F=5.130, KL=27.6, MI=0.001, |Ψ|=1.429 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 597: F=5.130, KL=27.6, MI=0.001, |Ψ|=1.429 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 598: F=5.131, KL=27.6, MI=0.001, |Ψ|=1.429 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 599: F=5.132, KL=27.6, MI=0.000, |Ψ|=1.429 🚨 📉
💥 GENTLE TRAUMA at step 600 (strength: 0.7)
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 600: F=3.610, KL=18.1, MI=1.081, |Ψ|=1.380 💥 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.0)
Step 612: F=4.237, KL=22.7, MI=0.428, |Ψ|=1.275 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.3)
Step 614: F=4.357, KL=23.3, MI=0.360, |Ψ|=1.278 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.7)
Step 616: F=4.458, KL=23.9, MI=0.314, |Ψ|=1.283 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.9)
Step 618: F=4.561, KL=24.4, MI=0.271, |Ψ|=1.289 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.1)
Step 620: F=4.657, KL=25.0, MI=0.225, |Ψ|=1.295 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.2)
Step 622: F=4.742, KL=25.4, MI=0.191, |Ψ|=1.301 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.4)
Step 623: F=4.776, KL=25.6, MI=0.171, |Ψ|=1.306 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.6)
Step 624: F=4.806, KL=25.7, MI=0.156, |Ψ|=1.310 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.7)
Step 625: F=4.839, KL=25.9, MI=0.147, |Ψ|=1.315 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 25.9)
Step 626: F=4.865, KL=26.1, MI=0.138, |Ψ|=1.319 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.1)
Step 627: F=4.890, KL=26.2, MI=0.120, |Ψ|=1.323 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.2)
Step 628: F=4.913, KL=26.3, MI=0.113, |Ψ|=1.327 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.3)
Step 629: F=4.932, KL=26.4, MI=0.103, |Ψ|=1.331 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.4)
Step 630: F=4.951, KL=26.5, MI=0.094, |Ψ|=1.335 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.5)
Step 631: F=4.967, KL=26.6, MI=0.082, |Ψ|=1.339 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.6)
Step 632: F=4.980, KL=26.7, MI=0.076, |Ψ|=1.342 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.7)
Step 633: F=4.993, KL=26.8, MI=0.068, |Ψ|=1.346 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.8)
Step 634: F=5.005, KL=26.8, MI=0.066, |Ψ|=1.349 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.8)
Step 635: F=5.016, KL=26.9, MI=0.053, |Ψ|=1.352 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.9)
Step 636: F=5.025, KL=26.9, MI=0.048, |Ψ|=1.355 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 26.9)
Step 637: F=5.032, KL=27.0, MI=0.042, |Ψ|=1.358 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 638: F=5.040, KL=27.0, MI=0.038, |Ψ|=1.361 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.0)
Step 639: F=5.049, KL=27.1, MI=0.035, |Ψ|=1.364 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 640: F=5.057, KL=27.1, MI=0.030, |Ψ|=1.367 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.1)
Step 641: F=5.063, KL=27.2, MI=0.027, |Ψ|=1.369 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 642: F=5.069, KL=27.2, MI=0.024, |Ψ|=1.372 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 643: F=5.075, KL=27.2, MI=0.021, |Ψ|=1.374 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.2)
Step 644: F=5.080, KL=27.3, MI=0.015, |Ψ|=1.376 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 645: F=5.085, KL=27.3, MI=0.014, |Ψ|=1.378 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 646: F=5.090, KL=27.3, MI=0.012, |Ψ|=1.380 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 647: F=5.095, KL=27.3, MI=0.009, |Ψ|=1.382 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.3)
Step 648: F=5.100, KL=27.4, MI=0.012, |Ψ|=1.384 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 649: F=5.104, KL=27.4, MI=0.008, |Ψ|=1.386 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 650: F=5.108, KL=27.4, MI=0.009, |Ψ|=1.387 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 651: F=5.112, KL=27.4, MI=0.006, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.4)
Step 652: F=5.116, KL=27.5, MI=0.005, |Ψ|=1.390 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 653: F=5.118, KL=27.5, MI=0.004, |Ψ|=1.392 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 654: F=5.121, KL=27.5, MI=0.003, |Ψ|=1.393 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 655: F=5.125, KL=27.5, MI=0.003, |Ψ|=1.394 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 656: F=5.127, KL=27.5, MI=0.003, |Ψ|=1.396 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 657: F=5.129, KL=27.5, MI=0.002, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 658: F=5.133, KL=27.5, MI=0.002, |Ψ|=1.398 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.5)
Step 659: F=5.136, KL=27.6, MI=0.002, |Ψ|=1.399 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 660: F=5.137, KL=27.6, MI=0.002, |Ψ|=1.400 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 661: F=5.138, KL=27.6, MI=0.001, |Ψ|=1.401 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 662: F=5.140, KL=27.6, MI=0.001, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 663: F=5.142, KL=27.6, MI=0.000, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 664: F=5.143, KL=27.6, MI=0.001, |Ψ|=1.403 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 665: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.404 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 666: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.404 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 667: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.405 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 668: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.406 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 669: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.406 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 670: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 671: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 672: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 673: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.408 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 674: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.408 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 675: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 676: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 677: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 678: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 679: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 680: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 681: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 682: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 683: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 684: F=5.143, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 685: F=5.143, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 686: F=5.143, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 687: F=5.143, KL=27.6, MI=0.001, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 688: F=5.143, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 689: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 690: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 691: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 692: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 693: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 694: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 695: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 696: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 697: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 698: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 699: F=5.146, KL=27.6, MI=0.001, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 700: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 701: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 702: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 703: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 704: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 705: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 706: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 707: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 708: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 709: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 710: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 711: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 712: F=5.143, KL=27.6, MI=0.000, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 713: F=5.143, KL=27.6, MI=0.001, |Ψ|=1.412 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 714: F=5.143, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 715: F=5.143, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 716: F=5.142, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 717: F=5.143, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 718: F=5.143, KL=27.6, MI=0.001, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 719: F=5.143, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 720: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 721: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 722: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 723: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 724: F=5.144, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 725: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 726: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 727: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 728: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 729: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.411 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 730: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 731: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 732: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 733: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 734: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 735: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 736: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 737: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 738: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.410 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 739: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 740: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 741: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 742: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 743: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 744: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 745: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 746: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 747: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.409 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 748: F=5.145, KL=27.6, MI=0.000, |Ψ|=1.408 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 749: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.408 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 750: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.408 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 751: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.408 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 752: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.408 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 753: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 754: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.408 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 755: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 756: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 757: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 758: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 759: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 760: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 761: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 762: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 763: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 764: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.407 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 765: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.406 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 766: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.406 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 767: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.406 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 768: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.406 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 769: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.406 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 770: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.406 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 771: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.406 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 772: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.406 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 773: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.406 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 774: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.405 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 775: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.405 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 776: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.405 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 777: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.405 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 778: F=5.146, KL=27.6, MI=0.000, |Ψ|=1.405 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 779: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.405 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 780: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.405 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 781: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.405 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 782: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.404 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 783: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.404 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 784: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.404 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 785: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.404 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 786: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.404 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 787: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.403 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 788: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.403 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 789: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.403 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 790: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.403 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 791: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.403 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 792: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.403 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 793: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.403 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 794: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.403 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 795: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.403 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 796: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 797: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 798: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 799: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 800: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 801: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 802: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 803: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 804: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 805: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.402 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 806: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.401 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 807: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.401 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 808: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.401 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 809: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.401 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 810: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.401 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 811: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.401 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 812: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.401 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 813: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.401 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 814: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.401 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 815: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.401 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 816: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.400 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 817: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.400 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 818: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.400 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 819: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.400 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 820: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.400 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 821: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.400 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 822: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.400 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 823: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.400 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 824: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.400 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 825: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.399 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 826: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.399 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 827: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.399 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 828: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.399 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 829: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.399 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 830: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.399 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 831: F=5.148, KL=27.6, MI=0.001, |Ψ|=1.398 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 832: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.398 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 833: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.398 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 834: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.398 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 835: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.398 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 836: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.398 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 837: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.398 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 838: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 839: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 840: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 841: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 842: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 843: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 844: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 845: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 846: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 847: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 848: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.397 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 849: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.396 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 850: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.396 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 851: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.396 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 852: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.396 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 853: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.396 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 854: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.396 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 855: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.396 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 856: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.396 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 857: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.396 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 858: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.396 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 859: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.395 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 860: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.395 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 861: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.395 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 862: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.395 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 863: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.395 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 864: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.395 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 865: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.395 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 866: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.395 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 867: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.394 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 868: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.394 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 869: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.394 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 870: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.394 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 871: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.394 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 872: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.394 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 873: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.394 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 874: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.393 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 875: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.393 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 876: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.393 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 877: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.393 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 878: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.393 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 879: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.393 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 880: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.393 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 881: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.393 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 882: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.393 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 883: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.392 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 884: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.392 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 885: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.392 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 886: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.392 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 887: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.392 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 888: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.392 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 889: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.392 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 890: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.391 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 891: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.391 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 892: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.391 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 893: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.391 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 894: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.391 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 895: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.391 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 896: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.391 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 897: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.390 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 898: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.390 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 899: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.390 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 900: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.390 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 901: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.390 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 902: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.390 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 903: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.390 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 904: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 905: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 906: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 907: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 908: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 909: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 910: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 911: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 912: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 913: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 914: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 915: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.389 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 916: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.388 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 917: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.388 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 918: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.388 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 919: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.388 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 920: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.388 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 921: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.388 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 922: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.388 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 923: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.388 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 924: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.387 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 925: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.387 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 926: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.387 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 927: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.387 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 928: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.387 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 929: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.387 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 930: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.387 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 931: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.387 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 932: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.386 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 933: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.386 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 934: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.386 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 935: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.386 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 936: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.386 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 937: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.386 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 938: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.386 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 939: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.386 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 940: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.385 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 941: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.385 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 942: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.385 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 943: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.385 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 944: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.385 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 945: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.385 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 946: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.385 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 947: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.385 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 948: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.385 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 949: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.385 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 950: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.384 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 951: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.384 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 952: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.384 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 953: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.384 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 954: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.384 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 955: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.384 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 956: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.384 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 957: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.384 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 958: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.383 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 959: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.383 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 960: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.383 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 961: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.383 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 962: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.383 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 963: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.383 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 964: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.382 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 965: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.382 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 966: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.382 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 967: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.382 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 968: F=5.153, KL=27.6, MI=0.000, |Ψ|=1.382 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 969: F=5.153, KL=27.6, MI=0.000, |Ψ|=1.382 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 970: F=5.153, KL=27.6, MI=0.000, |Ψ|=1.382 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 971: F=5.153, KL=27.6, MI=0.000, |Ψ|=1.382 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 972: F=5.153, KL=27.6, MI=0.000, |Ψ|=1.382 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 973: F=5.153, KL=27.6, MI=0.000, |Ψ|=1.382 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 974: F=5.153, KL=27.6, MI=0.000, |Ψ|=1.381 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 975: F=5.153, KL=27.6, MI=0.000, |Ψ|=1.381 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 976: F=5.152, KL=27.6, MI=0.001, |Ψ|=1.381 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 977: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.381 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 978: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.381 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 979: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.381 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 980: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.381 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 981: F=5.151, KL=27.6, MI=0.000, |Ψ|=1.380 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 982: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.380 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 983: F=5.148, KL=27.6, MI=0.001, |Ψ|=1.380 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 984: F=5.147, KL=27.6, MI=0.000, |Ψ|=1.380 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 985: F=5.148, KL=27.6, MI=0.001, |Ψ|=1.380 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 986: F=5.148, KL=27.6, MI=0.000, |Ψ|=1.380 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 987: F=5.148, KL=27.6, MI=0.001, |Ψ|=1.380 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 988: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.380 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 989: F=5.149, KL=27.6, MI=0.000, |Ψ|=1.379 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 990: F=5.149, KL=27.6, MI=0.001, |Ψ|=1.379 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 991: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.379 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 992: F=5.150, KL=27.6, MI=0.000, |Ψ|=1.379 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 993: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.379 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 994: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.379 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 995: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.379 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 996: F=5.152, KL=27.6, MI=0.000, |Ψ|=1.379 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 997: F=5.153, KL=27.6, MI=0.000, |Ψ|=1.378 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 998: F=5.153, KL=27.6, MI=0.000, |Ψ|=1.378 🚨 📉
   🚨 OBSERVER EMERGENCY RESET (KL: 27.6)
Step 999: F=5.153, KL=27.6, MI=0.000, |Ψ|=1.378 🚨 📉

============================================================
📊 OBSERVER-PROTECTED PERFORMANCE ANALYSIS
============================================================
Total steps: 1000
Trauma events: 2
Observer emergency resets: 826
Best Free Energy: 0.000
Final Free Energy: 5.153
Final KL divergence: 27.6
Final Mutual Information: 0.000
Final Controller Dominance: 0.012
Performance evolution: 0.000 → 5.153 (Δ = 5.153)

🔍 OBSERVER HEALTH METRICS:
  KL Divergence: 0.0 → 27.6 (Δ = -27.6)
  Mutual Information: 0.000 → 0.000 (Δ = -0.000)
  Observer emergency resets at: [132, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 311, 313, 315, 317, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 612, 614, 616, 618, 620, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999]

🔧 OBSERVER NEEDS ATTENTION - High KL divergence
💥 Trauma points: [300, 600]

🎉 OBSERVER-PROTECTED simulation completed!
