# Plate with a hole

A plane strip (plane stress) of width 5 m, length 8 m a centred hole of radius 0.5m is subjected to uniform tension of $sigma_0$ = 100 Pa applied at the ends of the strip. Due to symmetry, a quarter of this plate is modelled.

![Plate with a hole](plate-hole.svg)

## Howland expressions for stress concentration factors

Howland derived semi-analytical expressions for the stress concentration factors at the edge
of a symmetric hole of radius _R_ in a plate of finite width _2W_. These factors have been calcu-
lated for a range of plate geometries and are shown in the table below.


![Semi-analytical solution stress concentration](finite-width-plate-hole.png)
> Howland's semi-analytical solution

|R/W		 | Point A $\sigma_{xx}/\sigma_0$	| Point B $\sigma_{yy}/sigma_0$	|
|----------------|--------------------------------------|-------------------------------|
|0		 | 3.00					| -1.00				|
|0.1		 | 3.03					| -1.03				|
|0.2		 | 3.14					| -1.11				|
|0.3		 | 3.36					| -1.26				|
|0.4		 | 3.74					| -1.44				|
|0.5		 | 4.32					| -1.58				|

## Results

The stresses obtained from the Explicit Update Stress First simulation is shown below.

![Stress XX](plate-hole-stress-xx.png)
> Stress-XX

![Stress YY](plate-hole-stress-yy.png)
> Stress-YY
