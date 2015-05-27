# py2cytoscape: Utilities for Cytoscape and Cytoscape.js

## What is py2cytoscape?
This package is a collection of utilities to use Cytoscape and Cytoscape.js with [cyREST RESTful API app](http://apps.cytoscape.org/apps/cyrest).
This is still experimental and in alpha status.

## What's inside?

### cyREST Wrapper (New!)
[cyREST]() is a language-agnostic RESTful API for Cytoscape 3.  This package includes wrapper for the raw REST API.

### Data Conversion Utilities from/to [Cytoscape.js](http://js.cytoscape.org/) JSON.
The following libraries are supported:

* [NetworkX]() - From / To Cytoscape.js JSON
* [igraph]() - To Cytoscape.js JSON
* [GraphLab]() - To Cytoscape.js JSON (Partially supported)

And the following graph libraries will be supported soon:
* [graph-tool]()