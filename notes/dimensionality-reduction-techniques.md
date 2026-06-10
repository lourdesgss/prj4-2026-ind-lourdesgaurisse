# Dimensionality Reduction Techniques

The selection of an appropriate dimensionality reduction method depends on several characteristics of the dataset, the modelling objective, and the intended use of the transformed representation.

## Data Characteristics

The nature of the feature representation influences which techniques are suitable. Relevant considerations include whether the input consists of raw time-series measurements, frequency-domain representations, hand-crafted statistical features, or a combination of these. Feature type is also important, particularly whether variables are continuous, categorical, sparse, or dense.

The distribution of feature values may affect method selection. Some algorithms assume non-negative inputs, while others can accommodate signed values. An estimate of the dataset's intrinsic dimensionality can also be useful for determining how much compression is realistically achievable without significant information loss.

When available, existing labels, classes, or known groupings may provide additional guidance by allowing supervised evaluation of reduced representations.

## Modelling Objectives

Dimensionality reduction may serve different purposes, including:

* Data visualisation
* Noise reduction and signal extraction
* Feature compression for predictive modelling

The intended objective affects the choice of technique. For predictive modelling, it is important to consider whether the reduced features must remain interpretable and whether they should be traceable back to the original variables.

Another consideration is whether the learned transformation must be applied to unseen data during inference. Some methods naturally support out-of-sample transformation, while others are primarily intended for exploratory analysis and cannot easily generalise to new observations.

## Noise and Variability

Understanding the relationship between signal and noise is often critical. Important questions include whether measurement noise is expected to be random or structured, whether process variability can be distinguished from noise, and whether correlations exist between different features or channels.

The availability of clean reference data or controlled conditions may provide opportunities to validate whether a dimensionality reduction method successfully separates meaningful variation from unwanted noise.

## Computational Constraints

Practical considerations include available computational resources, acceptable training and inference times, and dataset size. Some methods can be trained on representative subsets and then applied to larger datasets, while others require access to the full data distribution during fitting.

Hardware availability, including access to GPUs or distributed computing resources, may also influence the feasibility of more computationally intensive approaches.

## Evaluation Criteria

The effectiveness of a dimensionality reduction technique should be assessed using objective criteria aligned with the intended application. Common evaluation approaches include:

* Reconstruction error
* Preservation of variance
* Downstream predictive model performance
* Cluster separation in reduced space
* Noise variance reduction

Where labels are available, performance can be validated on a held-out test set. Additional qualitative or domain-specific sanity checks may also be useful to determine whether meaningful patterns remain visible after transformation.

