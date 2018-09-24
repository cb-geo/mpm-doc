# VTK

When the CB-Geo mpm code is compiled with VTK libraries, the MPM code can be set to write VTK data of partices at a specified output frequency. The input JSON configuration takes as optional `vtk` argument. The following attributes are valid options for VTK: `"stresses`, `strains`, and `velocities`. When the attribute `vtk` is not specified or an incorrect argument is defined, the code will write all available options.

```JSON
  "post_processing": {
    "output_steps": 5,
    "vtk": ["stresses", "strains", "velocities"],
    "path": "results/"
  }
```

