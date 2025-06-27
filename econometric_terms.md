# econometric_terms.md

## Basic Concepts

```
Endogeneity              # When explanatory variable correlates with error term
Exogeneity               # When explanatory variable is uncorrelated with error term
Heteroskedasticity       # Non-constant variance of error terms
Homoskedasticity         # Constant variance of error terms
Autocorrelation          # Correlation between error terms across time
Multicollinearity        # High correlation between explanatory variables
```

## Estimation Methods

```
OLS                      # Ordinary Least Squares
2SLS                     # Two-Stage Least Squares
IV                       # Instrumental Variables
GMM                      # Generalized Method of Moments
MLE                      # Maximum Likelihood Estimation
FGLS                     # Feasible Generalized Least Squares
```

## Time Series Concepts

```
Stationarity             # Constant mean and variance over time
Unit Root                # Series has a stochastic trend
Cointegration            # Long-run equilibrium relationship
ARIMA                    # AutoRegressive Integrated Moving Average
VAR                      # Vector Autoregression
VECM                     # Vector Error Correction Model
GARCH                    # Generalized Autoregressive Conditional Heteroskedasticity
```

## Panel Data Terms

```
Fixed Effects            # Control for unobserved heterogeneity
Random Effects           # Assume individual effects are random
Difference-in-Differences # Causal inference method
Hausman Test             # Test for fixed vs random effects
Within Estimator         # Fixed effects estimator
Between Estimator        # Cross-sectional variation
```

## Statistical Tests

```
Durbin-Watson            # Test for autocorrelation
Breusch-Pagan            # Test for heteroskedasticity
White Test               # Test for heteroskedasticity
Jarque-Bera              # Test for normality
ADF Test                 # Augmented Dickey-Fuller (unit root test)
Granger Causality        # Test for causality in time series
```

## Model Selection

```
AIC                      # Akaike Information Criterion
BIC                      # Bayesian Information Criterion
R-squared                # Coefficient of determination
Adjusted R-squared       # Penalized R-squared
F-test                   # Joint significance test
t-test                   # Individual coefficient significance
```

## Splines & Nonparametric Methods

```
B-splines                # Basis splines for smooth curve fitting
Cubic Splines            # Piecewise cubic polynomials with smoothness constraints
Natural Splines          # Cubic splines with linear tails
Smoothing Splines        # Minimize penalized sum of squares
Regression Splines       # Piecewise polynomials for flexible regression
Knots                    # Points where spline pieces connect
Degrees of Freedom       # Number of parameters in spline model
Penalized Splines        # Splines with roughness penalty
Thin Plate Splines       # Multidimensional smoothing splines
GAM                      # Generalized Additive Models
LOWESS                   # Locally Weighted Scatterplot Smoothing
Kernel Regression        # Nonparametric regression using kernels
```