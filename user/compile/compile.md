# Build

To compile the CB-Geo MPM code please make sure you have the following packages. The CB-Geo MPM code is written in C++14 and compiles successfully on GCC 8.x and Clang 6.x.

## Prerequisites
The following additional packages are required to compile the MPM code.

* [Boost](http://www.boost.org/)
* [Eigen](http://eigen.tuxfamily.org/)
* [Intel TBB](https://www.threadingbuildingblocks.org/)
* [HDF5](https://support.hdfgroup.org/HDF5/)

### Optional
* [MPI](https://www.open-mpi.org/)
* [VTK](https://www.vtk.org/)

### Fedora (Recommended)
> 28

Please run the following command:

```shell
dnf install -y boost boost-devel clang cmake cppcheck eigen3-devel findutils gcc gcc-c++ \
               git hdf5 hdf5-devel hdf5-openmpi hdf5-openmpi-devel kernel-devel lcov\
               make openmpi openmpi-devel sqlite sqlite-devel tar tbb tbb-devel valgrind vim \
               voro++ voro++-devel vtk vtk-devel wget
```

### Ubuntu 
> 18.04

```shell
sudo apt-get install -y cmake gcc git libboost-all-dev libeigen3-dev libhdf5-dev libtbb-dev libvtk7-dev
```

### Docker

Alternatively the [CB-Geo MPM docker image](/docker) can be also used, which comes pre-packaged with relevant libraries.

## Compile

0. Run CMake to create make files. `mkdir build && cd build && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=g++ ..`. Here `..` refers to the path to the `CMakeLists.txt` file.

1. Run `make clean && make -jN` (where N is the number of cores).

### Run tests

0. Run `./mpmtest -s` (for a verbose output) or `ctest -VV`.


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
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=mpicxx -DCMAKE_EXPORT_COMPILE_COMMANDS=On ..
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

