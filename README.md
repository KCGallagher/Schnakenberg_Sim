# Schnakenberg_Sim

This package generates a basic Turing Pattern model using the Schnakenberg System [[1](#references)], as part of a group project for the SABS DTC Mathematical Biology Course.

## Schnakenberg System

We consider a trimolecular reaction that may display limit cycle behaviour:

_2X + Y ⇌ 3X_  
_X ⇌ A_  
_B → Y_  

A and B are in sufficient excess that their concentration is effectively constant. We may consider these reactions to be equivalent to standard formation and decay reactions: 

_∅ → A, A → ∅, ∅ → B_

This can be represented by the non-dimensional system of ODEs:

<img src="https://render.githubusercontent.com/render/math?math=\frac{dx}{dt} = x(t)^{2}y(t) - x(t) - b">

<img src="https://render.githubusercontent.com/render/math?math=\frac{dy}{dt} = - x(t)^{2}y(t) - a">

where _a_ and _b_ are both negative.

This autocatalytic system is similar to a _'[Brusselator](https://en.wikipedia.org/wiki/Brusselator)'_, in which _Y_ is instead formed from _X_ (at some rate _cX_ ).

## References

[1] Schnakenberg, J. (1979). Simple chemical reaction systems with limit cycle behaviour. In Journal of Theoretical Biology (Vol. 81, Issue 3, pp. 389–400). Elsevier BV. https://doi.org/10.1016/0022-5193(79)90042-0
