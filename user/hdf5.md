# HDF5

The CB-Geo mpm code writes HDF5 data of partices at each output time step. The HDF5 data can be read using Python / Pandas. If `pandas` package is not installed, run `pip3 install pandas`. 

To read a particles HDF5 data, for example `particles00.h5` at step 0:

```python
# Read HDF5 data
# !pip3 install pandas
import pandas as pd
df = pd.read_hdf('particles00.h5', 'table')
# Print column headers
print(list(df))
```

The particles HDF5 data has the following variables stored in the dataframe:

```
['id', 'coord_x', 'coord_y', 'coord_z', 'velocity_x', 'velocity_y', 'velocity_z', 
'stress_xx', 'stress_yy', 'stress_zz', 'tau_xy', 'tau_yz', 'tau_xz', 'status']
```

Each item in the header can be used to access data in the `h5` file. To print velocities (x, y, and z) of the particles:

```python
# Print all velocities
print(df[['velocity_x', 'velocity_y','velocity_z']])
```

```
   velocity_x  velocity_y  velocity_z
0         0.0         0.0    0.016667
1         0.0         0.0    0.016667
2         0.0         0.0    0.016667
3         0.0         0.0    0.016667
4         0.0         0.0    0.033333
5         0.0         0.0    0.033333
6         0.0         0.0    0.033333
7         0.0         0.0    0.033333
```
