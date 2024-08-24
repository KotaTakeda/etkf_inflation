# ETKF & Inflation
Codes to generate the numerical results in the paper [1].

[1] K. Takeda and T. Sakajo, Uniform error bounds of the ensemble transform Kalman filter for chaotic dynamics with multiplicative covariance inflation, submitted 2024.

## Requirements
```
pip install ./da_py
pip install -r requirements.txt
```

## Example (`l96_etkf.ipynb`)
### Setting
- Lorenz96
  - J = 40
  - F = 8
- Simulate
  - scheme = RK4
  - dt = 0.01
  - N = 20 * 360 * 2
- Observation (full observation)
  - r = sqrt(0.1)
  - H = I_40
  - R = r**2 * I_40
  - obs_per = 5
  - burn_in = N/2
- Assimilate by ETKF
    - m = 41
    - alpha = 1.0, 1.1, 5.0
 
