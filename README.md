# py2cytoscape [![Build Status](https://travis-ci.org/cytoscape/py2cytoscape.svg?branch=master)](https://travis-ci.org/cytoscape/py2cytoscape) [![PyPI version](https://badge.fury.io/py/py2cytoscape.svg)](https://badge.fury.io/py/py2cytoscape) [![ReadtheDocs](https://readthedocs.org/projects/py2cytoscape/badge/?version=latest)](https://py2cytoscape.readthedocs.io) [![DOI](https://zenodo.org/badge/24250285.svg)](https://zenodo.org/badge/latestdoi/24250285)

## DEPRECATION

Please note that this project has been superceded by the [py4cytoscape project](https://github.com/cytoscape/py4cytoscape). py2cytoscape is not currently maintained.

## Installation

py2cytoscape can be installed using `conda`, `pip`.

### conda

`conda` installs `igraph` with py2cytoscape.
You do not need to install `igraph` by yourself.

```shell
conda install -c conda-forge py2cytoscape
```

### Latest stable release (pip)

```shell
pip3 install py2cytoscape
```

### Development version (pip)

```shell
pip3 install git+https://github.com/cytoscape/py2cytoscape.git
```

### Dependencies (extra): igraph

```
git clone https://github.com/igraph/python-igraph/
cd python-igraph

git clone https://github.com/igraph/igraph igraphcore
cd igraphcore
./bootstrap.sh
mkdir _build && cd _build
../configure --prefix=$PWD/../_install
make
make install
cd ../../

CPPFLAGS="-I$PWD/igraphcore/_install/include/igraph ${CPPFLAGS}"
export CPPFLAGS
LDFLAGS="-L$PWD/igraphcore/_install/lib ${LDFLAGS}"
export LDFLAGS
PKG_CONFIG_PATH=igraphcore/_install/lib/pkgconfig/
export PKG_CONFIG_PATH

python3 setup.py install --user
```

## Documentation

Package documentation can be found on [https://py2cytoscape.readthedocs.io](https://py2cytoscape.readthedocs.io).

For contributing please check the [wiki](https://github.com/cytoscape/py2cytoscape/wiki).

Full workflows can be found on the [cytoscape/cytoscape-automation](https://github.com/cytoscape/cytoscape-automation) repo. The following workflows include cyrest usage:

* [advanced-cancer-networks-and-data](https://github.com/cytoscape/cytoscape-automation/blob/master/for-scripters/Python/advanced-cancer-networks-and-data.ipynb)


## Contributing

Please do all your development in our development docker image: 

```
docker pull mpgagebioinformatics/py2cytoscape:latest
```

* Create a folder to map to the container's user home folder
```
mkdir -p ~/py2cy-container
```
----
* Start the container from the latest version of the image
```
sudo docker run -d -p 8787:8787 -p 8888:8888 \
-v ~/py2cy-container:/home/mpiage --name py2cy-container \
-it mpgagebioinformatics/py2cytoscape:latest
```
----
* Alternatively you can start the container from a specific tag/version of the image
```
sudo docker run -d -p 8787:8787 -p 8888:8888 \
-v ~/py2cy-container:/home/mpiage --name py2cy-container \
-it mpgagebioinformatics/py2cytoscape:<tag>
```
----
* Connect to the running container
```
sudo docker exec -i -t py2cy-container /bin/bash
```
----
* Stop the container
```
sudo docker stop py2cy-container
```
----
* Jupyter

Once you have connected to the running container you can start `jupyter` with
```
module load jupyterhub
jupyter notebook --ip=0.0.0.0
```
A URL will be presented to you, and it should be pasted into your host's browser (Chrome  recommended).

----
* RStudio-server
Once you have connected to the running container you can start `Rstudio server` with
```
module load rlang
sudo rstudio-server start
```
You can then get access by connecting on your host's browser to [http://localhost:8787](http://localhost:8787).

For stopping the server use:
```
sudo rstudio-server stop
```

----

* X forward to enable Cytoscape

On a Mac install `socat` and `xquartz`:
```
brew install socat
brew install xquartz
```
Open Xquartz:
```
open -a Xquartz
```
Then navigate to XQuartz > Preferences > Security  and tick the box 'Allow connections from network clients'.

Check your ip address:
```
IP=$(ifconfig en0 | grep inet | awk '{ print $2 }')
```
Start `socat`:
```
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
```
an then start the container by adding the `-e DISPLAY=${IP}:0` argument. 

Complete example call: 
```
IP=$(ifconfig en0 | grep inet | awk '{ print $2 }') && \
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\" & \
docker run -d -e DISPLAY=${IP}:0 -p 8787:8787 -p 8888:8888 \
-v ~/py2cy-container:/home/mpiage --name py2cy-container \
-it mpgagebioinformatics/py2cytoscape:latest
```

----
* User account

User: `mpiage`

Pass: `bioinf`


## Citing

Ono, K. et al. (2015) CyREST: Turbocharging Cytoscape Access for External Tools via a RESTful API. *F1000Res*, **4**, 478

```Note to repository maintainers: Please *DO NOT* move this page ... the Cytoscape Automation paper refers directly to it.```

