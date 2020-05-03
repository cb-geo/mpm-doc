# Mohr-Coulomb Model

Mohr-Coulomb model is the most common used constitutive model for soil.

## Yield function

The current Mohr-Coulomb model includes two yield criterions, shear failure and tension failure. 

### Shear failure

The Mohr-Coulomb criterion assumes that yield occurs when the shear stress on any point in a material reaches a value that depends linearly on the normal stress in the same plane. The Mohr-Coulomb model is based on plotting Mohr's circle for states of stress at yield in the plane of the maximum and minimum principal stresses. The yield line is the best straight line that touches these Mohr's circles.

For general states of stress the yield function is more conveniently written in terms of three stress invariants as

$$F = R_{mc}q+p'tan \phi' - c'$$ 
<br/>

$$R_{mc}(\theta, \phi') = \frac{1}{\sqrt{3}cos\phi'}sin(\theta+\frac{\pi}{3})+\frac{1}{3}cos(\theta+\frac{\pi}{3})tan\phi'$$

Where $p'$ is the effective mean pressure, $q$ is the magnitude of deviatoric stress, $\theta$ is the Lode's angle, $\phi'$ is the effective friction angle, $c$ is the effective cohesion.
### Tension cut-off

The tension cutoff is modeled using the Rankine surface, which is written as

$$F = R_{r}q+p' - \sigma ^t$$
<br/>

$$R_r = \frac{2}{3}cos\theta$$

Where $\sigma ^t$ is the tension strength.

## Flow rule

Two non-assosiated potential flow rules are defined for two failure type separatly.

### Plastic flow on the Mohr-Coulomb yield surface

The flow potential, $P$, for the Mohr-Coulomb yield surface is chosen as a hyperbolic function in the meridional stress plane and the smooth elliptic function proposed by Menétrey and Willam (1995) in the deviatoric stress plane:

$$P = \sqrt{(\epsilon c'tan\psi)^2+(R_{mw}q)^2} + p'tan\psi$$
<br/>

$$R_{mw}(\theta,e) = \frac{4(1-e^2)cos^2\theta + (2e-1)^2}{2(1-e^2)cos\theta + (2e-1)\sqrt{4(1-e^2)cos^2\theta + 5e^2 - 4e}}R_{mc}(\frac{\pi}{3},\phi')$$
<br/>

$$R_{mc}(\frac{\pi}{3},\phi') = \frac{3 - sin\phi'}{6cos\phi'}$$
<br/>

$$e = \frac{3 - sin\phi'}{3 + sin\phi'}$$

Where $\epsilon$ is a parameter referred to as the meridional eccentricity (default as 0.1). $e$ is a parameter referred to as the deviatoric eccentricity (0<$e$<0.5).

### Plastic flow on the Rankine surface (Tension)

A flow potential that results in a nearly associative flow is chosen for the Rankine surface and is constructed by modifying the Menétrey-Willam potential described earlier:

$$P_t = \sqrt{(\epsilon_t\sigma_t )^2+(R_{t}q)^2} + p'$$
<br/>

$$R_{t}(\theta,e_t) = \frac{1}{3} \frac{4(1-e_t^2)cos^2\theta + (2e_t-1)^2}{2(1-e_t^2)cos\theta + (2e_t-1)\sqrt{4(1-e_t^2)cos^2\theta + 5e_t^2 - 4e_t}}$$

Where $\epsilon_t$ is a parameter referred to as the meridional eccentricity (default as 0.1). $e_t$ is a parameter referred to as the deviatoric eccentricity (default as 0.6).
## Strain softening

A linear softening rule is defined for the shear strength parameters as follows

$$ \phi',c',\psi(\epsilon_s^p)=\left\{
\begin{aligned}
\phi'_{peak},c'_{peak},\psi'_{peak} & &(\epsilon_s^p < \epsilon_{s,peak}^p) \\
\frac{\phi'_{peak},c'_{peak},\psi'_{peak} - \phi'_{residual},c'_{residual},\psi'_{residual}}{\epsilon_{s,residual}^p - \epsilon_{s,peak}^p}(\epsilon_{s}^p - \epsilon_{s,peak}^p) & & (\epsilon_{s,peak}^p < \epsilon_s^p < \epsilon_{s,residual}^p) \\
\phi'_{residual},c'_{residual},\psi_{residual}& & (\epsilon_s^p > \epsilon_{s,residual}^p)
\end{aligned}
\right.
$$

Where the $\epsilon_s^p$ is the plastic deviatoric strain.
## Input parameters

An example input JSON is given as follow for Mohr-Coulomb model.

```
  "materials": [
    {
      "id" : 0,
      "type": "MohrCoulomb2D",
	  "density": 2000.0,
	  "poisson_ratio": 0.3,
	  "youngs_modulus": 2E7,
	  "softening": true,
	  "friction": 25,
	  "dilation": 0,
	  "cohesion": 2E4,
	  "residual_friction": 13,
	  "residual_dilation": 0,
	  "residual_cohesion": 5E3,
	  "peak_pdstrain": 0,
	  "residual_pdstrain": 0.05,
	  "tension_cutoff": 1E4
    }
  ]
```
  * "type" is the material type ("MohrCoulomb2D" for 2D plain strain condition, "MohrCoulomb3D" for 3D), 
  * "density" ,"poisson_ratio" and "youngs_modulus" are the general elastic paramters, 
  * "softening" is the strain softening option (true or false), 
  * "friction" is the friction angle in degree (peak value when softening is activated), 
  * "dilation" is the dilation angle in degree (peak value when softening is activated), 
  * "cohesion" is the cohesion in Pa (peak value when softening is activated), 
  * "residual_friction" is the residual friction angle in degree, 
  * "residual_dilation" is the residual dilation angle in degree,
  * "residual_cohesion" is the residual cohesion in Pa, 
  * "peak_pdstrain" is the start point of strain softening (plastic deviatoric strain)
  * "residual_pdstrain" is the end point of strain softening (plastic deviatoric strain)
  * "tension_cutoff" is the tension strength in Pa (1E22 for no tension cut-off)

## References

[1] Menetrey, Philippe, and K. J. Willam. "Triaxial failure criterion for concrete and its generalization." Structural Journal 92.3 (1995): 311-318.
