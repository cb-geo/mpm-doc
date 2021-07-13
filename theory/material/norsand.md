# NorSand

The bonded NorSand model is an extension of the original critical state based constitutive model NorSand by Jefferies (1993) and Jefferies and Been (2016). Relevant equations are presented briefly on this document.

## Summary of NorSand Equations

Relevant equations are presented below with a complete list of symbols provided at the end. 

### Internal Model Parameters

Internal model parameters are used to calculate the critical stress ratio image needed to determine the yield surface. Using the critical stress ratio image represent one of the major updates between Jefferies (1993) and Jeffereies and Been (2016). 

$$ \psi_i = e - e_i $$

$$ \quad e_i = \Gamma - \lambda\ln(p_i/p_{\text{atm}}) $$

$$ \chi_i = \frac{\chi_{tc}}{(1-\chi_{tc}\lambda/M_{tc})} $$

$$ M_i = M_{\theta} \left(1-\frac{\chi_i N |\psi_i|}{M_{tc}}\right) $$

$$ M_{itc} = M_{tc} \left(1-\frac{\chi_i N |\psi_i|}{M_{tc}}\right) $$

### Critical State

The critical stress relies on lode angle, which uses a cosine convention in `CB-Geo`. This form of the critical stress ratio is from Jefferies and Shuttle (2011). 

$$ M_{\theta} = M_{tc}-\frac{M_{tc}^2}{3+M_{tc}}\cos\left(\frac{3\theta}{2}\right) $$

### Yield Surface

The yield surface equation includes a cap which relies on the internal model parametes above. 

$$ F = \frac{q}{p+p_c} - M_i +M_i \ln\left(\frac{p+p_c}{p_i+p_c+p_d}\right), \quad \left(\frac{p_i+p_c+p_d}{p+p_c}\right)_{\text{max}}=\exp\left[\frac{-\chi_i\psi_i}{M_{itc}}\right] $$

### Bonded model

$$ p_c = p_{c0} \exp{(-m_c \varepsilon^p_q)} $$

$$ p_d = p_{d0} \exp{(-m_d \varepsilon^p_q)} $$

### Hardening Rule

$$ \frac{\partial p_i}{\partial\varepsilon_q^p} = H\frac{M_i}{M_{itc}}\left(\frac{p}{p_i}\right)^2\left[\exp\left(\frac{-\chi_i\psi_i}{M_{tc}}\right)-\frac{p_i}{p}\right]p_i $$


### Flow Rule (associated potential flow rule)

$$ P = F $$

### Elasticity

$$ K = \frac{1 + e}{\kappa}p + m_M (p_c + p_d) $$

$$ G = \frac{3K(1 - 2\nu)}{2(1+\nu)} $$


### Symbols
| Symbol              | Name                                             |
| ------------------- | ------------------------------------------------ |
| $e$                 | void ratio                                       |
| $e_i$               | void ratio image                                 |
| $F$                 | yield surface funciton                           |
| $G$                 | shear modulus                                    |
| $H$                 | hardening modulus                                |
| $K$                 | bulk modulus                                     |
| $m_c$               | cohesive degradation                             |
| $m_d$               | dilative degradation                             |
| $m_M$               | bonded modulus                                   |
| $M_{\theta}$        | critical stress ratio                            |
| $M_{i}$             | critical stress ratio image                      |
| $M_{itc}$           | critical stress ratio triaxial compression image |
| $M_{tc}$            | critical stress ratio triaxial compression       |
| $N$                 | volumetric coupling (dilatancy) parameter        |
| $p$                 | mean stress                                      |
| $p_{\text{atm}}$    | atmospheric reference pressure                   |
| $p_c$               | cohesive pressure                                |
| $p_{c0}$            | initial cohesive pressure                        |
| $p_d$               | dilative pressure                                |
| $p_{d0}$            | initial dilative pressure                        |
| $p_i$               | mean stress image                                |
| $P$                 | potential function                               |
| $q$                 | deviatoric stress                                |
| $\Gamma$            | void ratio at reference pressure                 |
| $\varepsilon_q^p$   | plastic deviatoric strain                        |
| $\eta$              | stress ratio                                     |
| $\theta$            | lode angle (cosine convention)                   |
| $\kappa$            | unload/reload slope                              |
| $\lambda$           | normal compression line (NCL) slope              |
| $\nu$               | Poisson's ratio (assumed constant)               |
| $\phi$              | friction angle                                   |
| $\chi_i$            | state-dilatancy image                            |
| $\chi_{tc}$         | state-dilatancy triaxial compression             |
| $\psi$              | state parameter                                  |
| $\psi_i$            | state parameter image                            |


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

For traditional NorSand (Jefferies, 2016), `bond_model` is set to be `false`. The code could also take a simpler and reduced input such as follow. Note that `tolerance` is also optional along with the other six variables.

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
[2] Jefferies, M., Been K. (2016). "Soil liquefaction: a critical state approach." Second Edition. CRC Press.
[3] Jefferies, M., Shuttle, D. (2011). "On the operating critical friction ratio in general stress states." Géotechnique, 61(8), 709-713.
[4] Setiasabda, Ezra Y. (2020). “Material point method for large deformation modeling in geomechanics using isoparametric elements.” Ph.D. dissertation, Berkeley, CA: Univ. of California, Berkeley.
