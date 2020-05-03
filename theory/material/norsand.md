# NorSand

The bonded NorSand model is an extension of the original critical state based constitutive model NorSand by Jefferies (1993). Relevant equations are presented briefly on this document.

## Yield Function

$$ F = \frac{q}{p+p_c} - \frac{M_\theta}{N}\left[1 + (N-1)\left(\frac{p + p_c}{p_i + p_c + p_d}\right)^\frac{N}{1-N}\right] $$

$$M(\theta) = M_{tc} - \frac{M_{tc}^2}{3 + M_{tc}}cos(\frac{3\theta}{2})$$

where $p$ is the mean pressure, $q$ is the magnitude of deviatoric stress, $\theta$ is the Lode's angle (with cosine convention), $M$ is the slope of the critical line, $M_{tc}$ is the value of $M$ under trial extension status. Furthermore, $p_c$ and $p_d$ are cohesive and dilative pressure terms to describe the bond. They are defined as:

$$ p_c = p_{c0} \exp{(-m_c \varepsilon^p_d)} $$

$$ p_d = p_{d0} \exp{(-m_d \varepsilon^p_d)} $$

where $p_{c0}$ is the initial cohesive pressure term, $p_{d0}$ is the initial dilative pressure term, $m_c$ is cohesive degradation term and $m_d$ is dilative degradation term. Lastly, $\varepsilon^p_d$ is the equivalent plastic deviatoric strain. 

## Flow Rule

An assosiated potential flow rules is defined, which means it has the same format with the yield function.

## Elastic Modulus

The bulk and shear modulus are defined as follow, with an assumption of constant Poisson's ratio $\nu$.

$$ K = \frac{1 + e}{\kappa}p + m_M (p_c + p_d) $$

$$ G = \frac{3K(1 - 2\nu)}{2(1+\nu)} $$

where $e$ is the void ratio, $\kappa$ is the swell/recompression index,, $K$ is the volumetric modulus, and finally $G$ is the shear modulus.


## Input Parameters

An example input JSON is given as follow for 3D bonded model. Note that `tolerance` is an optional parameter.

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
  * "id" is the material ID, used for multiple material models in a simulation
  * "type" is the material type ("NorSand2D" for 2D plain strain condition, "NorSand3D" for 3D), 
  * "density" is the density of the material,
  * "poisson_ratio" is the constant elastic parameter Poisson's ratio $\nu$,
  * "reference_pressure" is set at atmospheric pressure of 100 kPa,
  * "friction_cs" is the critical state friction angle used to compute $M$,
  * "lambda" is the virgin compression index $\lambda$,
  * "kappa" is the swell/recompression index $\kappa$,
  * "gamma" is the void ratio based on the reference atmospheric pressure,
  * "chi" is the dilatancy coefficient $\chi$,
  * "hardening_modulus" is hardening modulus $H$,
  * "void_ratio_initial" is the initial void ratio $e_0$,
  * "p_image_initial" is the initial $p_image$, the intersection between the yield surface and critical state line,
  * "bond_model" is the bonded behavior boolean option (true or false),
  * "p_cohesion_initial" is the initial cohesive pressure term $p_{c0}$ to describe the bond,
  * "p_dilation_initial" is the initial dilation pressure term $p_{d0}$ to describe the bond,
  * "m_cohesion" is the cohesive degradation term $m_c$,
  * "m_dilation" is the dilative degradation term $m_d$,
  * "m_modulus" is bonded modulus effects of the cohesion and dilation $m_M$,
  * "tolerance" is an optional tolerance value for computations such as yield condition, set default as machine epsilon.

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
