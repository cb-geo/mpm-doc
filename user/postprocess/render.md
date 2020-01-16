# Rendering

The CB-Geo mpm code is capable of generating Houdini compatible (*.bgeo) files for VFX rendering. This option is enabled when compiled with the partio library. Houdini Apprentice can be used to generate photo-realistic rendering of outputs.


## Install Partio

```shell
sudo dnf install -y libnsl freeglut freeglut-devel
mkdir -p ~/workspace && cd ~/workspace/ && git clone https://github.com/wdas/partio.git && \
    cd partio && cmake . && make
```

## Compile with Partio viz support

Please include `-DPARTIO_ROOT=/path/to/partio/` in the cmake command. A typical cmake command would look like `cmake -DCMAKE_BUILD_TYPE=Release -DPARTIO_ROOT=~/workspace/partio/ ..`

## Houdini rendering
The bgeo files can be rendered using the non-commercial [Houdini Apprentice](https://www.sidefx.com/download/).
