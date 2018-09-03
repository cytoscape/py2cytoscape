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

## ***cyclient.session.createSessionFile***

**`cyclient.session.createSessionFile(file, verbose=None)`**

Saves the current session to a file. If successful, the session file location will be returned.

* **`file`** Session file location as an absolute path
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.session.deleteSession***

**`cyclient.session.deleteSession(verbose=None)`**

This deletes the current session and initializes a new one. A message is returned to indicate the success of the deletion.

* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.session.getSessionFromFile***

**`cyclient.session.getSessionFromFile(file, verbose=None)`**

Loads a session from a local file and returns the session file name

* **`file`** Session file location as an absolute path
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.session.getSessionName***

**`cyclient.session.getSessionName(verbose=None)`**

Returns the file name for the current Cytoscape session.

* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.session.runGarbageCollection***

**`cyclient.session.runGarbageCollection(verbose=None)`**

Manually call Java's System.gc() to free up unused memory. This process happens automatically, but may be useful to call explicitly for testing or evaluation purposes.

* **`verbose`** print more

* **`returns`** 204: Successful Garbage Collection

___
