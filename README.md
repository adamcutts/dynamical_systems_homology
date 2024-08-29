# <p align="center">An investigation into classification of initial conditions of dynamical systems using persistent homology</p>

### <p align="center">Adam Cutts</p>

---
Many thanks to my supervisor Ximena Fernandez at Oxford's Mathematical Institute for her helpful guidance and feedback throughout this project.

---
## Introduction
A continuous time dynamical system conists of a state space $X$, typically some subset of $`\mathbb{R}^n`$, along with some $C^1$ function $f$. The system then evolves according to the ODE $\dot{x} = f(x)$, where $x\in X$. Such systems can be thought of as a vector field imposed on the state space $X$. 

The long-run dynamics of such systems is of great interest. In practice, one wants to characterise the evolution of a state from some initial state $x_0$. For instance, will that state evolve under the action of $f$ in a periodic manner? Will the state stabilise to some fixed value? Will it blow up in an unbounded way? 

Such questions are trivial to analyse in low dimensions. For instance, if $X$ is 1-dimensional, no periodic orbits can exist; either states stabilise to a fixed point or they blow up to $\pm \infty$. See chapter 2.6 of [^1] for more on this. The situation gets more complicated the higher the dimension of the state space $X$. In these cases, we are no longer interested just in fixed points, but in attractors, that is sets of points towards which nearby states evolve. 

This code explores categorising the long-run dynamics of a dynamical system by exploring the topology of its attractors. Following along the lines of [^2], we investigate the so-called double-gyre system. However, where [^2] explores the BraMAH approach, we instead seek to use the tools of persistent homology [^3].

---
## Setup
The double-gyre system models oscillating jets of water in 2-dimensions. It has the advantage that the domain of definition is invariant in the sense that the vector field always has 0 outward component at the boundary. It is defined on the state space $[0,2]\times [0,1]$, with the following vector field: 
```
markdown test:
  indent test
```
---
## References
[^1]: Steven H. Strogatz. "Nonlinear Dynamics and Chaos", 1994 
[^2]: Charó, Gisela D., Guillermo Artana, and Denisse Sciamarella. "Topology of dynamical reconstructions from Lagrangian data". Physica D: Nonlinear Phenomena 405 (2020): 132371, 2020
[^3]: Gunnar Carlsson. "Topology and Data". American Mathematical Society. S 0273-0979(09)01249-X, 2009
