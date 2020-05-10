# Static Analysis with PVS Studio

Download and install PVS studio: [https://www.viva64.com/en/pvs-studio-download/](https://www.viva64.com/en/pvs-studio-download/)

```
for i in $(find . -iname *.cc); do sed  -i '1i// This is an open source non-commercial project. Dear PVS-Studio, please check it.\n// PVS-Studio Static Code Analyzer for C, C++, C#, and Java: http://www.viva64.com' $i; done
for i in $(find . -iname *.h); do sed  -i '1i// This is an open source non-commercial project. Dear PVS-Studio, please check it.\n// PVS-Studio Static Code Analyzer for C, C++, C#, and Java: http://www.viva64.com' $i; done
for i in $(find . -iname *.tcc); do sed  -i '1i// This is an open source non-commercial project. Dear PVS-Studio, please check it.\n// PVS-Studio Static Code Analyzer for C, C++, C#, and Java: http://www.viva64.com' $i; done
mkdir -p build && cd build
cmake -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=mpicxx -DKAHIP_ROOT=~/workspace/KaHIP/ -DMPM_BUILD_LIB=Off -DHALO_EXCHANGE=On  .. 
pvs-studio-analyzer trace -- ninja -j12
pvs-studio-analyzer analyze -j -o PVS-Studio.log
plog-converter -t html -o PVS-Studio.html PVS-Studio.log
```
