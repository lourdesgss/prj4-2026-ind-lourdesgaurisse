# Spatial Interactions in Discrete Physical Systems

[Source](https://sites.math.duke.edu/~rtd/reprints/paper82.pdf)

## Relevant Sections

Interacting Particle Systems. Our second approach assumes that the patches can be identified with the set of lattice points $S = \mathbb{Z}^2$, the points in two-dimensional space with integer coordinates. Following Brown and Hansell (1987), the dynamics are formulated as follows:

(i) **Migration**. Each individual changes its spatial location at rate $f$ and when it moves it moves to a randomly chosen nearest neighbor of $x$; i.e., it picks with equal probability one of the four points $x + (1,0)$, $x - (1,0)$, $x + (0, 1)$, and $x - (0, 1)$ that differ from $x$ by $1$ in one of the coordinates.

(ii) **Deaths due to crowding**. Each individual at $x$ at time $t$ dies at rate $k(n_t(x) + s_t(x))$.

(iii) **Game step**. Let $N$ be the interaction neighborhood for the model. In this paper we consider two choices for $N$:

- $N_1 = \{(0, 0)\text{ and its nearest neighbors}\}$
- $N_2 = \{(z_1, z_2) \in \mathbb{Z}^2 : |z_1| \leq 2, |z_2| \leq 2\}$ (a $5 \times 5$ square centered at $(0, 0)$).

For any choice of $N$ we let

$$n_t(x) = \sum_{z \in N} \text{(number of hawks at } x+z \text{ at time } t\text{)}$$

$$s_t(x) = \sum_{z \in N} \text{(number of doves at } x+z \text{ at time } t\text{)}$$

$$p_t(x) = n_t(x) / (n_t(x) + s_t(x)).$$

Here $n_t(x)$ and $s_t(x)$ are the number of hawks and doves in the interaction neighborhood of $x$ at time $t$, and $p_t(x)$ is the fraction of hawks. Each hawk experiences a birth (or death) rate of $a p_t(x) + b(1 - p_t(x))$ while each dove experiences a birth (or death) rate of $c p_t(x) + d(1 - p_t(x))$. The phrase "birth (or death)" means that these numbers are interpreted as birth rates if they are positive and death rates if they are negative.

The choice of the nearest neighborhood $N_1$ for the migration and the game steps is primarily for simplicity. In most cases the qualitative features of the model do not depend upon the exact form of the neighborhood chosen. (However, see the analysis of Case 3 below.) We could make the interacting particle system model look more like the patch model by making the game step involve only individuals in the same patch but this would not affect the results very much.

### Clarifying Note

While the mathematical depth of this paper exceeds my current level of comprehension, examining the topic within an academic context provided insights that contributed to the development of my function.
