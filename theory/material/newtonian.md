# Newtonian

The constitutive equation for stress tensor in a fluid motion is assumed to be of the
general form:

$$\mathbf{\sigma} = − p \bf{I} + \tau$$

where $\tau = \mathbf{F(D)}$ is known as the viscous or extra stress tensor, $p$ is the thermodynamic pressure and $\mathbf{D}$ is the rate of deformation.

The mean stress $\tilde \sigma$ is equal to the thermodynamic pressure $−p$, if and only if one
of the following two conditions are satisfied:

   * Fluid is incompressible: $\nabla \cdot \bf{D} = 0$

   * Stokes condition: $K = \frac{2}{3}\mu + \lambda = 0.$

where $\mu$ and $\lambda$ are Lame constants. In general, the Stokes condition does not hold. For Newtonian fluids, incompressibility does not necessarily imply that $\tilde \sigma = − p$. 

The thermodynamic pressure $p$ is calculated as

$$p = p_0 - K d\epsilon_v$$

where, $p_0$ is the initial thermodynamic pressure, calculated as the mean initial stress,
$K$ is the bulk modulus and $d\epsilon_v$ is the volumetric strain (compressive volumetric strain
is negative). Typically, the thermodynamic pressure is calculated as the centre of the cell
to minimise pressure osciallations.


For an isotropic viscous fluid, the stress tensor takes the form:

$$ \sigma = 2 \mu \mathbf{D} + \lambda(tr \mathbf{D})\mathbf{I} - p\mathbf{I} $$.

$$ \sigma_{ij} = 2 \mu D_{ij} + (\lambda D_{kk} - p) \delta_{ij} $$

$$ \sigma_{ij} = - p \delta_{ij} + 2 \mu D_{ij} - \frac{2}{3} \mu D_{kk}  $$

## References

[1] Reddy, J. N. (2014). An Introduction to Nonlinear Finite Element Analysis: with applications to heat transfer, fluid mechanics, and solid mechanics. OUP Oxford.
