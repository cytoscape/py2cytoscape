## ***cyclient.node.rename***

**`cyclient.node.rename(self, network=None, newName=None, node=None, verbose=False)`**

Sets the value of the name column for the passed node.

* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`newName (string, optional)`** New name of the node ,
* **`node (string, optional)`** Selects a node by name, or, if the
parameter has the prefix suid:, selects a node by SUID.
* **`verbose`** print more

___

## ***cyclient.node.get***

**`cyclient.node.get(self, network=None, node=None, verbose=False)`**

Returns the SUID of a node that matches the passed parameters. If
multiple nodes are found, only one will be returned, and a warning will
be printed.

* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`node (string, optional)`** Selects a node by name, or, if the
parameter has the prefix suid: selects a node by SUID.
* **`verbose`** print more

* **`returns`** [ SUIDs of nodes that match the passed parameters ]

___

## ***cyclient.node.select_from_file***

**`cyclient.node.select_from_file(self, afile=None, verbose=False)`**

Selects nodes in the current network based on node names provided by a file.

* **`afile (string, optional)`** Path to file containing list of nodes to select
* **`verbose`** print more

___

## ***cyclient.node.get_attribute***

**`cyclient.node.get_attribute(self, columnList=None, namespace=None, network=None, nodeList=None, verbose=False)`**

Returns the attributes for the nodes passed as parameters.

* **`columnList (string, optional)`** A list of column names, separated
by commas.
* **`namespace (string, optional)`** Node, Edge, and Network objects
support the default, local, and hidden namespaces. Root networks
also support the shared namespace. Custom namespaces may be specified
by Apps.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`nodeList (string, optional)`** Specifies a list of nodes. The
keywords all, selected, or unselected can be used to specify nodes
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list of
COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`verbose`** print more

* **`returns`** [ { "name": "Q9UQ35"}, { "name": "Q4G0J3" } ]

___

## ***cyclient.node.list_properties***

**`cyclient.node.list_properties(self, network=None, verbose=False)`**

Returns a list of visual properties available for nodes.

* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`verbose`** print more

* **`returns`** [ list of visual properties available for nodes ]

___

## ***cyclient.node.list***

**`cyclient.node.list(self, network=None, nodeList=None, verbose=False)`**

Returns a list of the node SUIDs associated with the passed network parameter.

* **`network (string, optional)`** Specifies a network by name, or by SUID
if the prefix SUID: is used. The keyword CURRENT, or a blank value
can also be used to specify the current network.
* **`nodeList (string, optional)`** Specifies a list of nodes. The
keywords all, selected, or unselected can be used to specify nodes by
their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list of
COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`verbose`** print more

* **`returns`** [ 283,  295, 311 ]

___

## ***cyclient.node.get_properties***

**`cyclient.node.get_properties(self, network=None, nodeList=None, propertyList=None, verbose=False)`**

Returns the visual properties for the nodes that match the passed parameters.

* **`network (string, optional)`** Specifies a network by name, or by SUID
if the prefix SUID: is used. The keyword CURRENT, or a blank value
can also be used to specify the current network.
* **`nodeList (string, optional)`** Specifies a list of nodes. The
keywords all, selected, or unselected can be used to specify nodes by
their selection state. The pattern COLUMN:VALUE sets this parameter to
any rows that contain the specified column value; if the COLUMN prefix
is not used, the NAME column is matched by default. A list of COLUMN:VALUE
pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to match
multiple values.
* **`propertyList (string, optional)`** A list of property names separated by commas.
* **`verbose`** print more


* **`returns`** [
{
"SUID": 627,
"visualProperties": [
{
"visualProperty": "NODE_VISIBLE",
"value": true
},
{
"visualProperty": "NODE_PAINT",
"value": "#FF6666"
}
]
},
{
"SUID": 566,
"visualProperties": [
{
"visualProperty": "NODE_VISIBLE",
"value": true
},
{
"visualProperty": "NODE_PAINT",
"value": "#FF6666"
}
]
} ]

___

## ***cyclient.node.set_attribute***

**`cyclient.node.set_attribute(self, columnList=None, namespace=None, network=None, nodeList=None, valueList=None, verbose=False)`**

Sets the value of a specified column for the passed node or set of nodes.

* **`columnList (string, optional)`** A list of column names, separated
by commas.
* **`namespace (string, optional)`** Node, Edge, and Network objects
support the default, local, and hidden namespaces. Root networks also
support the shared namespace. Custom namespaces may be specified by Apps.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network. ,
* **`nodeList (string, optional)`** Specifies a list of nodes. The
keywords all, selected, or unselected can be used to specify nodes by
their selection state. The pattern COLUMN:VALUE sets this parameter to
any rows that contain the specified column value; if the COLUMN prefix
is not used, the NAME column is matched by default. A list of COLUMN:VALUE
pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to
match multiple values.
* **`valueList (string, optional)`** A list of values, separated by
commas. List values can be included using the format [value1,value2].
* **`verbose`** print more

___

## ***cyclient.node.set_properties***

**`cyclient.node.set_properties(self, network=None, nodeList=None, propertyList=None, valueList=None, verbose=False)`**

Sets the value of a specified property for the passed node or set of nodes.

* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`nodeList (string, optional)`** Specifies a list of nodes. The
keywords all, selected, or unselected can be used to specify nodes
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list of
COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`propertyList (string, optional)`** A list of property names
separated by commas.
* **`valueList (string, optional)`** A list of values separated by commas.
* **`verbose`** print more

___

## ***cyclient.node.list_attributes***

**`cyclient.node.list_attributes(self, namespace=None, network=None, verbose=False)`**

Returns a list of column names assocated with nodes.

* **`namespace (string, optional)`** Node, Edge, and Network objects
support the default, local, and hidden namespaces. Root networks also
support the shared namespace. Custom namespaces may be specified by Apps.
* **`network (string, optional)`** Specifies a network by name, or by SUID
if the prefix SUID: is used. The keyword CURRENT, or a blank value can
also be used to specify the current network.
* **`verbose`** print more

* **`returns`** [ list of column names assocated with nodes ]

___

## ***cyclient.node.create_attribute***

**`cyclient.node.create_attribute(self, column=None, listType=None, namespace=None, network=None, coltype=None, verbose=False)`**

Creates a new node column.

* **`column (string, optional)`** Unique name of column.
* **`listType (string, optional)`** Can be one of integer, long, double,
or string. = ['integer', 'long', 'double', 'string', 'boolean']
* **`namespace (string, optional)`** Node, Edge, and Network objects
support the default, local, and hidden namespaces. Root networks
also support the shared namespace. Custom namespaces may be
specified by Apps.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`coltype (string, optional)`** Can be one of integer, long, double,
string, or list. = ['integer', 'long', 'double', 'string', 'boolean', 'list']
* **`verbose`** print more

* **`returns`** {"columnName": columnName}

___

