# Build

To compile CB-Geo MPM please make sure you have the following packages. The MPM code is written in C++14 and compiles successfully on GCC 8.x and Clang 6.x.

## Prerequisites
The following additional packages are required to compile the MPM code.

* [Boost](http://www.boost.org/)
* [Eigen](http://eigen.tuxfamily.org/)
* [Intel TBB](https://www.threadingbuildingblocks.org/)
* [HDF5](https://support.hdfgroup.org/HDF5/)
* [VTK](https://www.vtk.org/)

### Fedora (Recommended)
> 28

Please run the following command:

```shell
dnf install -y boost boost-devel clang cmake cppcheck eigen3-devel findutils gcc gcc-c++ \
               git hdf5 hdf5-devel kernel-devel lcov make openmpi openmpi-devel tar \
	       tbb tbb-devel valgrind vim vtk vtk-devel wget
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
