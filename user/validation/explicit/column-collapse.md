# Column Collapse

In 

## Hydrostatic Analytical Solution

Given the material points cannot move horizontally, the hydrostatic column collapse problem should yield condition. 


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
|x-spacing 		| 0.02 $m$ 	|
|y-spacing 		| 0.02 $m$ 	|
|Particles per cell |  25  |


### Analysis

|Description		| value		|
|-----------------------|---------------|
|Total analysis time 	| 0.1 s		|
|Gravity		| -9.81 $m/s^2$		|

### Material

|Description		| value		|
|-----------------------|---------------|
|Material	                          | Bingham |
|Density ($\rho$) 		              | 1800.0 $kg/m^3$ |
|Young's modulus ($E$)	              | 1000000 $N/m^2$	|
|Yield stress ($\tau_0$)              | 20.0     |
|Viscosity ($\mu$)                    | 25.0     |
|Critical shear rate ($\dot{\gamma}$) |  0.0     | 


## Hydrostatic Analysis

Analysis are carried out using MPM Explicit USF and USL algorithms. Note that the material position is updated using nodal acceleration.

### Cases

|Description		 | Case I	| Case I	|
|------------------------|--------------|---------------|
|Poisson ratio ($\nu$)   | 0.0		 | 0.3		 |

## Results
### USF Results at 0.1s

| Parameter				| Analytical	| Case I	| Case II 	|
|---------------------------------------|---------------|---------------|---------------|
|$\sigma_{yy} (N/m^2)$			| -1730.484		|-0.982638	|-0.983478	|
|$\sigma_{xx} (N/m^2)$          |     0.00		| 0.043406	| 0.041306	|



### USL Results at 0.1s


| Parameter				| Analytical	| Case I	| Case II 	|
|---------------------------------------|---------------|---------------|---------------|
|$\sigma_{yy} (N/m^2)$			| -1730.484		|-0.982638	|-0.983478	|
|$\sigma_{xx} (N/m^2)$          |     0.00		| 0.043406	| 0.041306	|

