# NorSand

An example input JSON is given as follow for 2D bonded model. Note that `tolerance` is an optional parameter.

```
  "materials": [
    {
      "id" : 0,
      "type" : "NorSand2D",
      "density" : 2000,
      "poisson_ratio" : 0.17,
      "reference_pressure" : 1.0E+5,
      "friction_cs" : 27.0,
      "N" : 0.3,
      "lambda" : 0.11,
      "kappa" : 0.008,
      "gamma" : 1.0,
      "chi" : 3.5,
      "hardening_modulus": 600,
      "void_ratio_initial" : 0.38,
      "p_image_initial" : 3000000,
      "bond_model" : true,
      "p_cohesion_initial" : 1.2E+7,
      "p_dilation_initial" : 1.2E+7,
      "m_cohesion" : 10,
      "m_dilation" : 1,
      "m_modulus" : 100,
      "tolerance" : 1.0E-15    
    }
  ]
```
