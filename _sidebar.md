<!-- docs/_sidebar.md -->

* User documentation

  * [About](user/about.md)
  * [Compile](user/compile/compile.md)
  * [Spack](user/compile/spack.md)
  * [Docker](user/compile/docker.md)
  * [Singularity](user/compile/singularity.md)
  * Preprocess
    * [Input JSON](user/preprocess/input.md)
    * [ASCII Mesh/Particles](user/preprocess/ascii-mesh-particles.md)
    * [Entity Sets](user/preprocess/entity-sets.md)
  * Run MPM
    * [Local](user/run/local.md)
    * [TACC Stampede 2](user/run/hpc/tacc-stampede2.md)
    * [TACC Frontera](user/run/hpc/tacc-frontera.md)    
  * Postprocess
    * [HDF5 data](user/postprocess/hdf5.md)
    * [VTK](user/postprocess/vtk.md)
    * [Rendering](user/postprocess/render.md)
  * Validation
    * Explicit
      * [Uniaxial stress](user/validation/explicit/uniaxial-stress/uniaxial-stress.md)
      * [Hydrostatic column](user/validation/explicit/hydrostatic-column/hydrostatic-column.md)
      * [Plate with a hole](user/validation/explicit/plate-hole/plate-hole.md)
      * [Plate with a hole (isoparametric)](user/validation/explicit/plate-hole-iso/plate-hole-iso.md)

* Theory

  * [About](theory/about.md)
  * Continuum mechanics
    * [Strains](theory/continuum-mechanics/strain.md)
  * Geometry
    * [Rotation matrices](theory/geometry/rotation-matrices.md)
  * [MPM](theory/mpm.md)
    * [MPM Explicit](theory/mpm-explicit.md)
      * [Update Stress First](theory/usf.md)
      * [Update Stress Last](theory/usl.md)
  * Material
    * [LinearElastic](theory/material/linear-elastic.md)
    * [Bingham](theory/material/bingham.md)
    * [Newtonian](theory/material/newtonian.md)
    * [MohrCoulomb](theory/material/mohr-coulomb.md)
    * [ModifiedCamClay](theory/material/modified-cam-clay.md)
    * [NorSand](theory/material/norsand.md)
  * [Contact](theory/contact.md)

* Code
  * [Overview](code/overview.md)
  * [Material](code/material/material.md)

* Developer
  * [Getting started](developer/getting-started.md)
  * [CB-Geo developer workflow](developer/workflow.md)
  * [CB-Geo git guidelines](developer/git-guidelines.md)
