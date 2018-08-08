# Velocity gradient {docsify-ignore}

In 3 dimensions, the gradient, $\nabla v$, of the velocity $v$ is a second-order tensor which can be expressed as the matrix $\mathbf{L}$:

$$
\bf{L}=\nabla v =\left[
\begin{matrix}
\frac{\partial v_x}{\partial x} & \frac{\partial v_x}{\partial y} & \frac{\partial v_x}{\partial z} \\\\
\frac{\partial v_y}{\partial x} & \frac{\partial v_y}{\partial y} & \frac{\partial v_y}{\partial z} \\\\
\frac{\partial v_z}{\partial x} & \frac{\partial v_z}{\partial y} & \frac{\partial v_z}{\partial z}
\end{matrix}
\right]
$$

$\mathbf{L}$ can be decomposed into the sum of a symmetric matrix $\mathbf{D}$ and a skew-symmetric matrix $\mathbf{W}$ as follows

$$ \mathbf{D} = \frac{1}{2} (L + L^T) $$

$$ \mathbf{W} = \frac{1}{2} (L - L^T) $$

where $\mathbf{D}$ is called the rate of deformation tensor and $\mathbf{W}$ is called the vorticity tensor or spin tensor.


$$ \mathbf{D}=\left[
\begin{matrix}
\frac{du_x}{dx}  & \frac{1}{2}(\frac{du_x}{dy} + \frac{du_y}{dx}) & \frac{1}{2}(\frac{du_x}{dz} + \frac{du_z}{dx}) \\\\
\frac{1}{2}(\frac{du_x}{dy} + \frac{du_y}{dx}) & \frac{du_y}{dy}  & \frac{1}{2}(\frac{du_y}{dz} + \frac{du_z}{dy}) \\\\
\frac{1}{2}(\frac{du_x}{dz} + \frac{du_z}{dx}) & \frac{1}{2}(\frac{du_y}{dz} + \frac{du_z}{dy}) & \frac{du_z}{dz}  
\end{matrix}
\right]
$$

As a 6x1 the rate of deformation tensor $\mathbf{D} = \left[\frac{du_x}{dx}, \frac{du_y}{dy}, \frac{du_z}{dz}, \frac{1}{2}(\frac{du_x}{dy} + \frac{du_y}{dx}), \frac{1}{2}(\frac{du_y}{dz} + \frac{du_z}{dy}), \frac{1}{2}(\frac{du_x}{dz} + \frac{du_z}{dx})\right]^T$

# Strain rate  {docsify-ignore}

In CB-Geo MPM, the strain rate tensor $\dot\epsilon$ is calculated as $\mathbf{B} u$, where $\mathbf{B}$ is
the B-matrix and $u$ represents the velocity components.

$$ \dot \epsilon= \mathbf{B}u =\left[
\begin{matrix}
\frac{du_x}{dx}  & (\frac{du_x}{dy} + \frac{du_y}{dx}) & (\frac{du_x}{dz} + \frac{du_z}{dx}) \\\\
(\frac{du_x}{dy} + \frac{du_y}{dx}) & \frac{du_y}{dy}  & (\frac{du_y}{dz} + \frac{du_z}{dy}) \\\\
(\frac{du_x}{dz} + \frac{du_z}{dx}) & (\frac{du_y}{dz} + \frac{du_z}{dy}) & \frac{du_z}{dz}  
\end{matrix}
\right]
$$

As a 6x1 strain rate $\dot \epsilon = \left[\frac{du_x}{dx}, \frac{du_y}{dy}, \frac{du_z}{dz}, (\frac{du_x}{dy} + \frac{du_y}{dx}), (\frac{du_y}{dz} + \frac{du_z}{dy}), (\frac{du_x}{dz} + \frac{du_z}{dx})\right]^T$


## Relate strain rate $\dot \epsilon$ and rate of deformation tensor $\mathbf{D}$ {docsify-ignore}

The rate of deformation tensor $\mathbf{D}$ is not the same as the time rate of change of the
infinitesimal strain tensor $\epsilon$, that is, the strain rate $\dot \epsilon$̇,
where superposed dot signifies the material time derivative.

$$ \dot \epsilon = \left[ \dot \epsilon_{xx}, \dot \epsilon_{yy}, \dot \epsilon_{yy}, \dot \epsilon_{xy}, \dot \epsilon_{yz}, \dot \epsilon_{zx}\right]^T$$

The rate of deformation tensor $\mathbf{D}$ can be written as a function of strain rate $\dot \epsilon$:

$$ \mathbf{D} = \left[ \dot \epsilon_{xx}, \dot \epsilon_{yy}, \dot \epsilon_{yy}, \frac{1}{2}\dot \epsilon_{xy}, \frac{1}{2} \dot \epsilon_{yz}, \frac{1}{2} \dot \epsilon_{zx}\right]^T$$