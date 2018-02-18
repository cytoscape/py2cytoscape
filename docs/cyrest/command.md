## ___cyclient.command.echo___

The echo command will display the value of the variable specified by the
variableName argument, or all variables if variableName is not provided.

**`cyclient.command.echo(self, variableName, verbose=False)`**

* **`variableName`** The name of the variable or "*" to display the value of all variables.
* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.command.echo("*")
```
___

## ***cyclient.command.open_dialog***

The command line dialog provides a field to enter commands and view
results. It also provides the help command to display namespaces,
commands, and arguments.

**`cyclient.command.open_dialog(self, verbose=False)`**

* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.command.open_dialog()
```
___

## ___cyclient.command.pause___

The pause command displays a dialog with the text provided in the
message argument and waits for the user to click OK

**`cyclient.command.pause(self, variableName, verbose=False)`**

* **`message`** a message to display. default=None
* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.command.pause("check out the results before continuing")
```
___

## ___cyclient.command.quit___

This command causes Cytoscape to exit. It is typically used at
the end of a script file.

**`cyclient.command.quit(self, verbose=False)`**

* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.command.quit()
```
___

## ___cyclient.command.run___

The run command will execute a command script from the file pointed to
by the file argument, which should contain Cytoscape commands, one per
line. Arguments to the script are provided by the args argument.

**`cyclient.command.run(self, script_file,args=None,verbose=False)`**

* **`script_file`** file to run
* **`args`** enter the script arguments as key:value pairs
 separated by commas. eg. "arg1:value1,arg2:value2"
* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.command.run("/path/to/myscript","title:miRNA_network,nodes:100")
```
___

## ___cyclient.command.sleep___

The sleep command will pause processing for a period of time as
 specified by duration seconds. It is typically used as part of
 a command script.

**`cyclient.command.sleep(self, duration, verbose=False)`**

* **`duration`** enter the time in seconds to sleep
* **`verbose`** print more

```python
>>> from py2cytoscape import cyrest
>>> cytoscape=cyrest.cyclient()
>>> cytoscape.command.sleep(60)
```
