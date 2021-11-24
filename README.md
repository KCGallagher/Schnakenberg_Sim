# Schnakenberg_Sim

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![BCH compliance](https://bettercodehub.com/edge/badge/KCGallagher/Schnakenberg_Sim?branch=master)](https://bettercodehub.com/)


This package generates a basic Turing Pattern model using the Schnakenberg System [[1](#references)], as part of a group project for the SABS DTC Mathematical Biology Course.

## Schnakenberg System

We consider a trimolecular reaction that may display limit cycle behaviour:

_2A + B ⇌ 3A_  
_A ⇌ M_  
_N → B_  

M and N are in sufficient excess that their concentration is effectively constant. We may consider these reactions to be equivalent to standard formation and decay reactions: 

_2A + B → 3A, ∅ → A, A → ∅, ∅ → B_

Which occur with respective rates _k1, k2, k3, k4_.

This can be represented by the non-dimensional system of ODEs:

<img src="https://render.githubusercontent.com/render/math?math=\frac{da}{dt} = \mu \+ \kappa a(t)^{2}b(t) - \alpha a(t)">
<img src="https://render.githubusercontent.com/render/math?math=\frac{db}{dt} = \beta - \kappa a(t)^{2}b(t) ">


| Parameter     | Description                                                                             | Unit |
| ------------- | --------------------------------------------------------------------------------------- | ---- |
| μ             | Birth rate of A molcules | 1/t  |    
| β             | Birth rate of B molecules   | 1/t  |
| κ             | Rate of _2A + B ⇌ 3A_  reaction     | 1/t  |
| α         | Death rate of A molcules    | 1/t  |

β > 0 controls the rate of tranmission, κ > 0 the rate at which exposed individuals become infectious, and γ > 0 the rate at which individuals recover. The model also requires initial conditions for each compartment: S(0), E(0), I(0), and R(0), which represent the initial number of people in each category.


This autocatalytic system is similar to a _'[Brusselator](https://en.wikipedia.org/wiki/Brusselator)'_, in which _B_ is instead formed from _A_ (at some rate _kA_ ).

## Code Structure

Running files have _'main'_ in the file name (such as `ode_main.py`), and can be used to run simulations of the system, based on functions defined in the other files. The functionality of each of these files is as follows:

* `ode_main.py` - Solve time-dependant ODE model with no spatial dependance

Further scripts are provided as Jupyter Notebooks (`.ipynb`) in the `Examples/` directory, and used to generate all figures in the `Images/` directory.

## References

[1] Schnakenberg, J. (1979). Simple chemical reaction systems with limit cycle behaviour. In Journal of Theoretical Biology (Vol. 81, Issue 3, pp. 389–400). Elsevier BV. https://doi.org/10.1016/0022-5193(79)90042-0
