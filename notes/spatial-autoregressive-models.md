# Spatial Autoregressive Models

This document summarises modelling approaches that can encode spatial or structural dependencies between units, motivated by the observation that `HeadIdx#` in the waveform dataset represents a physically ordered sequence of chips on a printhead, with adjacent chips sharing similar behaviour and data availability patterns.

## Motivation

A conventional regression or tree model treats each chip index as an independent observation. This ignores the fact that chips close together on the printhead are likely to have correlated outputs — due to shared manufacturing tolerances, ink flow dynamics, or thermal gradients. Ignoring this structure means the model will fail to capture a systematic source of variation, and predictions for underrepresented chips (e.g. 5–12) will rely solely on the global signal rather than local neighbourhood context.
## Approach 1 — Spatial Lag Model (SAR)

The **Spatial Autoregressive (SAR)** model extends a standard linear model by adding a spatially lagged version of the dependent variable as a regressor:

```
y = ρ W y + X β + ε
```

where `W` is a **spatial weights matrix** encoding which units are "neighbours" (e.g. adjacent chips), and `ρ` is the spatial autocorrelation coefficient. If `ρ` is significantly non-zero, the output of a chip is partly explained by the outputs of its neighbours.

> Anselin, L. (1988). _Spatial Econometrics: Methods and Models_. Kluwer Academic Publishers. LeSage, J. & Pace, R. K. (2009). _Introduction to Spatial Econometrics_. CRC Press / Chapman & Hall.

---

## Approach 2 — Conditional Autoregressive Model (CAR)

The **CAR model** is a Bayesian alternative that specifies the conditional distribution of each unit given its neighbours, rather than modelling the joint distribution directly:

```
y_i | y_{-i} ~ N( μ_i + Σ_j w_ij (y_j - μ_j), σ²_i )
```

CAR models are widely used in spatial statistics when the neighbourhood structure is irregular or when uncertainty quantification is important. They are computationally tractable via MCMC or variational inference.

A CAR prior placed on chip-level random effects would allow the model to borrow strength from neighbouring chips when estimating the output of a chip with sparse observations (e.g. chips 5–12 with missing waveform configs).

> Besag, J. (1974). Spatial interaction and the statistical analysis of lattice systems. _Journal of the Royal Statistical Society: Series B_, 36(2), 192–225. Banerjee, S., Carlin, B. P., & Gelfand, A. E. (2004). _Hierarchical Modeling and Analysis for Spatial Data_. Chapman & Hall/CRC.

---

## Approach 3 — Graph Neural Networks (GNNs)

For a more flexible, non-linear approach, a **Graph Neural Network** can encode the chip topology directly as a graph, where each chip is a node and edges connect neighbours. At each layer, a chip's representation is updated by aggregating information from its neighbours:

```
h_i^(l+1) = σ( W^(l) · AGG({ h_j^(l) : j ∈ N(i) }) )
```

GNNs can learn complex, non-linear spatial dependencies and scale to cases where the neighbourhood structure is not strictly linear.

**Applicability here:** Represent each chip as a node with features `[waveform_id, dt2, Coverage#, Color$]`, connect adjacent chips with edges, and predict the waveform output vector at each node. A GraphSAGE or GCN architecture would be a reasonable starting point.

> Kipf, T. N. & Welling, M. (2017). Semi-supervised classification with graph convolutional networks. _ICLR 2017_. [arXiv:1609.02907](https://arxiv.org/abs/1609.02907) Hamilton, W., Ying, R., & Leskovec, J. (2017). Inductive representation learning on large graphs. _NeurIPS 2017_. [arXiv:1706.02216](https://arxiv.org/abs/1706.02216)

---

## Comparison

|Approach|Linearity|Uncertainty|Interpretability|Complexity|
|---|---|---|---|---|
|SAR|Linear|Frequentist|High|Low|
|CAR|Linear|Bayesian|High|Medium|
|GNN|Non-linear|None (by default)|Low|High|

---

## Next Steps

Given the dataset structure, the first step is to add a **spatial lag feature**: for each row, compute the mean waveform output of the two neighbouring chips at the same operating point, and include it as an additional input to a tree-based model.