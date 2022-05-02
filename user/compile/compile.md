# Build

To compile the CB-Geo MPM code please make sure you have the following packages. The CB-Geo MPM code is written in C++14 and compiles successfully on GCC 8.x and Clang 6.x.

### Prerequisite packages
> The following prerequisite packages can be found in the docker image:

* [Boost](http://www.boost.org/)
* [Eigen](http://eigen.tuxfamily.org/)
* [HDF5](https://support.hdfgroup.org/HDF5/)

#### Optional
* [MKL](https://software.intel.com/en-us/mkl)
* [MPI](https://www.open-mpi.org/)
* [KaHIP](https://github.com/schulzchristian/KaHIP)
* [OpenMP 5.0](https://www.openmp.org/specifications/)
* [Partio](https://github.com/wdas/partio)
* [VTK](https://www.vtk.org/)

### Fedora installation

Please run the following command:

```shell
dnf install -y boost boost-devel clang clang-analyzer clang-tools-extra cmake cppcheck dnf-plugins-core \
                   eigen3-devel findutils freeglut freeglut-devel gcc gcc-c++ git hdf5 hdf5-devel \
                   kernel-devel lcov libnsl make ninja-build openmpi openmpi-devel tar \
                   valgrind vim vtk vtk-devel wget
```

### Ubuntu installation

Please run the following commands to install dependencies:

```
sudo apt update
sudo apt upgrade
sudo apt install -y gcc g++ git cmake libboost-all-dev libeigen3-dev libhdf5-serial-dev libopenmpi-dev libomp-dev
```

If you are running Ubuntu 18.04 or below, you may want to update the GCC version to 9 to have OpenMP 5 specifications
support.

```
sudo apt install software-properties-common
sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
sudo apt install gcc-9 g++-9
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 90 --slave /usr/bin/g++ g++ /usr/bin/g++-9 --slave /usr/bin/gcov gcov /usr/bin/gcov-9

```

To install other dependencies:
> CMake 3.15
```
sudo apt-get install software-properties-common
sudo apt-add-repository 'deb https://apt.kitware.com/ubuntu/ bionic main'
sudo apt update
sudo apt upgrade
```

> OpenGL and X11:Xt
```
sudo apt-get install freeglut3-dev libxt-dev
```

> VTK
```
git clone https://gitlab.kitware.com/vtk/vtk.git VTK
cd VTK && mkdir build && cd build/
cmake -DCMAKE_BUILD_TYPE:STRING=Release ..
make -j
sudo make install
```

### Partio for Houdini SFX Visualization

```shell
sudo dnf install -y libnsl freeglut freeglut-devel
mkdir -p ~/workspace && cd ~/workspace/ && git clone https://github.com/wdas/partio.git && \
    cd partio && cmake . && make
```

Houdini supported (*.bgeo) files will be generated. These can be rendered using the non-commercial [Houdini Apprentice](https://www.sidefx.com/download/).

### KaHIP installation for domain decomposition

```shell
git clone https://github.com/kahip/kahip && cd kahip
sh ./compile_withcmake.sh
```

## Compile
> See https://mpm-doc.cb-geo.com/ for more detailed instructions. 

0. Run `mkdir build && cd build && cmake -DCMAKE_CXX_COMPILER=g++ ..`.

1. Run `make clean && make -jN` (where N is the number of cores).

> To compile without KaHIP partitioning use `cmake -DNO_KAHIP=True ..`

### Compile mpm or mpmtest

* To compile either `mpm` or `mpmtest` alone, run `make mpm -jN` or `make mpmtest -jN` (where N is the number of cores).

### Compile without tests [Editing CMake options]

To compile without tests run: `mkdir build && cd build && cmake -DMPM_BUILD_TESTING=Off  -DCMAKE_CXX_COMPILER=g++ ..`.

## Compile with MPI (Running on a cluster)

The CB-Geo mpm code can be compiled with `MPI` to distribute the workload across compute nodes in a cluster.

Additional steps to load `OpenMPI` on Fedora:

```
source /etc/profile.d/modules.sh
export MODULEPATH=$MODULEPATH:/usr/share/modulefiles
module load mpi/openmpi-x86_64
```

Compile with OpenMPI (with halo exchange):

```
mkdir build && cd build 
export CXX_COMPILER=mpicxx
cmake -DCMAKE_BUILD_TYPE=Release -DKAHIP_ROOT=~/workspace/KaHIP/ -DHALO_EXCHANGE=On ..
make -jN
```

To enable halo exchange set `-DHALO_EXCHANGE=On` in `CMake`. Halo exchange is a better MPI communication protocol, however, use this only for larger number of MPI tasks (> 4).

### Compile with Ninja build system [Alternative to Make]

0. Run `mkdir build && cd build && cmake -GNinja -DCMAKE_CXX_COMPILER=g++ ..`.

1. Run `ninja`

### Compile with Partio viz support

Please include `-DPARTIO_ROOT=/path/to/partio/` in the cmake command. A typical cmake command would look like `cmake -DCMAKE_BUILD_TYPE=Release -DPARTIO_ROOT=~/workspace/partio/ ..`
