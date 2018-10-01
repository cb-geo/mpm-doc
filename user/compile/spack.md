# Spack

You can also use [Spack](https://spack.io/) to install dependencies and the CB-Geo MPM code. 

## Install Spack locally

```shell
git clone https://github.com/spack/spack.git
. spack/share/spack/setup-env.sh
```

## Installing dependencies with spack

```shell
spack install boost+filesystem
spack install eigen
spack install tbb
spack install hdf5+hl
```

### To load dependencies

Once the dependencies are installed locally using Spack. You can use `spack load` or `module load` command to load installed dependencies.

## Clone and run the mpm code

Clone and run the MPM code as discussed in the compile section.

# Install the CB-Geo mpm using Spack [optional]

## Create a local spack repo
```shell
spack repo create $HOME/myspack; spack repo add $HOME/myspack
```

## Create an mpm package

```
spack create github:cb-geo/mpm.git -n mpm -t cmake -r myspack
```

Replace the mpm/package.py file with
```python
from spack import *

class Mpm(CMakePackage):
    """CB-Geo Material Point Method"""

    #homepage = "https://www.cb-geo.com/research/mpm"
    version('develop', git='https://github.com/cb-geo/mpm.git', preferred=True)

    depends_on('opengl')
    depends_on('boost+filesystem')
    depends_on('tbb')
    depends_on('hdf5+hl')

    def cmake_args(self):
        args = ["-DCMAKE_EXPORT_COMPILE_COMMANDS=On -DENABLE_COVERAGE=Off"]
        return args
```

Run `spack spec -I mpm` to check if `spack` has picked up the required mpm packages. The specification file for the MPM code can be edited by typing `spack edit mpm` once you have a `mpm/package.py` file in the `myspack` repo.

To compile install the code use `spack install mpm`. 
