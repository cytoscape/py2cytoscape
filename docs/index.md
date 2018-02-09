# py2cytoscape [![Build Status](https://travis-ci.org/cytoscape/py2cytoscape.svg?branch=master)](https://travis-ci.org/cytoscape/py2cytoscape) [![PyPI version](https://badge.fury.io/py/py2cytoscape.svg)](https://badge.fury.io/py/py2cytoscape) [![ReadtheDocs](https://readthedocs.org/projects/py2cytoscape/badge/?version=latest)](https:/py2cytoscape.readthedocs.io)

### What is _py2cytoscape_?
py2cytoscape is a collection of utilities to use [Cytoscape](http://www.cytoscape.org/) and [Cytoscape.js](http://js.cytoscape.org/) from Python.  Network visualization feature is still limited in Python, but with this tool, you can access both of Cytoscape and Cytoscape.js as network visualization engines for your Python code!

This package is still experimental and in alpha status.

### Background

![](http://cl.ly/Xk5o/cytoscape-flat-logo-orange-100.png)

Cytoscape is a [de-facto standard desktop application for network visualization in bioinformatics community](https://scholar.google.com/scholar?hl=en&q=cytoscape).  But actually, it is a domain-independent graph visualization software for all types of network data analysis.  We want to introduce cy2cytoscape, along with _cyREST_ and _Jupyter Notebook_, to broader data science community.

### Installation

py2cytoscape supports both Python 2.7 and 3.5.

py2cytocape depends on python-igraph and optionary depends on scipy.
(We do not include scipy to py2cytoscape prerequisite dependencies.)

You can install py2cytoscape with pip.

### Mac

```shell
pip install py2cytoscape
#if you use the scipy dependent py2cytoscape method
pip install scipy
```

### Ubuntu Linux

```shell
apt install g++ make libxml2-dev python-dev python3-dev zlib1g-dev
pip install py2cytoscape
#if you use the scipy dependent py2cytoscape method
pip install scipy
```

### Windows

To install py2cytoscape dependencies, we recommend that you use [Miniconda](http://conda.pydata.org/miniconda.html) Python package manager.

Miniconda has scipy binary package, but do not have python-igraph binary package.
So download the python-igraph whl for your Python (2 or 3, 32bit or 64bit) from [Christoph’s site](http://www.lfd.uci.edu/~gohlke/pythonlibs/#python-igraph).
And install it with `pip`.
Please install python-igraph before you install py2cytoscape, otherwise pip will try to **build** python-igraph (and will fail).

(In the case of Python3.5 64bit)

```
pip install .\python_igraph-0.7.1.post6-cp35-none-win_amd64.whl
pip install py2cytoscape
conda install scipy
```

### Features

### cyREST Wrapper (New from 0.4.0)
[cyREST](http://apps.cytoscape.org/apps/cyrest) is a language-agnostic RESTful API for [Cytoscape 3](http://www.cytoscape.org/what_is_cytoscape.html).  Of course you can drive Cytoscape by calling raw RESTful API using [requests]() or other http client library, but with this wrapper, you can significantly reduce your lines of code.

#### Example: Creating an empty network in Cytoscape from Python

##### __Without__ py2cytoscape (raw cyREST API call)

```python
# HTTP Client for Python
import requests

# Standard JSON library
import json

# Basic Setup
PORT_NUMBER = 1234
BASE = 'http://localhost:' + str(PORT_NUMBER) + '/v1/'

# Header for posting data to the server as JSON
HEADERS = {'Content-Type': 'application/json'}

# Define dictionary of empty network
empty_network = {
        'data': {
            'name': 'I\'m empty!'
        },
        'elements': {
            'nodes':[],
            'edges':[]
        }
}

res = requests.post(BASE + 'networks?collection=My%20Collection', data=json.dumps(empty_network), headers=HEADERS)
new_network_id = res.json()['networkSUID']
print('Empty network created: SUID = ' + str(new_network_id))
```

##### __With__ py2cytoscape

```python
from py2cytoscape.data.cyrest_client import CyRestClient

cy = CyRestClient()
network = cy.network.create(name='My Network', collection='My network collection')
print(network.get_id())
```

### Embedded Visualization Widget for [Jupyter Notebook](http://jupyter.org/)

![](http://cl.ly/aexk/cyjs_widget.png)

You can use Cytoscape.js network visualization widget in Jupyter Notebook. This is particulaly useful when you share your network analysis results with others.


### Data Conversion Utilities from/to [Cytoscape.js](http://js.cytoscape.org/) JSON
Cytoscape.js JSON is one of the standard data exchange formats in Cytoscape community.  py2cytoscape includes some graph data conversion utilities for popular graph analysis packages in Python.

Currently, the following graph objects are supported:

* [NetworkX](https://networkx.github.io/) - From / To Cytoscape.js JSON
* [igraph](http://igraph.org/python/) - From / To Cytoscape.js JSON
* [pandas DataFrame](http://pandas.pydata.org/) - To Cytoscape.js JSON

And these popular libraries will be supported soon:

* [Numpy adj. matrix](http://www.numpy.org/) (binary/weighted)
* [graph-tool](http://graph-tool.skewed.de/)
* [GraphX](https://spark.apache.org/graphx/)
* [GraphLab](https://github.com/dato-code/Dato-Core)
