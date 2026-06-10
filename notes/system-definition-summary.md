# System Definition Summary

## Physical Structure of the System

The system consists of four colour channels, each containing 30 chips. Every chip contains 1120 nozzles, giving a total of $30 \times 1120 = 33600$ nozzles per colour.

Let the nozzle index be defined as $j \in {1,\ldots,33600}$. The domain is therefore a discrete ordered spatial index rather than a continuous coordinate system.

---

## Experimental Configuration

Each experiment corresponds to a full configuration of the system across multiple parameter scales.

The relevant variables are structured hierarchically:

* global parameters (e.g. coverage),
* chip-level parameters (e.g. voltage $V$, flank ratio $Fr$),
* nozzle-level parameters (e.g. $dt2$).

A configuration at experiment $m$ is written as
$\Theta^{(m)} = (\text{colour}, V, Fr, dt2, \text{coverage})$.

The full design yields approximately $M = 3600$ experiments.

---

## Hierarchical Data Representation

For each experiment, the input is a spatially structured field rather than a flat vector.

The process variables can be represented as
$U^{(m)} \in \mathbb{R}^{33600 \times p}$,
where each nozzle carries multiple features including inherited chip-level quantities and nozzle-specific parameters.

Global variables are represented separately as
$\theta^{(m)} \in \mathbb{R}^{q}$.

The observed output is a spatial response field
$Y^{(m)} \in \mathbb{R}^{33600}$.

The learning problem is therefore the mapping
$(U^{(m)}, \theta^{(m)}) \mapsto Y^{(m)}$.

---

## Chip-Level Partitioning

The nozzle space is explicitly partitioned into chips via a mapping
$h(j): {1,\ldots,33600} \rightarrow {1,\ldots,30}$.

Each chip contains 1120 nozzles, and chip-level variables are constant within each partition.

This implies the spatial domain is piecewise structured rather than homogeneous, with discontinuities induced by chip boundaries.

---

## Continuous Field Interpretation

A common modelling step is to introduce continuous approximations $U(x)$ and $Y(x)$, where $x$ denotes a spatial coordinate.

This does not correspond to a physical continuum but to an assumption that discrete measurements arise from an underlying smooth latent function.

This assumption enables the use of kernels, convolutions, and differential operators, effectively imposing smoothness as an inductive bias rather than encoding true physical continuity.

---

## Limitations of Continuity

Purely continuous representations tend to obscure structural discontinuities inherent in the system.

Issues include loss of explicit chip boundaries, oversmoothing across discontinuities, and reduced fidelity to the discrete architecture.

Continuity is therefore a modelling choice rather than a physical requirement.

---

## Interaction Structure

Pairwise interactions across nozzles can be expressed via a coupling matrix $C_{jk}$.

However, directly learning $C_{jk}$ is not tractable due to dimensionality.

Practical alternatives impose structure through locality or hierarchy, such as distance-based kernels, neighbourhood graphs, or chip-level grouping.

Thus, interaction structure is better understood as a constrained function of spatial proximity and chip identity rather than a free parameter matrix.

---

## Noise Modelling

A standard assumption is
$Y = f(U,\theta) + \varepsilon$, where $\varepsilon \sim \mathcal{N}(0,\sigma^2)$.

This independence assumption is unlikely to hold in this system.

Noise is expected to be spatially correlated, chip-dependent, and potentially parameter-dependent.

A more general formulation is therefore
$Y \sim p(Y \mid U,\theta)$, treating variability as a conditional distribution rather than independent additive noise.

In practice, what is often labelled as “noise” may contain structured but unmodelled system behaviour.

---

## Hierarchical Modelling View

The system can be decomposed into four interacting levels:

1. global configuration $\theta$
2. chip assignment $h(j)$
3. spatial input field $U_j$
4. spatial output field $Y_j$

The full mapping is
$(\theta, U) \rightarrow Y$ over a structured discrete spatial domain.

---

## Hybrid Continuous–Discrete Representation

If a continuous formulation is used, it should explicitly preserve known discrete structure.

A suitable kernel decomposition is

$k(x,x') = k_{\text{local}}(|x-x'|) + k_{\text{chip}}(h(x), h(x'))$.

This combines local smoothness assumptions with explicit chip-level structure, allowing continuity within regions while preserving discontinuities at known boundaries.
