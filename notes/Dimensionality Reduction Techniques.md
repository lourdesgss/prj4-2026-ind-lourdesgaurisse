# Selecting an approach for dimensionality reduction backed up by Facts and Logic

Pre-decision information checklist:
- What is the raw feature representation going into the reduction? (Time-series waveform samples, frequency bins, hand-crafted statistics, or some combination?)
	- Time-series waveform samples
- Are all features dense and continuous, or do you have sparse or categorical features mixed in?
	- Dense & continuous (in theory) features
- Are feature values non-negative (magnitudes, power spectra) or signed?
	- Non-signed
- What is the intrinsic dimensionality estimate? (Even rough: PCA explained variance curve, or nearest-neighbour distance distributions)
	- IDK
- Do you have known labels or groupings on a subset? (Waveform categories, known-good vs. defective prints, colour outcome buckets)
	- Nope

**About the goal**
- Is dimensionality reduction primarily for visualisation, for noise filtering, or as a preprocessing step before a predictive model?
	- Predictive model
- Do you need the reduced dimensions to be interpretable and mappable back to original features?
	- Yes
- Is the downstream model sensitive to linearity assumptions, or is it a black-box that can handle any latent space?
	- 
- Do you need to apply the learned reduction to new, unseen data at inference time? (Rules out t-SNE; favours PCA, autoencoders, UMAP with `transform`)

**About your noise separation problem specifically**
- Do you have a hypothesis about the structure of measurement noise versus process variability? (e.g., additive Gaussian noise → ICA or PCA; structured periodic artefacts → frequency-domain methods first)
- Can you produce a "clean reference" subset or known-noise conditions for validation?
- Is noise independent across channels/features, or correlated?

**About scale and infrastructure**
- What is your compute environment? (Single machine, cluster, GPU availability)
- What is the acceptable runtime for an offline fitting step vs. an online transform?
- Can you fit on a random sample and apply the transform to the full dataset, or does the full distribution matter for fitting?

**About evaluation**
- How will you judge that the reduction worked? (Reconstruction error, downstream model performance, visual cluster separation, noise variance explained)
- Do you have a held-out labelled test set for downstream model evaluation?
- Is there a human-interpretable sanity check you can run? (e.g., known waveform defects appearing as outliers in the reduced space)