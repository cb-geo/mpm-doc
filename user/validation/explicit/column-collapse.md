# Column Collapse



## Hydrostatic Analytical Solution

Given the material points cannot move horizontally, the hydrostatic column collapse problem should yield hydrostatic condition. We expect no deviatoric stress component in hydrostatic condition and thus Bingham fluid model will give the same pressure for all normal stress directions ($\sigma_{xx}, \sigma_{yy}, \sigma_{zz}$).


![column collapse](columncollapse.png)
*Figure illustrating the hydrostatic column collapse. w = 0.2 m and h = 0.1 m. All three sides (left, bottom and right) are normally fixed*


## MPM configuration

### Mesh

|Cell dimensions	| value		|
|-----------------------|---------------|
|x-length 		| 0.01 $m$ 	|
|y-length 		| 0.01 $m$ 	|

### Particles

|Particle spacings	| value		|
|-----------------------|---------------|
|x-spacing 		| 0.002 $m$ 	|
|y-spacing 		| 0.002 $m$ 	|
|Particles per cell |  25  |


### Analysis

|Description		| value		|
|-----------------------|---------------|
|Total analysis time 	| 0.1 s		|
|Gravity		| -9.81 $m/s^2$		|

### Material

|Description		| value		|
|-----------------------|---------------|
|Material	                          | Newtonian |
|Density ($\rho$) 		              | 1800.0 $kg/m^3$ |
|Young's modulus ($E$)	              | 1000000 $N/m^2$	|
|Viscosity ($\mu$)                    |  0.0     |


## Hydrostatic Analysis

Analysis are carried out using MPM Explicit USF and USL algorithms.

### Cases

Case I: Velocity update
Case II: Acceleration update

## Results
### USF Results at 0.1s

| Parameter				| Analytical	| Case I	| Case II 	|
|---------------------------------------|---------------|---------------|---------------|
|$\sigma_{yy} (N/m^2)$			| -1730.484		| -1680.244	|  |
|$\sigma_{xx} (N/m^2)$          | -1730.484		| -1680.244	|  |



### USL Results at 0.1s


| Parameter				| Analytical	| Case I	| Case II 	|
|---------------------------------------|---------------|---------------|---------------|
|$\sigma_{yy} (N/m^2)$			| -1730.484		| -1680.182	|   |
|$\sigma_{xx} (N/m^2)$          | -1730.484		| -1680.182	| 	|

