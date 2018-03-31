## ***cyclient.edge.rename***

**`cyclient.edge.rename(self, edge=None, network=None, newName=None, verbose=False)`**

Sets the value of the name column for the passed edge.

* **`edge (string, optional)`** Selects an edge by name, or, if the
parameter has the prefix suid:, selects an edge by SUID.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`newName (string, optional)`** New name of the edge
* **`verbose`** print more


___

## ***cyclient.edge.get***

**`cyclient.edge.get(self,edge=None,network=None,sourceNode=None, targetNode=None, atype=None, verbose=False)`**

Returns the SUID of an edge that matches the passed parameters. If
multiple edges are found, only one will be returned, and a warning will
be reported in the Cytoscape Task History dialog.

* **`edge (string, optional)`** Selects an edge by name, or, if the
parameter has the prefix suid:, selects an edge by SUID. If this
parameter is set, all other edge matching parameters are ignored.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`sourceNode (string, optional)`** Selects a node by name, or, if
the parameter has the prefix suid:, selects a node by SUID. Specifies
that the edge matched must have this node as its source. This parameter
must be used with the targetNode parameter to produce results.
* **`targetNode (string, optional)`** Selects a node by name, or, if
the parameter has the prefix suid:, selects a node by SUID. Specifies
that the edge matched must have this node as its target. This parameter
must be used with the sourceNode parameter to produce results.
* **`atype (string, optional)`** Specifies that the edge matched must
be of the specified type. This parameter must be used with the
sourceNode and targetNode parameters to produce results.
* **`verbose`** print more

* **`returns`** {"columnName": columnName }


___

## ***cyclient.edge.get_attribute***

**`cyclient.edge.get_attribute(self,columnList=None,edgeList=None,namespace=None, network=None, verbose=False)`**

Returns the attributes for the edges passed as parameters.

* **`columnList (string, optional)`** A list of column names, separated
by commas.
* **`edgeList (string, optional)`** Specifies a list of edges. The
keywords all, selected, or unselected can be used to specify edges
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list
of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`namespace (string, optional)`** Node, Edge, and Network objects
support the default, local, and hidden namespaces. Root networks
also support the shared namespace. Custom namespaces may be specified
by Apps.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`verbose`** print more

* **`returns`** eg. [ {"name": "TAT (pp) O60563"}, {"name": "TAT (pp) O60563"}]


___

## ***cyclient.edge.list_properties***

**`cyclient.edge.list_properties(self,columnList=None,edgeList=None,namespace=None, network=None, verbose=False)`**

Returns a list of visual properties available for edges.

* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`verbose`** print more

* **`returns`**  eg. [
"Label Font Size",
"Source Arrow Size",
"Stroke Color (Unselected)",
"Source Arrow Selected Paint",
"Label Font Face",
"Target Arrow Unselected Paint",
"Transparency",
"Source Arrow Unselected Paint",
"Tooltip",
.. ]

___

## ***cyclient.edge.list***

**`cyclient.edge.list(self, edgeList=None, network=None, verbose=False)`**

Returns a list of the edge SUIDs associated with the passed network parameter.

* **`edgeList (string, optional)`** Specifies a list of edges. The
keywords all, selected, or unselected can be used to specify edges
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list of
COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`verbose`** print more

* **`returns`** eg. [ 772, 773, .. ]

___

## ***cyclient.edge.get_properties***

**`cyclient.edge.get_properties(self,edgeList=None,network=None,propertyList=None, verbose=False)`**

Returns the visual properties for the edges that match the passed parameters.

* **`edgeList (string, optional)`** Specifies a list of edges. The
keywords all, selected, or unselected can be used to specify edges
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list
of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`propertyList (string, optional)`** A list of property names
separated by commas.
* **`verbose`** print more

* **`returns`** eg. [
{
"SUID": 1647,
"visualProperties": [
{
"visualProperty": "EDGE_PAINT",
"value": "#808080"
},
{
"visualProperty": "EDGE_VISIBLE",
"value": true
}
]
},
...
]

___

## ***cyclient.edge.set_attribute***

**`cyclient.edge.set_attribute(self, columnList=None, edgeList=None, namespace=None, network=None, valueList=None, verbose=False)`**

Sets the value of a specified column for the passed edge or set of edges.

* **`columnList (string, optional)`** A list of column names, separated
by commas.
* **`edgeList (string, optional)`** Specifies a list of edges. The
keywords all, selected, or unselected can be used to specify edges
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list
of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`namespace (string, optional)`** Node, Edge, and Network objects
support the default, local, and hidden namespaces. Root networks
also support the shared namespace. Custom namespaces may be specified
by Apps.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`valueList (string, optional)`** A list of values, separated by
commas. List values can be included using the format [value1,value2].
* **`verbose`** print more


___

## ***cyclient.edge.set_properties***

**`cyclient.edge.set_properties(self, edgeList=None, network=None, propertyList=None, valueList=None, verbose=False)`**

Sets the value of a specified property for the passed edge or set of edges.

* **`edgeList (string, optional)`** Specifies a list of edges. The
keywords all, selected, or unselected can be used to specify edges
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list of
COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`propertyList (string, optional)`** A list of property names
separated by commas.
* **`valueList (string, optional)`** A list of values separated by commas.
* **`verbose`** print more

___

## ***cyclient.edge.list_attributes***

**`cyclient.edge.list_attributes(self,columnList=None,edgeList=None,namespace=None, network=None, verbose=False)`**

Returns the attributes for the edges passed as parameters.

* **`columnList (string, optional)`** A list of column names, separated
by commas.
* **`edgeList (string, optional)`** Specifies a list of edges. The
keywords all, selected, or unselected can be used to specify edges
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list
of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`namespace (string, optional)`** Node, Edge, and Network objects
support the default, local, and hidden namespaces. Root networks
also support the shared namespace. Custom namespaces may be specified
by Apps.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`verbose`** print more

* **`returns`**  eg. [
"SUID",
"shared name",
"shared interaction",
"name",
"selected",
"interaction",
"Annotation",
.. ]

___

## ***cyclient.edge.create_attribute***

**`cyclient.edge.create_attribute(self,column=None,listType=None,namespace=None, network=None, atype=None, verbose=False)`**

Creates a new edge column.

* **`column (string, optional)`** Unique name of column
* **`listType (string, optional)`** Can be one of integer, long, double,
or string.
* **`namespace (string, optional)`** Node, Edge, and Network objects
support the default, local, and hidden namespaces. Root networks
also support the shared namespace. Custom namespaces may be specified
by Apps.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`atype (string, optional)`** Can be one of integer, long, double,
string, or list.
* **`verbose`** print more


___

