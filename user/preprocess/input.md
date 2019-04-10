# Preprocessing

## Input JSON
The CB-Geo MPM code uses a `JSON` file for input configuration.

```JSON
{
  "title": "Example JSON Input for 3D MPM",
  "input_files": {
    "mesh": "mesh-3d.txt",
    "particles": "particles-3d.txt",
    "velocity_constraints": "velocity-constraints.txt",
    "nodal_tractions": "nodal-tractions.txt",
    "particles_volumes" : "particles-volumes.txt",
    "particles_tractions": "particles-tractions.txt",
    "particles_stresses": "particles-stresses.txt",
    "particles_cells": "particles-cells.txt"
  },
  "materials": [
    {
      "id": 0,
      "density": 1000.0,
      "poisson_ratio": 0.495,
      "type": "LinearElastic3D",
      "youngs_modulus": 1.0E+08
    },
    {
      "id": 1,
      "density": 2300.0,
      "poisson_ratio": 0.25,
      "type": "LinearElastic3D",
      "youngs_modulus": 1.5E+06
    }
  ],
  "mesh": {
    "isoparametric": false,
    "check_duplicates": false,
    "cell_type": "ED3H8",
    "generate_particles_cells": 1,
    "mesh_reader": "Ascii3D",
    "node_type": "N3D",
  },
  "particle": {
    "material_id": 0,
    "particle_type": "P3D"
  },
  "analysis": {
    "type": "MPMExplicitUSF3D",
    "velocity_update", true,
    "dt": 1.0E-5,
    "uuid": "usf-axial-loading-5cb93af"
    "nsteps": 10,
    "resume" : {
      "resume": true,
      "uuid": "usf-axial-loading-5cb93af",
      "step" : 5
    },
    "gravity": [0.0, 0.0, -9.81]
  },
  "post_processing": {
    "output_steps": 5,
    "vtk": ["stresses", "strains", "velocities"],
    "path": "results/"
  }
}
```
### Input files

The `input_files` object define the location of various optional and required input files:
```
  "input_files": {
    "mesh": "mesh-3d.txt",
    "particles": "particles-3d.txt",
    "velocity_constraints": "velocity-constraints.txt",
    "particles_volumes" : "particles-volumes.txt",
    "particles_tractions": "particles-tractions.txt",
    "particles_stresses": "particles-stresses.txt",
    "particles_cells": "particles-cells.txt"
  }
```

|File					| Description				|
|---------------------------------------|---------------------------------------|
|mesh					| Nodal coordinates and cell node ids	|
|particles				| Particle coordinates			|
|velocity_constraints (optional) 	| Velocity constraints on the nodes	|
|particles_volumes (optional) 		| Particle volumes			|
|particles_tractions (optional) 	| Traction applied on the particles	|
|particles_stresses (optional) 		| Initial stresses of the particles	|
|particles_cells (optional) 		| Initial guess of particle location	|



### Analysis

The `analysis` object defines the type of analysis, number of steps, time-step, and an optional resume support.

```
  "analysis": {
    "type": "MPMExplicitUSF3D",
    "velocity_update", true,
    "dt": 1.0E-5,
    "nsteps": 10,
    "uuid": "usf-axial-loading-5cb93af",
    "gravity": [0.0, -9.81, 0.0],
    "resume" : {
      "resume": true,
      "uuid": "usf-axial-loading-5cb93af",
      "step" : 5
    }
  }
```

The CB-Geo MPM currently supports 2D and 3D explicit analysis. An analysis option can be selected by passing a required `-a` command to the mpm executable.

Supported analyses are:

|Analysis		| Description				|
|-----------------------|---------------------------------------|
|MPMExplicitUSF2D	| Explicit 2D MPM Update Stress First	|
|MPMExplicitUSF3D	| Explicit 3D MPM Update Stress First	|
|MPMExplicitUSL2D 	| Explicit 2D MPM Update Stress Last	|
|MPMExplicitUSL3D 	| Explicit 3D MPM Update Stress Last	|


#### Velocity update [optional]

In explicit code, the `velocity_update` flag allows to switch between updating particle velocity based on nodal acceleration (default, when `velocity_update` is set to `false`) and to use nodal velocity when set to `true`.

#### Resume [optional]

The CB-Geo mpm code allows for an optional resume at a check-point support. To resume an analysis at a give time-step, please set the option `resume` to `true`, the analysis `uuid` to which to resume from has to be assigned, and the `step` from which to resume. 

