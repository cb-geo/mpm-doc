# Update Stress First (USF)
> MPM Explicit

## Nomenclature {docsify-ignore}

### General {docsify-ignore}

$G$   acceleration due to gravity ($G = 9.81 m/s^2$)

### Material Point {docsify-ignore}

$\textbf{a}_p^t$ acceleration of material point $p$ at time $t$

$m_p^t$ mass of material point $p$ at time $t$

$m\textbf{v}_p^t$ momentum of material point $p$ at time $t$

$n_p$ total number of material points in the body

$s_p$ spacing between material points

$\textbf{t}_p^t$ traction at material point $p$

$\textbf{v}_p^t$ velocity of material point $p$ at time $t$

$V_p$ volume at material points $p$

$\textbf{x}_p^t$ coordinate vector of material point $p$ at time $t$

$\varepsilon_{v,p}^t$ volumetric strain of particle $p$ at time $t$

$\rho$ density of material point


### Node {docsify-ignore}

$\textbf{a}_i^t$ acceleration of node $i$

$\textbf{b}_i^t$ body force of node $i$

$\textbf{f}_i^t$ nodal force of node $i$ at time $t$

$\textbf{f}_i^{ext,t}$ nodal external force of node $i$ at time $t$

$\textbf{f}_i^{int,t}$ nodal internal force of node $i$ at time $t$

$m_i^t$ mass of node $i$ at time $t$

$m\textbf{v}_i^t$ momentum of node $i$ at time $t$

$\textbf{t}_i^t$ traction at node $i$

$\textbf{v}_i^t$ velocity of node $i$ at time $t$

$\boldsymbol{\varepsilon}_i^t$ strain of node $i$ at time $t$

$\boldsymbol{\sigma}_i^t$ stress of node $i$ at time $t$


### Shape Functions

$B_i (\textbf{x}_p^t)$ gradient of the shape function that maps node $i$ to material point $p$ and vice versa such that $B = \frac{dN}{d\textbf{x}}$

$N_i (\textbf{x}_p^t)$ shape function that maps node $i$ to material point $p$ and vice versa with independent variable of the location of each material point at time $t$
