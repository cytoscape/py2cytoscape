## ___cyclient___

A CyREST client.

**`cyclient(host="localhost", port=1234, version="V1")`**

* **`host`** CyREST host server address. default='localhost'
* **`port`** CyREST port number. default=1234
* **`version`** CyREST version. default='v1'

* **`returns status`** a cyclient object.

```python
>>> from py2cytoscape import cyrest as p2c
>>> cytoscape=p2c.cyclient()
```
___

## ___cyclient.status___

Checks the status of your CyREST server.

**`cyclient.status()`**

```python
>>> from py2cytoscape import cyrest as p2c
>>> cytoscape=p2c.cyclient()
>>> cytoscape.status()

CyREST online!
```
