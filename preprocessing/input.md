# Input

The CB-Geo MPM code uses a `JSON` file for input configuration.

```JSON
{
  "title": "Example JSON Input for 3D MPM",
  "input_files": {
    "velocity_constraints": "velocity-constraints.txt",
    "mesh": "mesh-3d.txt",
    "particles": "particles-3d.txt"
  },
  "materials": [
    {
      "id": 0,
      "density": 1000.0,
      "poisson_ratio": 0.495,
      "type": "LinearElastic3D",
      "youngs_modulus": 100000000.0
    },
    {
      "id": 1,
      "density": 2300.0,
      "poisson_ratio": 0.25,
      "type": "LinearElastic3D",
      "youngs_modulus": 1500000.0
    }
  ],
  "mesh": {
    "cell_type": "SFH8",
    "material_id": 1,
    "mesh_reader": "Ascii3D",
    "node_type": "N3D",
    "particle_type": "P3D"
  },
  "analysis": {
    "dt": 0.001,
    "nsteps": 10,
    "gravity": [
      0.0,
      0.0,
      -9.81
    ]
  },
  "post_processing": {
    "output_steps": 10,
    "path": "results/"
  }
}
```

## Ascii files
### Mesh

The ASCII mesh has the following format:

```
nnodes 	ncells
# nodal coordinates
x_0 	y_0 	z_0
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

`nnz` is the number of nodes.

`ncells` the number of cells.
 
$x_i$, $y_i$, $z_i$ correspond to the Cartesian coordinates of each node. 

Each node will be assigned a unique id from `0` to `nnodes -1`, and will be assigned in the 
order in which they appear. 

`ncells` refers to the number of nodes per element. 


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

### Velocity constraints

Velocity constraints at each node can be specified in the following format:

```
n_0     d_1     v_1
n_1     d_0     v_0
...
...
n_i     d_1     v_1
...
...
n_n     d_2     v_2
```

where, 

`n_i` is the node number.

`d_i` is the direction number `(0|1|2)` that corresponds to a cartesian direction, typically `(x|y|z)`.

`v_i` is the specified velocity in direction `d_i`.


### Material points

The material points file has the following format:

```
# material point coordinates
x_0	y_0 	z_0
x_1	y_1 	z_1
...
x_i	y_i	z_i
...
x_n	y_n	z_n 
```

$x_i$, $y_i$, $z_i$ correspond to the Cartesian coordinates of each material point. The material points are assigned a unique id from 0 to `n - 1`.

