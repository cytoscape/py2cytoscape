## ___cyclient___

**`cyclient(host="localhost", port=1234, version="V1")`**

A CyREST client.

* **`host`** CyREST host server address. default='localhost'
* **`port`** CyREST port number. default=1234
* **`version`** CyREST version. default='v1'

* **`returns status`** a cyclient object.

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
```
___

## ___cyclient.status___

**`cyclient.status()`**

Checks the status of your CyREST server.

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.status()

CyREST online!
```
___

## ___cyclient.version___

**`cyclient.version()`**

Checks Cytoscape version.

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.version()

cytoscapeVersion 3.6.0
apiVersion v1
```
___

## ___cyclient.copy___

**`cyclient.copy()`**

Creates a copy of the cyclient object.

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> new=cytoscape.copy()
```
___

## ___cyclient.result___

**`cyclient.result(filetype="PNG", saveas=None, host=None, port=None)`**

Checks the current network. 

* **`filetype`** file type eg.PDF, PNG, CYS, CYJS; default="PNG" 
* **`saveas`** /path/to/non/tmp/file.prefix
* **`host`** cytoscape host address, default=cytoscape_host
* **`port`** cytoscape port, default=1234
* **`returns`** an image

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> new=cytoscape.copy()
```
___