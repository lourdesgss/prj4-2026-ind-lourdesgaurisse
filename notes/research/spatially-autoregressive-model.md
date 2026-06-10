# Spatial Autoregressive Model

[Source](https://www.geeksforgeeks.org/data-science/spatial-autoregressive-model-an-overview/)

Spatial Autoregressive (SAR) models solve the need for spatially-aware statistical models. Traditional regression models assume that each observation is independent of others, which is rarely the case in spatial data. These models take spatial dependency into account for the modeling process, making them powerful tools for analyzing data where location matters.

A Spatial Autoregressive Model is a type of spatial regression model designed to account for spatial autocorrelation, the tendency for observations that are geographically close to exhibit similar values. In simpler terms, the SAR model allows the value of a variable at one location to depend on values of that variable at nearby locations.

Mathematically, the classic SAR model is defined as:

$$y = \rho W y + X \beta + \varepsilon$$

Where:

- $y$ : Dependent variable vector.
- $X$ : Matrix of independent variables.
- $\beta$ : Coefficients for the predictors.
- $\rho$ : Spatial autoregressive parameter.
- $W$ : Spatial weights matrix (defines the neighborhood structure).
- $\varepsilon$ : Random error term.

The key term here is $Wy$, which introduces spatial lag by capturing how the dependent variable at neighboring locations influences the current location. If spatial autocorrelation is present and not accounted for, In these cases standard regression models may yield biased or inefficient estimates.

## Understanding the Spatial Weights Matrix

At the core of SAR models we have the spatial weights matrix $W$. This matrix encodes the spatial structure, which means observations are considered neighbors and how strongly they are related.

Common forms of spatial weights include:

- Binary contiguity: $w_{ij}$ = 1 if regions i and j share a border, 0 otherwise.
- Inverse distance: Nearby observations get higher weights.
- Row-standardized weights: Each row sums to 1, which helps with model stability and interpretation.

The choice of  $W$ significantly impacts the behavior of the SAR model. In practice, spatial analysts often experiment with different forms of $W$ based on the underlying spatial process.

## Estimation Techniques

Estimating SAR models poses challenges due to the spatial lag term $Wy$, which makes things ambiguous. The presence of the dependent variable on both sides of the equation rules out simple OLS estimation.

Common estimation methods include:

- Maximum Likelihood Estimation (MLE): This method involves maximizing a log-likelihood function that accounts for spatial structure. Computationally expensive but accurate.
- Generalized Method of Moments (GMM): Useful for large datasets or when the likelihood is difficult to specify. Less efficient than MLE but more flexible.
- Bayesian Estimation: Uses prior distributions for parameters and Markov Chain Monte Carlo (MCMC) to estimate the posterior. Provides uncertainty quantification naturally.

# Independent Research

## Approach 1 — Spatial Lag Model (SAR)

The **Spatial Autoregressive (SAR)** model extends a standard linear model by adding a spatially lagged version of the dependent variable as a regressor:

$$y = \rho W y + X \beta + \varepsilon$$

where $W$ is a **spatial weights matrix** encoding which units are "neighbours" (e.g. adjacent chips), and $\rho$ is the spatial autocorrelation coefficient. If $\rho$ is significantly non-zero, the output of a chip is partly explained by the outputs of its neighbours.

> Anselin, L. (1988). *Spatial Econometrics: Methods and Models*. Kluwer Academic Publishers. LeSage, J. & Pace, R. K. (2009). *Introduction to Spatial Econometrics*. CRC Press / Chapman & Hall.

---

## Approach 2 — Conditional Autoregressive Model (CAR)

The **CAR model** is a Bayesian alternative that specifies the conditional distribution of each unit given its neighbours, rather than modelling the joint distribution directly:

$$y_i | y_{-i} \sim N( \mu_i + \Sigma_j w_{ij} (y_j - \mu_j), \sigma^2_i )$$

CAR models are widely used in spatial statistics when the neighbourhood structure is irregular or when uncertainty quantification is important. They are computationally tractable via MCMC or variational inference.

A CAR prior placed on chip-level random effects would allow the model to borrow strength from neighbouring chips when estimating the output of a chip with sparse observations (e.g. chips 5–12 with missing waveform configs).

> Besag, J. (1974). Spatial interaction and the statistical analysis of lattice systems. *Journal of the Royal Statistical Society: Series B*, 36(2), 192–225. Banerjee, S., Carlin, B. P., & Gelfand, A. E. (2004). *Hierarchical Modeling and Analysis for Spatial Data*. Chapman & Hall/CRC.

---

## Approach 3 — Graph Neural Networks (GNNs)

For a more flexible, non-linear approach, a **Graph Neural Network** can encode the chip topology directly as a graph, where each chip is a node and edges connect neighbours. At each layer, a chip's representation is updated by aggregating information from its neighbours:

$$h_i^{(l+1)} = \sigma( W^{(l)} \cdot \text{AGG}(\{ h_j^{(l)} : j \in \mathcal{N}(i) \}) )$$

GNNs can learn complex, non-linear spatial dependencies and scale to cases where the neighbourhood structure is not strictly linear.

**Applicability here:** Represent each chip as a node with features `[waveform_id, dt2, Coverage#, Color$]`, connect adjacent chips with edges, and predict the waveform output vector at each node. A GraphSAGE or GCN architecture would be a reasonable starting point.

> Kipf, T. N. & Welling, M. (2017). Semi-supervised classification with graph convolutional networks. *ICLR 2017*. [arXiv:1609.02907](https://arxiv.org/abs/1609.02907) Hamilton, W., Ying, R., & Leskovec, J. (2017). Inductive representation learning on large graphs. *NeurIPS 2017*. [arXiv:1706.02216](https://arxiv.org/abs/1706.02216)

---

## Comparison

|Approach|Linearity|Uncertainty|Interpretability|Complexity|
|---|---|---|---|---|
|SAR|Linear|Frequentist|High|Low|
|CAR|Linear|Bayesian|High|Medium|
|GNN|Non-linear|None (by default)|Low|High|