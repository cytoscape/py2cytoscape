## ___cyclient.session.new___

Destroys the current session and creates a new, empty one.

**`cyclient.session.new(verbose=False)`**

* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.session.new()
```
___

## ___cyclient.session.open___

Opens a session from a local file or URL.

**`cyclient.session.open(session_file=None, session_url=None, verbose=False)`**

* **`session_file`** The path to the session file (.cys) to be loaded.
* **`session_url`** A URL that provides a session file.
* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.session.open(session_file="/path/to/my/cytoscape/session.cys")
```
___
## ___cyclient.session.save___

Saves the current session to an existing file, which will be replaced.
If this is a new session that has not been saved yet, use 'save as' instead.

**`cyclient.session.save(session_file, verbose=False)`**

* **`session_file`** The path to the file where the current session must be saved to.
* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.session.save("/path/to/my/cytoscape/session.cys")
```
___
## ***cyclient.session.save_as***

Saves the current session as a new file.

**`cyclient.session.save_as(session_file, verbose=False)`**

* **`session_file`** The path to the file where the current session must be saved to.
* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.session.save_as("/path/to/my/cytoscape/session.cys")
```
___
