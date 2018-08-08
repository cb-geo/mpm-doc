# Bingham

The constitutive equation for the stress tensor for a non-Newtonian fluid can be
expressed as:

$$\sigma = − p I + \tau \qquad (\sigma_{ij} = −p \delta_{ij} + \tau_{ij})$$

where $\tau$ is known as the viscous or extra stress tensor.

The Bingham fluid differs from most other fluids in that it can
sustain an applied stress without fluid motion occurring. The fluid possesses a yield
stress, $τ_0$, such that when the applied stresses are below $τ_0$ no motion occurs; when
the applied stresses exceed $τ_0$ the material flows, with the viscous stresses being
proportional to the excess of the stress over the yield condition. In a general form,
the Bingham model can be expressed as

$$\tau = \left( \frac{\tau_0}{\sqrt{I_2}} + 2 \mu \right) \mathbf{D} \qquad
\mathrm{when} \quad \frac{1}{2}tr(\tau^2) \ge \tau_0^2$$

$$\tau = 0 \mathrm{when} \quad \frac{1}{2}tr(\tau^2) < \tau_0^2$$

The apparent viscosity of the material beyond the yield point is
$\left( \frac{\tau_0}{\sqrt{I_2}} + 2 \mu \right)$.