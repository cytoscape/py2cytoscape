# py2cytoscape [![Build Status](https://travis-ci.org/cytoscape/py2cytoscape.svg?branch=master)](https://travis-ci.org/cytoscape/py2cytoscape) [![PyPI version](https://badge.fury.io/py/py2cytoscape.svg)](https://badge.fury.io/py/py2cytoscape) [![ReadtheDocs](https://readthedocs.org/projects/py2cytoscape/badge/?version=latest)](https://py2cytoscape.readthedocs.io) [![DOI](https://zenodo.org/badge/24250285.svg)](https://zenodo.org/badge/latestdoi/24250285)

## Installation

### Latest stable release

```shell
pip3 install py2cytoscape
```

### Development version

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

## Citing

Ono, K. et al. (2015) CyREST: Turbocharging Cytoscape Access for External Tools via a RESTful API. *F1000Res*, **4**, 478

```Note to repository maintainers: Please *DO NOT* move this page ... the Cytoscape Automation paper refers directly to it.```

