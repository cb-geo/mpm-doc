# Stampede 2

Stampede 2 ( is a high performance computing system deployed at TACC (Texas Advanced Computing Center). More information about the system configuration and usage can be accessed in the [Stampede 2 User Guide](https://portal.tacc.utexas.edu/user-guides/lonestar5).

## Accessing the system

To access Stampede 2, it is recommended to create a [design safe account](https://www.designsafe-ci.org/account/register/), as it offers other facilities in addition to HPC access. Upon registering, the system can be accessed by using a SSH (Secure Shell) client, which is done by using the following command:


```shell
ssh taccuserid@stampede2.tacc.utexas.edu
```

*(taccuserid is the user id selected for registrering in the design safe website)*

Please enable [2FA (Two-factor authentication)](https://portal.tacc.utexas.edu/tutorials/multifactor-authentication) in your TACC account. Upon successful connection via SSH, an access to a login node will be granted. The login node is meant to perform file management, editing and compiling actions, it must not be used for running the code. To run the code, the user has two options: run on the compute nodes via an interactive session with an `idev` command, typically used for code development, or by submitting a batch job. Additionally, it is recommended that the user submit the jobs from the `$WORK` or `$SCRATCH` environments, instead of the `$HOME`.

## Installing prerequisites

Certain prerequisites such as `boost` and `hdf5` are available on TACC, and can be accessed using `module load` command. Additional dependency of `eigen` must be installed locally:


```shell
cd $WORK
module load boost hdf5 qt5 vtk
export LD_LIBRARY_PATH=$SWR_LD_LIBRARY_PATH:$LD_LIBRARY_PATH
```

> Eigen

```shell
git clone https://gitlab.com/libeigen/eigen.git
```

> KaHIP for domain decomposition

```shell
cd $WORK && git clone https://github.com/KaHIP/KaHIP && \
   cd KaHIP && sh ./compile_withcmake.sh
```

## Clone MPM code to Stampede

The `git clone` command can be used directly in the login node to clone the mpm repository into the Stampede.

```shell
cd $WORK
git clone https://github.com/cb-geo/mpm.git
```

To clone the mpm benchmark repository:

```shell
git clone https://github.com/cb-geo/mpm-benchmarks.git benchmarks
```


## Compile on Stampede

Please use the intel compiler on Stampede. To build the Make file, the procedure is similar to running the mpm on a local machine where the user also creates a build directory. However, the cmake command used is:

```shell
export CC=icc
export CXX=icpc
mkdir build && cd build && cmake -DBOOST_ROOT=$TACC_BOOST_DIR -DBOOST_INCLUDE_DIRS=$TACC_BOOST_INC -DCMAKE_BUILD_TYPE=Release -DEIGEN3_INCLUDE_DIR=$WORK/eigen -DKAHIP_ROOT=$WORK/KaHIP ..

make -j8
```

### Single installation and compile script
```shell
cd $WORK
module load boost hdf5 qt5 vtk
export LD_LIBRARY_PATH=$SWR_LD_LIBRARY_PATH:$LD_LIBRARY_PATH
git clone https://gitlab.com/libeigen/eigen.git
cd $WORK && git clone https://github.com/KaHIP/KaHIP && \
   cd KaHIP && sh ./compile_withcmake.sh
cd $WORK && git clone https://github.com/cb-geo/mpm.git
git clone https://github.com/cb-geo/mpm-benchmarks.git benchmarks
export CC=icc
export CXX=icpc
cd mpm && mkdir build && cd build && cmake -DBOOST_ROOT=$TACC_BOOST_DIR -DBOOST_INCLUDE_DIRS=$TACC_BOOST_INC -DCMAKE_BUILD_TYPE=Release -DEIGEN3_INCLUDE_DIR=$WORK/eigen -DKAHIP_ROOT=$WORK/KaHIP ..
make -j8
```   



## Running the code

### Interactive session via idev

One way to run the code is by requesting an interactive session with `idev` ([Guide - idev](https://portal.tacc.utexas.edu/user-guides/lonestar5#running-idev)):

```shell
idev -m 15
```

This command provides access to a compute node via idev for 15 minutes. Default time is 30  minutes and maximum is 59 minutes.

### Submitting a job

To submit a job, the user must first create a file, e.g `submission.txt`, with the following content:

```
#!/bin/bash
#SBATCH -J mpm        # job name
#SBATCH -o mpm.o%j   # output and error file name (%j expands to jobID)
#SBATCH -N 4              # number of nodes requested
#SBATCH -n 8              # total number of mpi tasks requested
#SBATCH -p normal         # queue (partition) -- normal, development, etc.
#SBATCH -t 01:00:00       # run time (hh:mm:ss) - 1 hour
# Slurm email notifications
#SBATCH --mail-user=userid@utexas.edu
#SBATCH --mail-type=begin   # email me when the job starts
#SBATCH --mail-type=end     # email me when the job finishes
# run the executable named a.out
module load boost hdf5 vtk
ibrun ./mpm -f $WORK/mpm/benchmarks/2d/hydrostatic_column/
```

Then, a job can be submitted by using the following command in the login node:

```shell
sbatch submission.txt
```

The list of submitted jobs can be viewed with `showq` (or `showq -u` if only a list of the user`s submitted jobs are required).

> When running using MPI, the recommendation is to use twice the number of MPI tasks corresponding to the number of nodes (for e.g., set N = 4 and n = 8).

## Transfering files to Stampede

To transfer files to a local machine to a login node, the user can use either `rsync` or `scp`. These commands must be used locally, for example:

```shell
rsync filename userid@stampede2.tacc.utexas.edu:/path/to/project/directory/
scp filename username@stampede2.tacc.utexas.edu:/path/to/project/directory/
```

For more information, visit [Stampede 2 GUide - Transferring Files](https://portal.tacc.utexas.edu/user-guides/stampede2#transferring-files).

## Mounting a remote directory

Whenever the output files need to be accessed from the local machine, it is necessary to mount a remote directory that can access the files in the login node the user has been assigned to. This is done with:

```shell
localhost$ sshfs taccuserid@stampede2.tacc.utexas.edu:/path/to/files/ ~/path/to/local/directory/
```

Unmounting the remote directory can be done with `fusermount -u ~/path/to/local/directory/`.

<aside class="notice">
To view the results, the hdf5 files must be used. VTK files cannot be generated in Stampede 2. 
</aside>
