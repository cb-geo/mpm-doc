# Contact Mechanics Between Distinct Bodies

The Material Point Method is naturally capable of modelling distinct bodies because each material point holds the information of its own material. However, the conventional MPM alone does not handle contact mechanics as the surface of distinct bodies meet. Additionally, one may need to identify contact interfaces without the need of prescribing their geometry at the start of a simulation. Therefore, the MPM requires a contact algorithm capable of identifying the contact of distinct bodies and applying their contact relationship. A first approach to deal with frictional contact was introduced by Bardenhagen et. al. (2000). This approach is the one presented within this document. Bardenhagen et. al. (2000) also describes the normal to the interface surface for each material as the normalized gradients of the volume. However, the authors method can lead to normal vectors of both materials that are not always aligned -- i.e., opposite to each other for two materials in contact -- which can lead to further errors of the contact relationship. Therefore, a slight change, as proposed by Nairn (2013), was introduced to the algorithm to handle such cases.

# Contact Algorithm {docsify-ignore}

> at each time step $\Delta t$ from $t$ to $t + \Delta t$, the nodal kinematics are initially computed similarly to the conventional MPM algorithm but considering the distinct materials:

## Initial Nodal Kinematics

* The state parameters at the material points are initialised at the beginning of every time step in the same manner as it is in the conventional MPM.

* The shape functions $N_i(x_p^t)$ and the gradient of the shape functions $B_i (x_p^t)$ are also computed at each material point as the conventional MPM dictates, with no changes due to the contact algorihtm.

* A nodal set of all the material ids (with no repetition) is created by identifying the material ids of all the material points in the cell. Each new material id is appended to this set. The size of this set will indicate whether the node is located at an interface of two or more materials or not.

* The nodal mass and momentum are calculated separately for each body $k$. They are based on the mass and velocity of all the material points in the cell that belong to their respective body and are mapped to the nodes using the shape functions.

    * Compute nodal mass of each body

        $$ m^t_{i,k} = \sum\limits_{p \in k} N_i(\textbf{x}_p^t) m_p $$

    * Compute nodal momentum of each momentum

        $$ (m \textbf{v})^t_{i,k} =  \sum\limits_{p \in k} N_i(\textbf{x}_p^t)m_p \textbf{v}_p^t $$

* The nodal velocities at each active node $i$ is computed for each material $k$ based on the momentum and the nodal mass.

    $$ \textbf{v}_{i,k}^t = \frac{(m \textbf{v})_{i,k}^t}{m_{i,k}^t} $$

* For the USF approach:

    * The strain at each material point is computed by mapping the strain rate from the nodes considering the material id of $p$:

        $$ \boldsymbol{\varepsilon}_p^t = \sum\limits_{i} B_i(\textbf{x}_p^t) \textbf{v}_{i,k}^t \quad \mbox{with} \quad k \ni p $$ 

    * The stress is then updated at each material point based on the constitutive model as it is for the conventional MPM with the USF approach. 

* Compute the nodal body force from the material points considering each material id separately:

    * Body force:

        $$ \textbf{b}_{i,k}^{t} = G \sum\limits_{p \in k} N_i(\textbf{x}_p^t) m_p $$

* Compute the nodal external and internal force considering each material id separately

    * External force:

        $$ (\textbf{f})^{ext,t}_{i,k} = \textbf{b}_{i,k}^t + \textbf{t}_{i,k}^t $$

    * Internal force:

        $$ (\textbf{f})^{int,t}_{i,k} = \sum\limits_{p \in k} V_p^t B_i(\textbf{x}_p^t) \boldsymbol{\sigma}_p^t $$

    * Resulting force:

        $$ \textbf{f}_{i,k}^t = (\textbf{f})^{ext,t}_{i,k} + (\textbf{f})^{int,t}_{i,k} $$

* The nodal acceleration and velocities of the next step $ t + \Delta t$ for each mateiral id are computed on all active nodes:

    * Nodal acceleration:

        $$ \textbf{a}_{i,k}^{t+\Delta t} = \frac{\textbf{f}_{i,k}^t}{m_{i,k}^t} $$

    * Nodal velocity:

        $$ \textbf{v}_{i,k}^{t + \Delta t} = \textbf{v}_{i,k}^t + \textbf{a}_{i,k}^{t + \Delta t} * \Delta t $$

## Normal Vector Computation

> at each time step $\Delta t$ from $t$ to $t + \Delta t$:

* The domain gradient is computed at each node for each separate material by mapping the gradient of the volumes at each node:

    $$ \textbf{g}_{i,k}^t = \sum\limits_{p \in k} V_p^t B_i(\textbf{x}_p^t) $$

* The normal unit vector at the interface of two materials is then determined considering the Maximum Volume Gradient Approach (MVG). This approach compares the domain gradients of the two materials in contact. The largest one in magnitude is normalized to determine the normal unit vector of that material while the normal unit vector of the lowest is set to be the opposite of the latter:

    $$ || \textbf{g}_{i,a}^t || > || \textbf{g}_{i,b}^t || \Rightarrow \hat{n}_{i,a}^t = \frac{\textbf{g}_{i,a}^t }{|| \textbf{g}_{i,a}^t  ||} \quad \mbox{and} \quad \hat{n}_{i,b}^t = \frac{\textbf{g}_{i,b}^t }{|| \textbf{g}_{i,b}^t  ||} $$

## Apply Contact Mechanics

> at each time step $\Delta t$ from $t$ to $t + \Delta t$:

* A contact node is detected by checking the size of its set of material ids; sets with more than one material is considered a contact node.

> for each contact node:

* The material's relative velocity to the velocity of the center of mass is computed at each contact node. The velocity of the center of mass is the one determined using the conventional MPM algorithm.

    $$ \Delta \textbf{v}_{i,k}^{t+\Delta t} = \textbf{v}_{i,k}^{t+\Delta t} - \textbf{v}_{i}^{t+\Delta t} $$

* The material's movement is checked at each contact node:

    $$ \Delta \textbf{v}_{i,k}^{t+\Delta t} \cdot \hat{n}_{i,k}^t > 0 \quad \Rightarrow \quad \mbox{approaching} $$

    $$ \Delta \textbf{v}_{i,k}^{t+\Delta t} \cdot \hat{n}_{i,k}^t \leq 0 \quad \Rightarrow \quad \mbox{separating} $$

* If the node is not a contact node or if the material is separating, nothing is done ($ \tilde{\textbf{v}}_{i,k}^{t+\Delta t} = \textbf{v}_{i,k}^{t+\Delta t} $). Otherwise (approaching condition):

    * The normal and tangential components of the relative velocity are computed

        $$ \Delta \textbf{v}_{i,k,norm}^{t+\Delta t} = [\Delta \textbf{v}_{i,k}^{t+\Delta t} \cdot \hat{n}_{i,k}^t] \hat{n}_{i,k}^t $$

        $$ \Delta \textbf{v}_{i,k,tan}^{t+\Delta t} = \hat{n}_{i,k}^t \times [\Delta \textbf{v}_{i,k}^{t+\Delta t} \times \hat{n}_{i,k}^t] $$

    * The following normal and tangential corrections are determined

        $$ \textbf{c}_{i,k,norm}^{t + \Delta t} = - \Delta \textbf{v}_{i,k,norm}^{t+\Delta t} $$

        $$ \textbf{c}_{i,k,tan}^{t + \Delta t} = - \min(\mu \Delta \textbf{v}_{i,k,norm}^{t+\Delta t}, \Delta \textbf{v}_{i,k,tan}^{t+\Delta t}) $$

    * The nodal velocity is updated

        $$ \tilde{\textbf{v}}_{i,k}^{t+\Delta t} = \textbf{v}_{i,k}^{t+\Delta t} + \textbf{c}_{i,k,norm}^{t + \Delta t} + \textbf{c}_{i,k,tan}^{t + \Delta t} $$

## Update of Material Points

> at each time step $\Delta t$ from $t$ to $t + \Delta t$:

* Apply any velocity constraints (and acceleration constraints -- when velocity is set, acceleration is set to zero) ah the material points

* Update the position of the material points based on the nodal velocity of their specific material.

    * Material point velocity:

        $$ \textbf{v}_p^{t+\Delta t} = \sum\limits_{i} N_i(\textbf{x}_p^t)\tilde{\textbf{v}}_{i,k}^{t+\Delta t} \quad \mbox{with} \quad k \ni p $$

    * Material point position:

        $$ \textbf{x}_p^{t+\Delta t} = \textbf{x}_p^t + \textbf{v}_p^{t+\Delta t} * \Delta t $$

## Nomenclature {docsify-ignore}

### General {docsify-ignore}

$G$   acceleration due to gravity

### Material Point {docsify-ignore}

$p$ material point index

$\textbf{a}_p^t$ acceleration of the material point $p$ at time $t$

$m_p^t$ mass of the material point $p$ at time $t$

$(m\textbf{v})_p^t$ momentum of the material point $p$ at time $t$

$\textbf{t}_p^t$ traction at material point $p$ at time $t$

$\textbf{v}_p^t$ velocity of the material point $p$ at time $t$

$V_p$ volume at material point $p$

$\textbf{x}_p^t$ coordinates of the material point $p$ at time $t$

$\boldsymbol{\varepsilon}_{p}^t$ strain tensor of the material point $p$ at time $t$

### Node {docsify-ignore}

$i$ node index

$k$ material index

$\textbf{a}_{i,k}^t$ acceleration of node $i$ and material $k$

$\textbf{b}_{i,k}^t$ body force of node $i$ and material $k$ at time $t$

$\textbf{f}_{i,k}^t$ nodal force of node $i$ and material $k$ at time $t$

$\textbf{f}_{i,k}^{ext,t}$ nodal external force of node $i$ and material $k$ at time $t$

$\textbf{f}_{i,k}^{int,t}$ nodal internal force of node $i$ and material $k$ at time $t$

$m_{i,k}^t$ mass of node $i$ and material $k$ at time $t$

$(m\textbf{v})_{i,k}^t$ momentum of node $i$ and material $k$ at time $t$

$\textbf{t}_{i,k}^t$ traction at node $i$ and material $k$ at time $t$

$\textbf{v}_{i,k}^t$ velocity of node $i$ and material $k$ at time $t$

$\boldsymbol{\sigma}_{i,k}^t$ stress tensor of node $i$ and material $k$ at time $t$

$\textbf{v}_i^t$ velocity of the center of mass at node $i$ and time $t$

$\Delta \textbf{v}_{i,k}^t$ relative velocity of node $i$ and material $k$ at time $t$

$\Delta \textbf{v}_{i,k,norm}^t$ normal component of the relative velocity of node $i$ and material $k$ at time $t$

$\Delta \textbf{v}_{i,k,tan}^t$ tangent component of the relative velocity of node $i$ and material $k$ at time $t$

$\textbf{c}_{i,k,norm}^t$ normal correction of the velocity of node $i$ and material $k$ at time $t$

$\textbf{c}_{i,k,tan}^t$ tangent correction of the velocity of node $i$ and material $k$ at time $t$

$\tilde{\textbf{v}}_{i,k}^t$ corrected velocity of node $i$ and material $k$ at time $t$

### Shape Functions

$B_i (\textbf{x}_p^t)$ gradient of the shape function that maps node $i$ to material point $p$ and vice versa such that $B = \frac{dN}{d\textbf{x}}$

$N_i (\textbf{x}_p^t)$ shape function that maps node $i$ to material point $p$ and vice versa with independent variable of the location of each material point at time $t$


[1] Bardenhagen, S.G., Brackbill, J. U., Sulsky, D. (2000). The material-point method for granular materials. Computer Methods in Applied Mechanics and Engineering, 187(3-4), 529-541.

[2] Nairn, J. A. (2013). Modeling imperfect interfaces in the material point method using multimaterial methods. Computer Modeling in Engineering and Sciences, 1(1), 1-15.