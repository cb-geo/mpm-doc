# Modified Cam-Clay Model

Modified Cam-Clay Model can be used as the constitutive model for normal consolidation soil or over-consolidation soil.

## Yield function

$$F = \frac{q^2}{M^2}+p'(p'-p_c)$$ 
<br/>

$$M(\theta) = M_{tc} - \frac{M_{tc}^2}{3 + M_{tc}}cos(\frac{3\theta}{2})$$

Where $p'$ is the effective mean pressure, $q$ is the magnitude of deviatoric stress, $\theta$ is the Lode's angle, $M$ is the slope of the critical line, $M_{tc}$ is the value of $M$ under trial extension status.

## Flow rule

An assosiated potential flow rules is defined, which means it has the same format with the yield function.

## Elastic modulus

The elastic modulus is computed based on the current stress status

$$E_b = \frac{1+e}{\kappa}p'$$
<br/>

$$G_s = \frac{3E_b(1-2\nu)}{2(1+\nu)}$$

Where $e$ is the void ratio, $\kappa$ is the swell/recompression index, $\nu$ is the Possion's ratio, $E_b$ is the volumetric modulus, $G_s$ is the shear modulus.

## Bonding behavior

The bonding behavior refers to Uchida et al.(2012) reserach. 
The bonding effect on the preconsolidation effective mean pressure and the yield function is computed as

$$F = \frac{q^2}{M^2}+(p'+p_{cc})(p'-p_c-p_{cc}-p_{cd})$$ 
<br/>

$$p_{cd} = a(\chi s_h)^b$$
<br/>

$$p_{cc} = c(\chi s_h)^d$$

The bonding effect on the shear modulus is computed as

$$G = G_s + G_b$$
<br/>

$$G_b = m_s(\chi s_h)$$

Where $G$ is the total shear modulus, $G_s$ is the original shear modulus, $G_b$ is the bonding enhancement part, $m_s$ is bonding parameter for the shear modulus.

## Subloading behavior

The subloading behavior make the soil form plastic strain even it's inside the yield surfacce. The detailed information can be found in Uchida et al.(2012) Then the yield function is changed to

$$F = \frac{q^2}{M^2}+(p'+p_{cc})[p'-R(p_c + p_{cc} + p_{cd})]$$ 
<br/>

$$dR = -u(1+\frac{p_{cd}+p_{cc}}{p_c}\ln{R}|d\epsilon^p|)$$

Where $R$ is the subloading ratio, $u$ is the subloading parameter (a smaller value means more plastic strain will be formed), $|d\epsilon^p|$ is the magnitude of the plastic strain increment.

## Input parameters

An example input JSON is given as follow for Modified Cam-Clay Model.

```
  "materials": [
    {
      "id" : 0,
      "type": "ModifiedCamClay2D",
      "density": 2000,
      "poisson_ratio": 0.3,
      "youngs_modulus": 2E7,
      "ocr": 1,
      "pc0": 6.0E+6,
      "m": 1.07,
      "lambda": 0.11,
      "kappa": 0.008,
      "p_ref": 6.0E+6,
      "e_ref": 0.38,
      "three_invariants": false,
      "subloading": true,
      "subloading_u": 100,
      "bonding": true,
      "mc_a": 1.2E+7,
      "mc_b": 1,
      "mc_c": 1.2E+7,
      "mc_d": 10,
      "s_h": 1,
      "m_degradation": 1,
      "m_shear": 2.4E+9
    }
  ]
```
  * "type" is the material type ("ModifiedCamClay2D" for 2D plain strain condition, "ModifiedCamClay3D" for 3D), 
  * "density" ,"poisson_ratio" and "youngs_modulus" are the general elastic paramters, the "youngs_modulus" is only used when the current mean pressure is negative,
  * "ocr" is the over consolidation ratio
  * "pc0" is the initial preconsolidation pressure
  * "m" is the slope of the critical line (it is defined as $M_{tc}$ if the "three_invariants" type is activated)
  * "lambda" is the virgin compression index $\lambda$,
  * "kappa" is the swell/recompression index $\kappa$.
  * "p_ref" is the reference effective mean pressure, 
  * "e_ref" is the void ratio based on the reference effective mean pressure, the initial void ratio is then defined as
    <br/>
    $e_{0} = e_{ref} - \lambda\ln{\frac{p_{c0} / OCR}{p_{ref}}} - \kappa \ln{OCR}$
  * "three_invariants" is the three invariants option (true or false), which represent if $M$ varies as Lode's angle,
  * "subloading" is the subloading option (true or false),
  * "bonding" is the bonding behavior option (true or false),
  "subloading_u" is the subloading parameter $u$,
  * "mc_a", "mc_b" is the paramters, $a$ and $b$, for dilation part of the bonding preconsolidation pressure ($p_{cd}$),
  * "mc_c", "mc_d" is the paramters, $c$ and $d$, for cohesion part of the bonding preconsolidation pressure ($p_{cc}$),
  * "s_h" is the initial saturation of bonding effect ($0 \leq s_h \leq 1$),
  * "m_degradation" is the degradation parameter for preconsolidation pressure,
  * "m_shear" is the bonding parameter ($m_s$) for shear modulus

## References

[1] Uchida, Shun, Kenichi Soga, and Koji Yamamoto. "Critical state soil constitutive model for methane hydrate soil." Journal of Geophysical Research: Solid Earth 117.B3 (2012).
