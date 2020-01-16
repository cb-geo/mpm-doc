# Build

To compile the CB-Geo MPM code please make sure you have the following packages. The CB-Geo MPM code is written in C++14 and compiles successfully on GCC 8.x and Clang 6.x.

## Prerequisites
The following additional packages are required to compile the MPM code.

* [Boost](http://www.boost.org/)
* [Eigen](http://eigen.tuxfamily.org/)
* [Intel TBB](https://www.threadingbuildingblocks.org/)
* [HDF5](https://support.hdfgroup.org/HDF5/)

#### Optional
* [MKL](https://software.intel.com/en-us/mkl)
* [MPI](https://www.open-mpi.org/)
* [KaHIP](https://github.com/schulzchristian/KaHIP)
* [Partio](https://github.com/wdas/partio)
* [VTK](https://www.vtk.org/)


### Fedora (Recommended)
> 28

Please run the following command:

```shell
dnf install -y boost boost-devel clang clang-analyzer clang-tools-extra cmake cppcheck dnf-plugins-core \
               eigen3-devel findutils freeglut freeglut-devel gcc gcc-c++ git hdf5 hdf5-devel \
               kernel-devel lcov libnsl make ninja-build openmpi openmpi-devel tar tbb tbb-devel \
               valgrind vim vtk vtk-devel wget
```

### Ubuntu 
> 18.04

Please run the following commands to install any updates:

```
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install 

sudo apt-get autoremove

```

To install dependencies

```shell
sudo apt-get install -y cmake gcc git libboost-all-dev libeigen3-dev libhdf5-serial-dev libopenmpi-dev libtbb-dev libvtk7-dev ninja-build
```

### KaHIP installation for domain decomposition [optional]
> Required if you are using MPI

```shell
cd ~/workspace/ && git clone https://github.com/schulzchristian/KaHIP && \
   cd KaHIP && sh ./compile_withcmake.sh
```


### Partio for Houdini SFX Visualization [optional]

```shell
sudo dnf install -y libnsl freeglut freeglut-devel
mkdir -p ~/workspace && cd ~/workspace/ && git clone https://github.com/wdas/partio.git && \
    cd partio && cmake . && make
```

Houdini supported (*.bgeo) files will be generated. These can be rendered using the non-commercial [Houdini Apprentice](https://www.sidefx.com/download/).


## Get the code

* Download the `mpm` code repository using git clone.

```shell
git clone https://github.com/cb-geo/mpm
```

## Compile

0. Navigate to the `mpm` repository, which was just cloned (`cd mpm`). Then run `CMake` to create make files. `mkdir build && cd build && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=g++ ..`. Here `..` refers to the path to the `CMakeLists.txt` file.

1. Run `make clean && make -jN` (where N is the number of cores).

### Run tests

0. Run `./mpmtest -s` (for a verbose output) or `ctest -VV`.

## Compile using Ninja build system

0. Run `mkdir build && cd build && cmake -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=g++ ..`.

1. Run `ninja`


## Compile with MPI (Running on a cluster)

The CB-Geo MPM code can be compiled with `MPI` to distribute the workload across compute nodes in a cluster.

Additional steps to load `OpenMPI` on Fedora:

```
source /etc/profile.d/modules.sh
export MODULEPATH=$MODULEPATH:/usr/share/modulefiles
module load mpi/openmpi-x86_64
```

Compile with OpenMPI:

```
mkdir build && cd build 
export CXX_COMPILER=mpicxx
cmake -DCMAKE_BUILD_TYPE=Release ..
make -jN
```

Additionally, you need to specify path to KaHIP if it is not in the system location.
```
-DCMAKE_EXPORT_COMPILE_COMMANDS=On -DKAHIP_ROOT=/path/to/kahip/
```

It will look like

```
mkdir build && cd build 
export CXX_COMPILER=mpicxx
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_EXPORT_COMPILE_COMMANDS=On -DKAHIP_ROOT=/path/to/kahip/ ..
make -jN
```


### Run with MPI

To run the CB-Geo MPM code on a cluster with MPI:

```
mpirun -N <#-MPI-tasks> ./mpm -f /path/to/input-dir/ -i mpm.json
```

For example to run the code on 4 compute nodes:

```
mpirun -N 4 ./mpm -f ~/benchmarks/3d/uniaxial-stress -i mpm.json
```


### Compile with Partio viz support

Please include `-DPARTIO_ROOT=/path/to/partio/` in the cmake command. A typical cmake command would look like `cmake -DCMAKE_BUILD_TYPE=Release -DPARTIO_ROOT=~/workspace/partio/ ..`
