# Docker

An easy way to run the MPM is to use our prebuilt, high-performance Docker images. This documentation explains how to get quickly started with using MPM in Docker, as well as how to take advantage of more advanced features of Docker. [Welcome docs on Docker](https://doc.cb-geo.com/docker/docker.html) covers further information on starting and stopping containers, sharing volume, etc.

## Prerequisites

* Please ensure you have sudo or root access and install [Docker](https://docs.docker.com/engine/installation/).

## Running the container

* Check if `docker` service is running: `systemctl status docker`.

* On RedHat based linux distros, you can start the docker service using `systemctl start docker`.

* Docker requires elevated previleges, ensure you are running docker as a sudoer or root.

* Pull the latest version of the MPM container with all prerequisites: `docker pull quay.io/cbgeo/mpm`. This will download the latest version of the MPM container.

* Check if the MPM container image is available on your system: `docker images`.

* Run the MPM docker container: `docker run -it quay.io/cbgeo/mpm:latest /bin/bash`. This will launch the MPM container.

* Clone the [MPM repository](https://github.com/cb-geo/mpm): `git clone https://github.com/cb-geo/mpm.git` or if you have a SSH key `git clone git@github.com:cb-geo/mpm.git`. The MPM code will be now available at `/home/cbgeo/research/mpm`.

* From the `mpm` directory, compile the source code using: `mkdir build && cd build &&  cmake -DCMAKE_BUILD_TYPE=Release ..`

## Sharing files between host and container


* To share a folder or a volume between the host (local machine) and the docker container:

```
docker run -it -v $(pwd):/home/cbgeo/research/mpm-shared/ quay.io/cbgeo/mpm:latest /bin/bash
```

> Users running Linux distributions with SELinux enabled (Redhat, CentOS, Fedora, and others) will need to add the `:z` option to all subsequent host volume mounts `-v`.

```
docker run -it -v $(pwd):/home/cbgeo/research/mpm-shared/:z quay.io/cbgeo/mpm:latest /bin/bash
```
