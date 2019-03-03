# Lonestar 5

Lonestar 5 is a high performance computing system deployed at TACC (Texas Advanced Computing Center). This resource was designed for academic researches in Austin and accros Texas. For more information about the system configuration and usage can be accessed in the [Lonestar 5 User Guide](https://portal.tacc.utexas.edu/user-guides/lonestar5).

## Accessing the system

To access Lonestar 5, a [design safe account](https://www.designsafe-ci.org/account/register/) is necessary. Upon registering, the system can be accessed by using an SSH (SEcure Shell) client, which is done by using the following shell command:


```shell
localhost$ ssh taccuserid@.s5.tacc.utexas.edu
```

*(taccuserid is the user id used in the registration on the design safe website)*

A login node will be assigned to the user as soon as they access the system with the `ssh` command. Although the login node is meant to perform file management, editing and compiling actions, it must not be used for running the code. For that, the user has two options: run on the compute nodes via an interactive seesion (`idev`) or by submitting a batch job. Additionally, it is recommended that the user submit the jobs from the `$WORK` or `$SCRATCH` environments, instead of the `$HOME`.

## Setting up the environment

Prior to running the code, at login, the module command is used to set up the basic environment to run mpm. Further, eigen must also be installed in order for the user to build and compile the mpm files. All of this is done with a couple of shell commands:

```shell
login1$ module boost hdf5
login1$ wget -o eigen http://bitbucket.org/eigen/eigen/get/3.3.7.zip
```

## Building the make files

To build the Make file, the procedure is similar to running the mpm on a local machine where the user also creates a build directory. However, the cmake command used is:

```shell
login1$ cmake -DBOOST_ROOT=$TACC_BOOST_DIR -DBOOST_INCLUDE_DIRS=$TACC_BOOST_INC -DCMAKE_BUILD_TYPE=Release -DEIGEN3_INCLUDE_DIR=$HOME/eigen ..
```

## Submitting a job

To submit a job, the user must first create a file, e.g `name-of-file.sh`, with the following content:

```
#!/bin/bash
#SBATCH -J column            # job name
#SBATCH -o column.o%j        # output and error file name (%j expands to jobID)
#SBATCH -N 1              # number of nodes requested
#SBATCH -n 1               # total number of mpi tasks requested
#SBATCH -p development      # queue (partition) -- normal, development, etc.
#SBATCH -t 03:00:00         # run time (hh:mm:ss) - 1.5 hours

# Slurm email notifications are now working on Lonestar 5
#SBATCH --mail-user=toa298@tacc.utexas.edu
#SBATCH --mail-type=begin   # email me when the job starts
#SBATCH --mail-type=end     # email me when the job finishes

# run the executable named a.out
ibrun ./mpm -f ../../benchmarks/2d/
```

Then, a job can be submitted by using the following command in the login node:

```shell
login1$ sbatch name-of-file.sh
```

The list of submitted jobs can be viewed with `showq` (or `showq -u` if only a list of the user`s submitted jobs are required).

## Mounting a remote directory

Whenever the output files need to be accessed from the local machine, it is necessary to mount a remote directory that can access the files in the login node the user has been assigned to. This is done with:

```shell
localhost$ sshfs taccuserid@ls5.tacc.utexas.edu:/path/to/files/ ~/path/to/local/directory/
```

Unmounting the remote directory can be done with `fusermount -u ~/path/to/local/directory/`.