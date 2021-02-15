# Frontera

Frontera is a high performance computing system deployed at TACC (Texas Advanced Computing Center). More information about the system configuration and usage can be accessed in the [Frontera User Guide](https://portal.tacc.utexas.edu/user-guides/frontera).

## Accessing the system

To access Frontera, it is recommended to create a [design safe account](https://www.designsafe-ci.org/account/register/), as it offers other facilities in addition to HPC access. Upon registering, the system can be accessed by using a SSH (Secure Shell) client, which is done by using the following command:


```shell
ssh taccuserid@frontera.tacc.utexas.edu
```

*(taccuserid is the user id selected for registrering in the design safe website)*

Please enable [2FA (Two-factor authentication)](https://portal.tacc.utexas.edu/tutorials/multifactor-authentication) in your TACC account. Upon successful connection via SSH, an access to a login node will be granted. The login node is meant to perform file management, editing and compiling actions, it must not be used for running the code. To run the code, the user has two options: run on the compute nodes via an interactive session with an `idev` command, typically used for code development, or by submitting a batch job. Additionally, it is recommended that the user submit the jobs from the `$WORK` or `$SCRATCH` environments, instead of the `$HOME`.

## Installing prerequisites

Certain prerequisites such as `boost` and `hdf5` are available on TACC, and can be accessed using `module load` command. Additional dependency of `eigen` must be installed locally:


```shell
module load boost hdf5
```

> Eigen

```shell
cd $WORK
git clone https://gitlab.com/libeigen/eigen.git
```

> KaHIP for domain decomposition

```shell
cd $WORK && git clone https://github.com/KaHIP/KaHIP && \
   cd KaHIP && sh ./compile_withcmake.sh 
```

## Get the code to Frontera

The `git clone` command can be used directly in the login node to clone the mpm repository into the Frontera.

```shell
cd $WORK
git clone https://github.com/cb-geo/mpm.git
```

To clone the mpm benchmark repository:

```shell
git clone https://github.com/cb-geo/mpm-benchmarks.git
```

## Compile on Frontera with VTK

Please use the intel compiler on Frontera. To build the Make file, the procedure is similar to running the mpm on a local machine where the user also creates a build directory. However, the cmake command used is:

```shell
export CC=icc
export CXX=icpc
mkdir build && cd build && cmake -DBOOST_INCLUDE_DIRS=$TACC_BOOST_INC -DCMAKE_BUILD_TYPE=Release -DEIGEN3_INCLUDE_DIR=$WORK/eigen -DKAHIP_ROOT=$WORK/KaHIP -DVTK_DIR=/work/01197/semeraro/frontera/VTK/VTKBinary/ ..

make -j
```

## Single installation and compile script
```shell
module load boost hdf5
cd $WORK && git clone https://gitlab.com/libeigen/eigen.git
cd $WORK && git clone https://github.com/KaHIP/KaHIP && \
   cd KaHIP && sh ./compile_withcmake.sh 
git clone https://github.com/cb-geo/mpm-benchmarks.git
git clone https://github.com/cb-geo/mpm.git && cd mpm
export CC=icc
export CXX=icpc
mkdir build && cd build &&  cmake -DBOOST_INCLUDE_DIRS=$TACC_BOOST_INC -DCMAKE_BUILD_TYPE=Release -DEIGEN3_INCLUDE_DIR=$WORK/eigen -DKAHIP_ROOT=$WORK/KaHIP -DVTK_DIR=/work/01197/semeraro/frontera/VTK/VTKBinary/ ..
make -j
```
