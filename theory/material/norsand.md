# NorSand

An example input JSON is given as follow for 2D bonded model. Note that `tolerance` is an optional parameter.

```
  "materials": [
    {
      "id" : 0,
      "type" : "NorSand3D",
      "density" : 2000,
      "poisson_ratio" : 0.17,
      "reference_pressure" : 1.0E+5,
      "friction_cs" : 27.0,
      "N" : 0.3,
      "lambda" : 0.3,
      "kappa" : 0.08,
      "gamma" : 1.0,
      "chi" : 3.5,
      "hardening_modulus": 200,
      "void_ratio_initial" : 0.38,
      "p_image_initial" : 3000000,
      "bond_model" : true,
      "p_cohesion_initial" : 1.2E+4,
      "p_dilation_initial" : 2.0E+4,
      "m_cohesion" : 10,
      "m_dilation" : 1,
      "m_modulus" : 100,
      "tolerance" : 1.0E-15    
    }
  ]
```

For traditional NorSand (Jefferies, 1993), `bond_model` is set to be `false`. The code could also take a simpler and reduced input such as follow. Note that `tolerance` is also optional along with the other six variables.

```
  "materials": [
    {
      "id" : 1,
      "type" : "NorSand3D",
      "density" : 2000,
      "poisson_ratio" : 0.17,
      "reference_pressure" : 1.0E+5,
      "friction_cs" : 27.0,
      "N" : 0.3,
      "lambda" : 0.3,
      "kappa" : 0.08,
      "gamma" : 1.0,
      "chi" : 3.5,
      "hardening_modulus": 200,
      "void_ratio_initial" : 0.38,
      "p_image_initial" : 3000000
    }
  ]
```

## References

[1] Jefferies, M. G. (1993). Nor-Sand: a simle critical state model for sand. Géotechnique, 43(1), 91-103.
