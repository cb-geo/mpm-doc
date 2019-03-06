# Lonestar 5

Lonestar 5 (LS5) is a high performance computing system deployed at TACC (Texas Advanced Computing Center). More information about the system configuration and usage can be accessed in the [Lonestar 5 User Guide](https://portal.tacc.utexas.edu/user-guides/lonestar5).

## Accessing the system

To access Lonestar 5, it is recommended to create a [design safe account](https://www.designsafe-ci.org/account/register/), as it offers other facilities in addition to HPC access. Upon registering, the system can be accessed by using a SSH (Secure Shell) client, which is done by using the following command:


```shell
ssh taccuserid@ls5.tacc.utexas.edu
```

*(taccuserid is the user id selected for registrering in the design safe website)*

Please enable [2FA (Two-factor authentication)](https://portal.tacc.utexas.edu/tutorials/multifactor-authentication) in your TACC account. Upon successful connection via SSH, an access to a login node will be granted. The login node is meant to perform file management, editing and compiling actions, it must not be used for running the code. To run the code, the user has two options: run on the compute nodes via an interactive session with an `idev` command, typically used for code development, or by submitting a batch job. Additionally, it is recommended that the user submit the jobs from the `$WORK` or `$SCRATCH` environments, instead of the `$HOME`.

## Installing prerequisites

Certain prerequisites such as `boost` and `hdf5` are available on TACC, and can be accessed using `module load` command. Additional dependency of `eigen` must be installed locally:

```shell
module load boost hdf5
wget http://bitbucket.org/eigen/eigen/get/3.3.7.zip
unzip 3.3.7.zip
mv eigen-eigen* eigen
```
## Cloning files to LS5

The `git clone` command can be used directly in the login node to clone the mpm repository into the LS5.

```shell
git clone https://github.com/cb-geo/mpm.git
```

To clone the mpm benchmark repository:

```shell
https://github.com/cb-geo/mpm-benchmarks.git
```

## Transfering files to LS5

To transfer files to a local machine to a login node, the user can use either `rsync` or `scp`. These commands must be used locally, for example:

```shell
rsync filename userid@ls5.tacc.utexas.edu:/path/to/project/directory/
scp filename username@ls5.tacc.utexas.edu:/path/to/project/directory/
```

For more information, visit [Lonestar 5 GUide - Transferring Files](https://portal.tacc.utexas.edu/user-guides/lonestar5#managing-transferring).

## Compile on LS5

To build the Make file, the procedure is similar to running the mpm on a local machine where the user also creates a build directory. However, the cmake command used is:

```shell
cmake -DBOOST_ROOT=$TACC_BOOST_DIR -DBOOST_INCLUDE_DIRS=$TACC_BOOST_INC -DCMAKE_BUILD_TYPE=Release -DEIGEN3_INCLUDE_DIR=$HOME/eigen ..
make -j
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
#SBATCH -J mpm            # job name
#SBATCH -o mpm.o%j        # output and error file name (%j expands to jobID)
#SBATCH -N 1              # number of nodes requested
#SBATCH -n 1               # total number of mpi tasks requested
#SBATCH -p development      # queue (partition) -- normal, development, etc.
#SBATCH -t 01:30:00         # run time (hh:mm:ss) - 1.5 hours

# Slurm email notifications are now working on Lonestar 5
#SBATCH --mail-user=userid@tacc.utexas.edu
#SBATCH --mail-type=begin   # email me when the job starts
#SBATCH --mail-type=end     # email me when the job finishes

# run the executable named a.out
ibrun ./mpm -f $WORK/benchmarks/2d/
```

Then, a job can be submitted by using the following command in the login node:

```shell
sbatch submission.txt
```

The list of submitted jobs can be viewed with `showq` (or `showq -u` if only a list of the user`s submitted jobs are required).

## Mounting a remote directory

Whenever the output files need to be accessed from the local machine, it is necessary to mount a remote directory that can access the files in the login node the user has been assigned to. This is done with:

```shell
localhost$ sshfs taccuserid@ls5.tacc.utexas.edu:/path/to/files/ ~/path/to/local/directory/
```

Unmounting the remote directory can be done with `fusermount -u ~/path/to/local/directory/`.

<aside class="notice">
To view the results, the hdf5 files must be used. VTK files cannot be generated in Lonestar 5. 
</aside>
