# Singularity

The CB-Geo MPM code is also available as a Singularity container, which can be used to run on HPC systems.

## Prerequisites

* Please ensure you have [Singularity](https://sylabs.io/singularity).

## Running the container

* Check if `singulartiy` is available on your HPC: `module av singularity` and load the Singularity module using `module load singularity`.

* The Singularity image for the CB-Geo MPM code is available at [`library://cbgeo/mpm/mpm`](https://cloud.sylabs.io/library/cbgeo/mpm) and can be pulled using `singularity pull library://cbgeo/mpm/mpm` this requires version 3 of Singularity.

* Alternatively, if you have an earlier version of Singularity (version below 3.0), the CB-Geo MPM Singularity image is also available on [direct download](https://s3.eu-west-2.amazonaws.com/singularity-containers/mpm.img).

* To run the Singularity CB-Geo MPM container `singularity run mpm.img -f /path/to/working/dir`. The results will be written to working dir.
