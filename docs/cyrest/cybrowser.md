## ___cyclient.cybrowser.dialog___

Launch and HTML browser in a separate window.

**`cyclient.cybrowser.dialog(wid=None, text=None, title=None, url=None, debug=False, verbose=False)`**

* **`wid`** Window ID
* **`text`** HTML text
* **`title`** Window Title
* **`url`** URL
* **`debug`** Show debug tools. boolean
* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.cybrowser.dialog(wid="1", "http://www.cytoscape.org")
```
___

## ___cyclient.cybrowser.hide___

Hide and HTML browser in the Results Panel.

**`cyclient.cybrowser.hide(wid, verbose=False)`**

* **`wid`** Window ID
* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.cybrowser.hide("1")
```
___

## ___cyclient.cybrowser.show___

Launch and HTML browser in the Results Panel.

**`cyclient.cybrowser.show(wid, text, title, url, verbose=False)`**

* **`wid`** Window ID
* **`text`** HTML text
* **`title`** Window Title
* **`url`** URL
* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.cybrowser.show(url="http://www.cytoscape.org")
```
___

## ___cyclient.cybrowser.show___

Display the CyBrowser version.

**`cyclient.cybrowser.version(verbose=False)`**

* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.cybrowser.version()

Version: 0.5.1

Finished
```
