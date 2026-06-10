28/05/2026
# Formal Definition

$$f : \mathbb{R}^34 \times \mathbb{R}^{33600 \times 3} \to \mathbb{R}^{33600}$$

$$f(\theta, U)_i = s(U_i) + \sum_{j \in \mathcal{N}(i)} W_{ij}(\theta), s(U_j) + \varepsilon_i$$

**Variables:**

| Symbol                               | Meaning                                | Space                             |
| ------------------------------------ | -------------------------------------- | --------------------------------- |
| $\theta$                             | global settings (colour, coverage)     | $\mathbb{R}^34$                    |
| $U$                                  | per-nozzle input field                 | $\mathbb{R}^{33600 \times 3}$     |
| $U_i = (V_{h(i)}, Fr_{h(i)}, dt2_i)$ | input vector for nozzle $i$            | $\mathbb{R}^3$                    |
| $s(U_i)$                             | baseline response of nozzle $i$        | $s : \mathbb{R}^3 \to \mathbb{R}$ |
| $\mathcal{N}(i)$                     | spatial neighbours of nozzle $i$       | to be defined                     |
| $W_{ij}(\theta)$                     | coupling weight from nozzle $j$ to $i$ | to be defined                     |
| $y_i$                                | measured print response at nozzle $i$  | $\mathbb{R}$                      |
| $\varepsilon_i$                      | noise                                  | $\mathbb{R}$                      |

---

## Still to Define

- **Functional form of $s$** — what model maps $U_i \in \mathbb{R}^3$ to a scalar response? (e.g. linear, MLP, GP)
- **Neighbourhood $\mathcal{N}(i)$** — how many neighbours, and by what criterion? (k-nearest, distance threshold, physical adjacency)
- **Functional form of $W_{ij}(\theta)$** — parametric decay, uniform contiguity, or data-driven from residual autocorrelation
- **Whether $W_{ij}$ depends on $\theta$ at all** 
## On Continuity
Domain and codomain
$$f : \mathbb{R}^5 \times (\mathcal{X} \to \mathbb{R}^3) \to (\mathcal{X} \to \mathbb{R})$$
Function:
$$f(\theta, U)(x) = s(U(x)) + \int_{\mathcal{X}} W(x, x', \theta) \, s(U(x')) \, dx' + \varepsilon(x)$$