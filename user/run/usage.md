# Run MPM

The CB-Geo MPM code uses `JSON` file type for input configuration.

## Usage {docsify-ignore}
```shell
./mpm  -a <analysis> [-i <input_file>] -f <working_dir> [--] [--version]
       [-h]
```

Where:
```shell
   -a <analysis>,  --analysis <analysis>
     (required)  MPM analysis

   -i <input_file>,  --input_file <input_file>
     Input JSON file [mpm.json]

   -f <working_dir>,  --working_dir <working_dir>
     (required)  Current working folder

   --,  --ignore_rest
     Ignores the rest of the labeled arguments following this flag.

   --version
     Displays version information and exits.

   -h,  --help
     Displays usage information and exits.
```

### Analysis

The CB-Geo MPM currently supports 2D and 3D explicit analysis. An analysis option can be selected by passing a required `-a` command to the mpm executable.

Supported analysis:

|Analysis		| Description				|
|-----------------------|---------------------------------------|
|MPMExplicitUSF2D	| Explicit 2D MPM Update Stress First	|
|MPMExplicitUSF3D	| Explicit 3D MPM Update Stress First	|
|MPMExplicitUSL2D 	| Explicit 2D MPM Update Stress Last	|
|MPMExplicitUSL3D 	| Explicit 3D MPM Update Stress Last	|

