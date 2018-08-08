# Velocity gradient  {docsify-ignore}

In 3 dimensions, the gradient, $\nabla \bf {v}$, of the velocity \textbf{v} is a second-order tensor which can be expressed as the matrix **L**:

$$
\bf{L}=\nabla \bf{v} =\left[
\begin{matrix}
\frac{\partial v_x}{\partial x} & \frac{\partial v_x}{\partial y} & \frac{\partial v_x}{\partial z} \\\\
\frac{\partial v_y}{\partial x} & \frac{\partial v_y}{\partial y} & \frac{\partial v_y}{\partial z} \\\\
\frac{\partial v_z}{\partial x} & \frac{\partial v_z}{\partial y} & \frac{\partial v_z}{\partial z}
\end{matrix}
\right]
$$

**L** can be decomposed into the sum of a symmetric matrix **D** and a skew-symmetric matrix **W** as follows

$$ D = \frac{1}{2} ( L + L^T) $$

$$ W = \frac{1}{2} ( L - L^T) $$

where **D** is called the rate of deformation tensor and **W** is called the vorticity tensor or spin tensor.


$$ \dot D=\left[
\begin{matrix}
\frac{du_x}{dx}  & \frac{1}{2}(\frac{du_x}{dy} + \frac{du_y}{dx}) & \frac{1}{2}(\frac{du_x}{dz} + \frac{du_z}{dx}) \\\\
\frac{1}{2}(\frac{du_x}{dy} + \frac{du_y}{dx}) & \frac{du_y}{dy}  & \frac{1}{2}(\frac{du_y}{dz} + \frac{du_z}{dy}) \\\\
\frac{1}{2}(\frac{du_x}{dz} + \frac{du_z}{dx}) & \frac{1}{2}(\frac{du_y}{dz} + \frac{du_z}{dy}) & \frac{du_z}{dz}  
\end{matrix}
\right]
$$

As a 6x1 the rate of deformation tensor $D = \left[\frac{du_x}{dx}, \frac{du_y}{dy}, \frac{du_z}{dz}, \frac{1}{2}(\frac{du_x}{dy} + \frac{du_y}{dx}), \frac{1}{2}(\frac{du_y}{dz} + \frac{du_z}{dy}), \frac{1}{2}(\frac{du_x}{dz} + \frac{du_z}{dx})\right]^T$

# Strain rate  {docsify-ignore}

In CB-Geo MPM, the strain rate tensor $\dot\epsilon$ is calculated as $B * u$, where $B$ is
the B-matrix and $u$ represents the velocity components.

$$ \dot \epsilon=\left[
\begin{matrix}
\frac{du_x}{dx}  & (\frac{du_x}{dy} + \frac{du_y}{dx}) & (\frac{du_x}{dz} + \frac{du_z}{dx}) \\\\
(\frac{du_x}{dy} + \frac{du_y}{dx}) & \frac{du_y}{dy}  & (\frac{du_y}{dz} + \frac{du_z}{dy}) \\\\
(\frac{du_x}{dz} + \frac{du_z}{dx}) & (\frac{du_y}{dz} + \frac{du_z}{dy}) & \frac{du_z}{dz}  
\end{matrix}
\right]
$$

As a 6x1 strain rate $\dot \epsilon = \left[\frac{du_x}{dx}, \frac{du_y}{dy}, \frac{du_z}{dz}, (\frac{du_x}{dy} + \frac{du_y}{dx}), (\frac{du_y}{dz} + \frac{du_z}{dy}), (\frac{du_x}{dz} + \frac{du_z}{dx})\right]^T$


## Relate strain rate $\dot \epsilon$ and rate of deformation tensor **D**  {docsify-ignore}

The rate of deformation tensor $D$ is not the same as the time rate of change of the
infinitesimal strain tensor $\epsilon$, that is, the strain rate $\dot \epsilon$̇,
where superposed dot signifies the material time derivative.

$$ \dot \epsilon = \left[ \dot \epsilon_{xx}, \dot \epsilon_{yy}, \dot \epsilon_{yy}, \dot \epsilon_{xy}, \dot \epsilon_{yz}, \dot \epsilon_{zx}\right]^T$$

The rate of deformation tensor **D** can be written as a function of strain rate $\dot \epsilon$:

$$ D = \left[ \dot \epsilon_{xx}, \dot \epsilon_{yy}, \dot \epsilon_{yy}, \frac{1}{2}\dot \epsilon_{xy}, \frac{1}{2} \dot \epsilon_{yz}, \frac{1}{2} \dot \epsilon_{zx}\right]^T$$