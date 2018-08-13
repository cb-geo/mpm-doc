# Preprocessing

## Input JSON
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
    "cell_type": "ED3H8",
    "material_id": 1,
    "mesh_reader": "Ascii3D",
    "node_type": "N3D",
    "particle_type": "P3D"
  },
  "analysis": {
    "dt": 1.0E-5,
    "nsteps": 10,
    "resume" : {
      "resume": true,
      "uuid": "restart",
      "step" : 5
    },
    "gravity": [0.0, 0.0, -9.81]
  },
  "post_processing": {
    "output_steps": 5,
    "path": "results/"
  }
}
```

### Analysis

The analysis object defines the type of analysis, number of steps, time-step, and an optional resume support.

```
  "analysis": {
    "dt": 1.0E-5,
    "nsteps": 10,
    "gravity": [0.0, -9.81, 0.0],
    "resume" : {
      "resume": true,
      "uuid": "restart",
      "step" : 5
    }
  }
```

#### Resume [optional]

The CB-Geo mpm code allows for an optional resume at a check-point support. To resume an analysis at a give time-step, please set the option `resume` to `true`, the analysis `uuid` to which to resume from has to be assigned, and the `step` from which to resume. 

