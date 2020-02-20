# Bingham

The constitutive equation for the stress tensor for a non-Newtonian fluid [1] can be
expressed as:

$$\mathbf{\sigma} = − p \bf{I} + \tau$$

$$\sigma_{ij} = − p \delta_{ij} + \tau_{ij}$$

where $\tau$ is known as the viscous or extra stress tensor and $p$ is the thermodynamic pressure.

The mean stress $\tilde \sigma$ is equal to the thermodynamic pressure $−p$, if and only if one
of the following two conditions are satisfied:

   * Fluid is incompressible: $\nabla \cdot \bf{D} = 0$

   * Stokes condition: $K = \frac{2}{3}\mu + \lambda = 0.$

In general, the Stokes condition does not hold. For Newtonian fluids, incompressibility
does not necessarily imply that $\tilde \sigma = − p$.

The thermodynamic pressure $p$ is calculated as

$$p = p_0 - K d\epsilon_v$$

where, $p_0$ is the initial thermodynamic pressure, calculated as the mean initial stress,
$K$ is the bulk modulus and $d\epsilon_v$ is the volumetric strain (compressive volumetric strain
is negative). Typically, the thermodynamic pressure is calculated as the centre of the cell
to minimise pressure osciallations.

The Bingham fluid differs from most other fluids in that it can
sustain an applied stress without fluid motion occurring. The fluid possesses a yield
stress, $τ_0$, such that when the applied stresses are below $τ_0$ no motion occurs; when
the applied stresses exceed $τ_0$ the material flows, with the viscous stresses being
proportional to the excess of the stress over the yield condition. In a general form,
the Bingham model [2] can be expressed as

$$\boldsymbol{\tau} = 2 \left( \frac{\tau_0}{\dot{\gamma}} + \mu \right) \mathbf{D} \qquad
\mathrm{when} \quad \frac{1}{2}tr(\boldsymbol{\tau}^2) \ge \tau_0^2$$

$$\boldsymbol{\tau} = 0 \quad \mathrm{when} \quad \frac{1}{2}tr(\boldsymbol{\tau}^2) < \tau_0^2$$


where $tr$ denotes the trace. The apparent viscosity of the material beyond the yield point is $\left( \frac{\tau_0}{\dot{\gamma}} + \mu \right)$.

Where $\dot{\gamma}$ is the shear rate defined as

$$ \dot{\gamma} = \sqrt{2 D_{ij}D_{ij}} $$



## References

[1] Reddy, J. N. (2014). An Introduction to Nonlinear Finite Element Analysis: with applications to heat transfer, fluid mechanics, and solid mechanics. OUP Oxford.

[2] Beverly, C. R. and Tanner, R. I. (1992). Numerical analysisof three-dimensional Bingham plastic flow. Journal of non-newtonian fluid mechanics 42(1-2), 85-115.
