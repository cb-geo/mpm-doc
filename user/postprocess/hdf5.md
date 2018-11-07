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
'stress_xx', 'stress_yy', 'stress_zz', 'tau_xy', 'tau_yz', 'tau_xz', 
'strain_xx', 'strain_yy', 'strain_zz', 'gamma_xy', 'gamma_yz', 'gamma_xz', 'epsilon_v', 'status']
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

## Partitioned HDF5

When running MPM on multiple nodes, the CB-Geo MPM code currently outputs files split based on their MPI rank. Each file is named as `attribute-mpirank_mpisize-01.h5` to read from all Particle HDF5 file:

```python
# Read partitioned HDF5 data
# !pip3 install pandas
import pandas as pd
# Number of MPI tasks
mpi = 4
# Create empty data frame
df = pd.DataFrame(index=range(0))
# Iterate over different files from MPI and append to data frame
for i in range(mpi):
    file = 'particles-'+str(i)+'_'+str(mpi)+'-09.h5'
    df = df.append(pd.read_hdf(file, 'table'))
print(df[['id', 'stress_xx', 'stress_yy','strain_xx', 'strain_yy', 'pressure']])
```
