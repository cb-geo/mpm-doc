# VTK

When the CB-Geo mpm code is compiled with VTK libraries, the MPM code can be set to write VTK data of partices at a specified output frequency. The input JSON configuration takes as optional `vtk` argument. The following attributes are valid options for VTK: `"stresses`, `strains`, and `velocities`. When the attribute `vtk` is not specified or an incorrect argument is defined, the code will write all available options.

```JSON
  "post_processing": {
    "output_steps": 5,
    "vtk": ["stresses", "strains", "velocities"],
    "path": "results/"
  }
```

> When opening particle data (*.vtp) in [ParaView](https://www.paraview.org/), please use the representation `Point Gaussian` to visualise the particle data attribute.


The CB-Geo MPM code generates parallel `*.pvtp` files when the code is executed across MPI ranks. Each MPI rank will produce an attribute subdomain files, for example `stresses-0_2-100.vtp` and `stresses-1_2-100.vtp` file for stresses generated in rank 0 of 2 rank MPI processes and also a parallel `pvtp` file `stress-100.pvtp`. The parallel `*.pvtp` file combines all the VTK outputs from different MPI ranks. Use the `*.pvtp` files when visualizing results from a distributed simulation.
