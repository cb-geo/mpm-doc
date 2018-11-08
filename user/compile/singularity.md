# Singularity

The CB-Geo MPM code is also available as a Singularity container, which can be used to run on HPC systems.

## Prerequisites

* Please ensure you have [Singularity](https://sylabs.io/singularity).

## Running the container

* Check if `singulartiy` is available on your HPC: `module av singularity` and load the Singularity module using `module load singularity`.

* The Singularity image for the CB-Geo MPM code is available at [`library://cbgeo/mpm/mpm`](https://cloud.sylabs.io/library/cbgeo/mpm) and can be pulled using `singularity pull library://cbgeo/mpm/mpm` this requires version 3 of Singularity.

* To run the Singularity CB-Geo MPM container `singularity run mpm.img -f /path/to/working/dir`. The results will be written to working dir.
