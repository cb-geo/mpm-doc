# Input

The CB-Geo MPM code uses a `JSON` file for input configuration.

```JSON
{
  "title": "Example JSON Input for 3D MPM",
  "input_files": {
    "constraints": "mesh_constraints.txt",
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
