# ETKF & Inflation
Codes to generate the numerical results in the paper [1].

[1]  **Uniform error bounds of the ensemble transform Kalman filter for chaotic dynamics with multiplicative covariance inflation** <br> <u>K. Takeda</u> and T. Sakajo, SIAM/ASA Journal on Uncertainty Quantification, 12(4), 1315-1335. <br> [![DOI](https://img.shields.io/badge/DOI-10.1137/22M1543550-lightblue?labelColor=lightgrey)](https://doi.org/10.1137/24M1637192)

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
 
### Results
![square error](https://github.com/KotaTakeda/etkf_inflation/blob/main/data/l96-etkf-inflation_se.png)
![eigen value](https://github.com/KotaTakeda/etkf_inflation/blob/main/data/l96-etkf-inflation_eval.png)
