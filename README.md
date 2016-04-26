# py2cytoscape
[![Build Status](https://travis-ci.org/idekerlab/py2cytoscape.svg?branch=develop)](https://travis-ci.org/idekerlab/py2cytoscape)

##### _Tools to use Cytoscape and Cytoscape.js from Python_

![](http://www.cytoscape.org/images/3_1_title3.png)

## Status
* 9/1/2015: Version 0.5.0 release.  View utilities added.
* 6/27/2014: Version 0.4.3 release. Minor update version for Python 3.4.x.
* 6/26/2014: Version 0.4.2 release. Confirmed to work with cyREST 1.1.0.
* 6/23/2014: Version 0.4.1 release.  Graph utility modules have been updated.
* 6/4/2014: Version 0.4.0 release.  This is still in alpha.

## What is _py2cytoscape_?
py2cytoscape is a collection of utilities to use [Cytoscape](http://www.cytoscape.org/) and [Cytoscape.js](http://js.cytoscape.org/) from Python.  Network visualization feature is still limited in Python, but with this tool, you can access both of Cytoscape and Cytoscape.js as network visualization engines for your Python code!

This package is still experimental and in alpha status.

### Background

![](http://cl.ly/Xk5o/cytoscape-flat-logo-orange-100.png)

Cytoscape is a [de-facto standard desktop application for network visualization in bioinformatics community](https://scholar.google.com/scholar?hl=en&q=cytoscape).  But actually, it is a domain-independent graph visualization software for all typs of network data analysis.  We want to introduce cy2cytoscape, along with _cyREST_ and _Jupyter Notebook_, to broader data science community.

## Installation

### Mac

```
brew install wget
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
~/Library/Python/2.7/bin/pip install py2cytoscape --user
```

### Windows

To install the latest version of py2cytoscape, try this:
(We strongly recommend that you use [Miniconda](http://conda.pydata.org/miniconda.html) Python package manager.)

```
conda install pandas networkx scipy
```
Next download **python-igraph** whl file from http://www.lfd.uci.edu/~gohlke/pythonlibs/ and

```
pip install THE_PYTHON_IGRAPH.whl
```
Finally,

```
pip install py2cytoscape
```




## Features

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
