## ***cyclient.command.quit***

**`cyclient.command.quit(self,verbose=False)`**

This command causes Cytoscape to exit. It is typically used at the end
of a script file.

* **`verbose`** print more

___

## ***cyclient.command.pause***

**`cyclient.command.pause(self, message=None, verbose=False)`**

The pause command displays a dialog with the text provided in the
message argument and waits for the user to click OK

* **`message`** a message to display. default=None
* **`verbose`** print more

___

## ***cyclient.command.run***

**`cyclient.command.run(self,script_file,args=None,verbose=False)`**

The run command will execute a command script from the file pointed to
by the file argument, which should contain Cytoscape commands, one per
line. Arguments to the script are provided by the args argument.

* **`script_file`** file to run
* **`args: enter the script arguments as key`** value pairs separated by
commas. eg. "arg1:value1,arg2:value2"
* **`verbose`** print more

___

## ***cyclient.command.echo***

**`cyclient.command.echo(self, variableName, verbose=False)`**

The echo command will display the value of the variable specified by the
variableName argument, or all variables if variableName is not provided.

* **`variableName`** The name of the variable or '*' to display the value of all variables.
* **`verbose`** print more

___

## ***cyclient.command.sleep***

**`cyclient.command.sleep(self,duration,verbose=False)`**

The sleep command will pause processing for a period of time as specified
by duration seconds. It is typically used as part of a command script.

* **`duration`** enter the time in seconds to sleep
* **`verbose`** print more

___

## ***cyclient.command.open_dialog***

**`cyclient.command.open_dialog(self, verbose=False)`**

The command line dialog provides a field to enter commands and view
results. It also provides the help command to display namespaces,
commands, and arguments.

* **`verbose`** print more

___

