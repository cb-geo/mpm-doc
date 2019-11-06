## Entity Sets

The model can be divided into several sets of particles or nodes by using the `entity_sets.json` file. This file has the following format:

```
{
    "particle_sets": [
        {
        "id": 0,
        "set": [p0_0, ... , p0_n]
        },
        {
        "id": 1,
        "set": [p1_0, ... , p1_n]
        }
    ],
    "node_sets": [
        {
        "id": 0,
        "set": [n0_0, ... , n0_n]
        },
        {
        "id": 1,
        "set": [n1_0, ... , n1_n]
    ]
}
```

`p0_i` is the id of a particle within the set with id 0.

`n0_i` is the id of a node within the set with id 0.

Each entity (particle or node) set will be assigned a unique id and a vector with the entity's (particles or nodes) id belonging to this set. The entity's id respect the order of the entity input file -- e.g. a particle id of 3 is the fourth particle in the input file `particles.txt`.
