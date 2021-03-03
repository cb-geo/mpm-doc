# Linear Elastic

The linear elastic model is the simpliest model for homogeneous isotropic materials. Relevant equations are presented briefly below.

## Elastic Modulus

The bulk, shear, and constrained moduli ($K$, $G$, and $M$, respectively) are defined as follows, 

$$ K = \frac{E}{3 (1 - 2\nu)}, $$

$$ G = \frac{E}{2(1 + \nu)}, $$

$$ M =  , $$

where $E$ is the Young's modulus and $\nu$ is the Poisson's ratio.

## Wave Velocities

The shear and pressue wave velocities ($v_s$ and $v_p$, respectively) are defined [1] as follows,

$$ v_s = , $$

$$ v_p = , $$

where $\rho$ is the density.

## Input Parameters

An example input JSON is provided for a 2D linear elastic model.

```
  "materials": [
    {
      "id" : 0,
      "type" : "LinearElastic2D",
      "density" : 2000,
      "youngs_modulus" : 10000000.0,
      "poisson_ratio" : 0.3
    }
  ]
```
  * "id" is the material ID, used for multiple material models in a simulation
  * "type" is the material type ("LinearElastic2D" for 2D plain strain condition, "LinearElastic3D" for 3D),
  * "density" is the density of the material,
  * "youngs_modulus" is the constant elastic parameter Young's modulus $E$,
  * "poisson_ratio" is the constant elastic parameter Poisson's ratio $\nu$.


## References

[1] Last Name, F. M. initials (YEAR). Title. Journal, volume, pages.