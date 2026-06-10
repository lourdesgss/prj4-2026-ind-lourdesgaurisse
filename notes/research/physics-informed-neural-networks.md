# Physics Informed Neural Networks

[Source](https://en.wikipedia.org/wiki/Physics-informed_neural_networks)

## Relevant Sections

In machine learning, physics-informed neural networks (PINNs), also referred to as theory-trained neural networks (TTNs), are a type of universal function approximator that can embed the knowledge of any physical laws that govern a given data-set in the learning process, and can be described by partial differential equations (PDEs)

---

In general, deep neural networks could approximate any high-dimensional function given that sufficient training data are supplied. However, such networks do not consider the physical characteristics underlying the problem, and the level of approximation accuracy provided by them is still heavily dependent on careful specifications of the problem geometry as well as the initial and boundary conditions. Without this preliminary information, the solution is not unique and may lose physical correctness.

To remedy this, Physics-Informed Neural Networks (PINNs) leverage governing physical equations in neural network training. Namely, PINNs are designed to be trained to satisfy the given training data as well as the imposed governing equations. In this fashion, a neural network can be guided with training datasets that do not necessarily need to be large or complete. An accurate solution of partial differential equations can potentially be found without knowing the boundary conditions. Therefore, with some knowledge about the physical characteristics of the problem and some form of training data (even sparse and incomplete), PINNs may be used for finding an optimal solution with high fidelity.

### For inverse computations

Physics-informed neural networks (PINNs) have proven particularly effective in solving inverse problems within differential equations, demonstrating their applicability across science, engineering, and economics. They have shown to be useful for solving inverse problems in a variety of fields, including nano-optics, topology optimisation/characterisation, multiphase flow in porous media, and high-speed fluid flow.

PINNs have demonstrated flexibility when dealing with noisy and uncertain observation datasets. They also demonstrated clear advantages in the inverse calculation of parameters for multi-fidelity datasets, meaning datasets with different quality, quantity, and types of observations. Uncertainties in calculations can be evaluated using ensemble-based or Bayesian-based calculations.

PINNs can also be used in connection with symbolic regression for discovering the mathematical expression in connection with discovery of parameters and functions.