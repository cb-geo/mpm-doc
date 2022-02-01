## Ascii files
### Mesh

The ASCII mesh has the following format:

```
nnodes 	ncells
# nodal coordinates
x_0	y_0 	z_0
x_1	y_1 	z_1
...
x_i	y_i	z_i
...
x_n	y_n	z_n 
# cells
# indices of nodes forming each cell
n1_0 n1_1 n1_2 n1_3 n1_4 n1_5 n1_6 n1_7
n2_3 n2_4 n2_5 n2_6 n2_7 n2_8 n2_9 n2_10
...
ni_i ni_j ni_k ni_l ni_w ni_x ni_y ni_z
...
...
nn_i nn_j nn_k nn_l nn_w nn_x nn_y nn_z
```

`nnodes` is the number of nodes.

`ncells` the number of cells.
 
$x_i$, $y_i$, $z_i$ correspond to the Cartesian coordinates of each node. 

Each node will be assigned a unique id from `0` to `nnodes -1`, and will be assigned in the 
order in which they appear. 

`n1_1, n1_2... n1_nn` corresponds to the node ids forming each cell. Cell ids should be arranged in the same order as the shape functions. This code uses the standard GMSH order for numbering nodes in cells.

An example of a 3D mesh comprising of two cells and twelve nodes is shown below:


```
# 12 nodes and 2 cells
12	2
0	0	0	# Node 0
1	0	0	# Node 1
1	1	0	# Node 2
0	1	0	# Node 3
0	0	1	# Node 4
1	0	1	# Node 5
1	1	1	# Node 6
0	1	1	# Node 7
2	0	0	# Node 8
2	1	0	# Node 9
2	0	1	# Node 10
2	1	1	# Node 11
0	1	2	3	4	5	6	7	# Cell 0
1	8	9	2	5	10	11	6	# Cell 1
```

### Material points

The material points file has the following format:

```
nparticles
# material point coordinates
x_0	y_0 	z_0
x_1	y_1 	z_1
...
x_i	y_i	z_i
...
x_n	y_n	z_n 
```

`nparticles` is the total number of particles. $x_i$, $y_i$, $z_i$ correspond to the Cartesian coordinates of each material point. The material points are assigned a unique id from 0 to `nparticles - 1`.

The `particles-cell.txt` file which describes the initial cell location of each material point has the following format:
```
p_0	c_0
p_1	c_1
...
p_i	c_i
...
p_n	c_n
```
where $p_i$ is the particle id and $c_i$ is the cell id where particle $p_i$ belongs.

### Particle Stresses [Optional]

The `particles_stresses.txt` file has the following format:

```
nparticles
# material point stresses
sigma_xx,0	sigma_yy,0	sigma_zz,0	tau_xy,0	tau_yz,0	tau_zx,0
sigma_xx,1	sigma_yy,1	sigma_zz,1	tau_xy,1	tau_yz,1	tau_zx,1
...
sigma_xx,i	sigma_yy,i	sigma_zz,i	tau_xy,i	tau_yz,i	tau_zx,i
...
sigma_xx,n	sigma_yy,n	sigma_zz,n	tau_xy,n	tau_yz,n	tau_zx,n
```

`nparticles` is the total number of particles. $\sigma_{xx,i}$, $\sigma_{yy,i}$, $\sigma_{zz,i}$, $\tau_{xy,i}$, $\tau_{yz,i}$, $\tau_{zx,i}$ correspond to the insitu stresses on each material point. Stresses are assigned in order to each material point based on the unique id from 0 to `nparticles - 1`. If including a `particles_stresses.txt` file, stresses must be assigned for all material points.