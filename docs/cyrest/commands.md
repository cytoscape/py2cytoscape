## ___cyclient.commands.list___

List all available command namespaces.

**`cyclient.commands.list(verbose=False)`**

* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.commands.list()

Available namespaces:
command
cybrowser
diffusion
edge
group
idmapper
layout
network
node
session
string
table
view
vizmap
```
___

## ___cyclient.commands.namespace___

List all available commands in a namespace.

**`cyclient.commands.namespace(namespace, verbose=False)`**

* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.commands.namespace("network")

Available commands for 'network':
  add
  add edge
  add node
  clone
  connect nodes
  create
  create attribute
  create empty
  delete
  deselect
  destroy
  export
  get
  get attribute
  get properties
  hide
  import file
  import url
  list
  list attributes
  list properties
  load file
  load url
  rename
  select
  set attribute
  set current
  set properties
  show
```
___
## ___cyclient.commands.command___

List the arguments of a command.

**`cyclient.commands.command(namespace, command, verbose=False)`**

* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.commands.command("network","rename")

Available arguments for 'network rename':
  name
  sourceNetwork
```
___
