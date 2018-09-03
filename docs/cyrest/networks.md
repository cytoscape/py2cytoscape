## ***cyclient.networks.getView***

**`cyclient.networks.getView(networkId, viewId, objectType, objectId, verbose=None)`**

Gets a list of Visual Properties for the Object specified by the `objectId` and `objectType` parameters in the Network View specified by the `viewId` and `networkId` parameters.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`objectType`** Type of Object
* **`objectId`** SUID of the Object
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getColumnNames***

**`cyclient.networks.getColumnNames(networkId, tableType, verbose=None)`**

Returns all the columns in the table specified by the `networkId` and `tableType` parameters.

* **`networkId`** SUID of the network containing the table
* **`tableType`** Table Type
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.updateTable***

**`cyclient.networks.updateTable(networkId, tableType, body, class, verbose=None)`**

Updates the table specified by the `tableType` and `networkId` parameters.  New columns will be created if they do not exist in the target table.
Current limitations:
* Numbers are handled as Double
* List column is not supported in this version

* **`networkId`** SUID containing the table
* **`tableType`** Type of table
* **`body`** The data with which to update the table.
* **`class`** None -- Not required, can be None
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.createNetworkFromSelected***

**`cyclient.networks.createNetworkFromSelected(networkId, title, verbose=None)`**

Creates new sub-network from current selection, with the name specified by the `title` parameter.
Returns the SUID of the new sub-network.

* **`networkId`** SUID of the network containing the selected nodes and edges
* **`title`** Name for the new sub-network -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getNodeCount***

**`cyclient.networks.getNodeCount(networkId, verbose=None)`**

Returns the number of nodes in the network specified by the `networkId` parameter.

* **`networkId`** SUID of the network containing the nodes
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.collapseGroup***

**`cyclient.networks.collapseGroup(networkId, groupNodeId, verbose=None)`**

Collapses the group specified by the `groupNodeId` and `networkId` parameters.

* **`networkId`** SUID of the Network
* **`groupNodeId`** SUID of the Node representing the Group
* **`verbose`** print more

* **`returns`** 204: Group collapsed; 500: Failed to collapse group

___

## ***cyclient.networks.getEdge***

**`cyclient.networks.getEdge(networkId, edgeId, verbose=None)`**

Returns an edge with its associated row data.

* **`networkId`** SUID of the network containing the edge
* **`edgeId`** SUID of the edge
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getTables***

**`cyclient.networks.getTables(networkId, verbose=None)`**

Returns every table in the network specified by the `networkId` parameter.

* **`networkId`** SUID of the Network
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getFirstImageAsSvg***

**`cyclient.networks.getFirstImageAsSvg(networkId, h, verbose=None)`**

Returns an SVG image of the first available Network View for the Network specified by the `networkId` parameter.
Default size is 600 px

* **`networkId`** SUID of the Network
* **`h`** Height of the image. Width is set automatically -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: SVG image stream.

___

## ***cyclient.networks.getRows***

**`cyclient.networks.getRows(networkId, tableType, verbose=None)`**

Returns all rows from the table specified by `networkId` and `tableType` parameters. Returns a JSON representation of an array of rows.
```
[
{
"SUID": 101,
"gene_name": "brca1",
"exp": 0.1
},
{
"SUID": 102,
"gene_name": "brca2",
"exp": 0.2
}
]
```

* **`networkId`** SUID of the network containing the table
* **`tableType`** Table Type
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.deleteGroup***

**`cyclient.networks.deleteGroup(networkId, groupNodeId, verbose=None)`**

Deletes the group specified by the `groupNodeId` and `networkId` parameters. The nodes and edges that the group contained will remain present in the network, however the node used to identify the Group will be deleted.

* **`networkId`** SUID of the Network
* **`groupNodeId`** SUID of the Node representing the Group
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.getSelectedNodes***

**`cyclient.networks.getSelectedNodes(networkId, verbose=None)`**

Gets the selected nodes in the network specified by the `networkId` parameter. The results are presented as a list of SUIDs.

* **`networkId`** SUID of the network containing the nodes
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.setCurrentNetworkView***

**`cyclient.networks.setCurrentNetworkView(body, verbose=None)`**

Sets the current Network View.

* **`body`** SUID of the Network View -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.expandGroup***

**`cyclient.networks.expandGroup(networkId, groupNodeId, verbose=None)`**

Expands the group specified by the `groupNodeId` and `networkId` parameters.

* **`networkId`** SUID of the Network
* **`groupNodeId`** SUID of the Node representing the Group
* **`verbose`** print more

* **`returns`** 204: Group expanded; 500: Failed to expand group

___

## ***cyclient.networks.setSelectedEdges***

**`cyclient.networks.setSelectedEdges(networkId, body, verbose=None)`**

Sets as selected the edges specified by the `suids` and `networkId` parameters.
Returns a list of selected SUIDs.

* **`networkId`** SUID of the network containing the edges
* **`body`** Array of edge SUIDs to select -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getEdgeDirected***

**`cyclient.networks.getEdgeDirected(networkId, edgeId, verbose=None)`**

Returns true if the edge specified by the `edgeId` and `networkId` parameters is directed.

* **`networkId`** SUID of the network containing the edge
* **`edgeId`** SUID of the edge
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getRow***

**`cyclient.networks.getRow(networkId, tableType, primaryKey, verbose=None)`**

Gets a row matching the value specified by the `primaryKey` parameter from the table specified by the `tableType` and `networkId` parameters.
Data is represented by column names and their values.
```json
{
"name": "Hodor 1",
"value": 0.11,
"matched": false
...
}
```

* **`networkId`** SUID of the network containing the table
* **`tableType`** Table type
* **`primaryKey`** Primary key of the row Object, normally an SUID
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getCurrentNetworkView***

**`cyclient.networks.getCurrentNetworkView(verbose=None)`**

Returns the current Network View.

* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getImageAsSvg***

**`cyclient.networks.getImageAsSvg(networkId, viewId, h, verbose=None)`**

Returns an SVG image of the Network View specified by the `viewId` and `networkId` parameters.
Default size is 600 px.

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`h`** Height of the image. Width is set automatically -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: SVG image stream.

___

## ***cyclient.networks.getGroup***

**`cyclient.networks.getGroup(networkId, groupNodeId, verbose=None)`**

Returns the group specified by the `groupNodeId` and `networkId` parameters.

* **`networkId`** SUID of the Network
* **`groupNodeId`** SUID of the Node representing the Group
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getNetworkPointer***

**`cyclient.networks.getNetworkPointer(networkId, nodeId, verbose=None)`**

If the node specified by the `nodeId` and `networkId` parameters has an associated nested network, returns the SUID of the nested network.

* **`networkId`** SUID of the network containing the node
* **`nodeId`** SUID of the node
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getAllGroups***

**`cyclient.networks.getAllGroups(networkId, verbose=None)`**

Returns a list of all the groups in the network specified by the `networkId` parameter.

* **`networkId`** Network SUID
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getImageAsPdf***

**`cyclient.networks.getImageAsPdf(networkId, viewId, verbose=None)`**

Returns a PDF of the Network View specified by the `viewId` and `networkId` parameters.
Default size is 500 px.

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`verbose`** print more

* **`returns`** 200: PDF image stream.

___

## ***cyclient.networks.putSingleVisualPropertyValueBypass***

**`cyclient.networks.putSingleVisualPropertyValueBypass(networkId, viewId, objectType, objectId, visualProperty, body, verbose=None)`**

Bypasses the Visual Style of the object specified by the `objectId` and `objectType` parameters, in the Network View specified by the `viewId` and `networkId` parameters. The Visual Property included in the message body will be used instead of the definition provided by the Visual Style.
Examples of Visual Properties:
```
{
"visualProperty": "NODE_BORDER_WIDTH",
"value": 2
}
```
```
{
"visualProperty": "EDGE_TRANSPARENCY",
"value": 170
}```
```
{
"visualProperty": "NETWORK_BACKGROUND_PAINT",
"value": "#000000"
}```
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`networkId`** Network SUID
* **`viewId`** Network View SUID
* **`objectType`** Type of Object
* **`objectId`** SUID of the Object
* **`visualProperty`** Name of the Visual Property
* **`body`** A Visual Property and its value.
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.getNetworkViewAsCx***

**`cyclient.networks.getNetworkViewAsCx(networkId, viewId, verbose=None)`**

Returns the Network View specified by the `viewId` and `networkId` parameters in [CX format](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#cytoscape-cx)

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.deleteAllNodes***

**`cyclient.networks.deleteAllNodes(networkId, verbose=None)`**

Delete all the nodes from the network specified by the `networkId` parameter.

* **`networkId`** SUID of the network to delete nodes from
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.getNeighbours***

**`cyclient.networks.getNeighbours(networkId, nodeId, verbose=None)`**

Returns the neighbors of the node specified by the `nodeId` and `networkId` parameters as a list of SUIDs.

* **`networkId`** SUID of the network containing the node.
* **`nodeId`** SUID of the node
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.setSelectedNodes***

**`cyclient.networks.setSelectedNodes(networkId, body, verbose=None)`**

Sets as selected the nodes specified by the `suids` and `networkId` parameters.
Returns a list of selected SUIDs.

* **`networkId`** SUID of the network containing the nodes
* **`body`** Array of node SUIDs to select -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getNetworkCount***

**`cyclient.networks.getNetworkCount(verbose=None)`**

Returns the number of networks in current Cytoscape session.

* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getViews***

**`cyclient.networks.getViews(networkId, viewId, objectType, visualProperty, verbose=None)`**

Returns a list of all Visual Property values for the Visual Property specified by the `visualProperty` and `objectType` parameters, in the Network View specified by the `viewId` and `networkId` parameters.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`objectType`** Type of Object
* **`visualProperty`** Name of the Visual Property -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getSelectedEdges***

**`cyclient.networks.getSelectedEdges(networkId, verbose=None)`**

Gets the selected edges in the network specified by the `networkId` parameter. The results are presented as a list of SUIDs.

* **`networkId`** SUID of the network containing the edges
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.deleteFirstNetworkView***

**`cyclient.networks.deleteFirstNetworkView(networkId, verbose=None)`**

Deletes the first available Network View for the Network specified by the `networkId` parameter. Cytoscape can have multiple views per network model, but this feature is not exposed in the Cytoscape GUI. GUI access is limited to the first available view only.

* **`networkId`** SUID of the Network
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.deleteNetworkVisualProp***

**`cyclient.networks.deleteNetworkVisualProp(networkId, viewId, visualProperty, verbose=None)`**

Deletes the bypass Visual Property specificed by the `visualProperty`, `viewId`, and `networkId` parameters. When this is done, the Visual Property will be defined by the Visual Style
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`visualProperty`** Name of the Visual Property
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getFirstImageAsPng***

**`cyclient.networks.getFirstImageAsPng(networkId, h, verbose=None)`**

Returns a PNG image of the first available Network View for the Network specified by the `networkId` parameter.
Default size is 600 px

* **`networkId`** SUID of the Network
* **`h`** Height of the image. Width is set automatically -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: PNG image stream.

___

## ***cyclient.networks.getColumnValues***

**`cyclient.networks.getColumnValues(networkId, tableType, columnName, verbose=None)`**

Returns all the values for the column specified by the `columnType` parameter, in the table specified by the `networkId` and `tableType` parameters.

* **`networkId`** SUID of the Network
* **`tableType`** Type of Table
* **`columnName`** Name of the Column
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getEdgeCount***

**`cyclient.networks.getEdgeCount(networkId, verbose=None)`**

Returns the number of edges in the network specified by the `networkId` parameter.

* **`networkId`** SUID of the network containing the edges
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.updateNetworkView***

**`cyclient.networks.updateNetworkView(networkId, viewId, bypass, body, verbose=None)`**

Updates the Visual Properties in the Network View specified by the `viewId` and `networkId` parameters.
Example Visual Properties:
```
{
"visualProperty": "NETWORK_BACKGROUND_PAINT",
"value": "#000000"
}```
```
{
"visualProperty": "NETWORK_CENTER_X_LOCATION",
"value": 250
}```
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)
Note that this sets the Visual Properties temporarily unless the `bypass` parameter is set to `true`. If the `bypass` parameter is set to `true`, the Visual Style will be overridden by these Visual Property values. If the `bypass` parameter is not used or is set to `false`, any Visual Properties set will return to those defined in the Visual Style if the Network View is updated.

* **`networkId`** Network SUID
* **`viewId`** Network View SUID
* **`bypass`** Bypass the Visual Style with these properties -- Not required, can be None
* **`body`** A list of Visual Properties and their values.
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.getCell***

**`cyclient.networks.getCell(networkId, tableType, primaryKey, columnName, verbose=None)`**

Return the value of a cell specified by the `primaryKey` and `columnName` parameters in the table specified by the `tableType` and `networkId` parameters.
Returns a JSON representation of a String, Boolean, Number, or List.

* **`networkId`** SUID of the network containing the table
* **`tableType`** Table type
* **`primaryKey`** Primary key of the row Object, normally an SUID
* **`columnName`** Name of the Column
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getEdges***

**`cyclient.networks.getEdges(networkId, column, query, verbose=None)`**

Returns a list of all edges in the network specified by the `networkId` parameter as SUIDs.
If the `column` and `query` parameters are specified, the results will be limited to rows in the edge table where the value in the column specified by the `column` parameter matches the value specified by the `query` parameter.

* **`networkId`** SUID of the network containing the edges
* **`column`** The name of the column that will be queried for matches. -- Not required, can be None
* **`query`** The value to be matched. -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.createNetworkView***

**`cyclient.networks.createNetworkView(networkId, verbose=None)`**

Creates a new Network View for the Network specified by the `networkId` parameter.

* **`networkId`** SUID of the Network
* **`verbose`** print more

* **`returns`** 201: Network View SUID

___

## ***cyclient.networks.getNetwork***

**`cyclient.networks.getNetwork(networkId, verbose=None)`**

Returns the Network specified by the `networkId` parameter with all associated tables in [Cytoscape.js](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#cytoscape-js-json) format

* **`networkId`** SUID of the Network
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getNetworkViewCount***

**`cyclient.networks.getNetworkViewCount(networkId, verbose=None)`**

Returns a count of the Network Views available for the Network specified by the `networkId` parameter.
Cytoscape can have multiple views per network model, but this feature is not exposed in the Cytoscape GUI. GUI access is limited to the first available view only.

* **`networkId`** SUID of the Network
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.updateView***

**`cyclient.networks.updateView(networkId, viewId, objectType, objectId, bypass, body, verbose=None)`**

Updates the Visual Properties in the object specified by the `objectId` and `objectType` parameters in the Network View specified by the `viewId` and `networkId` parameters.
Examples of Visual Properties:
```
{
"visualProperty": "NODE_BORDER_WIDTH",
"value": 2
}
```
```
{
"visualProperty": "EDGE_TRANSPARENCY",
"value": 170
}```
```
{
"visualProperty": "NETWORK_BACKGROUND_PAINT",
"value": "#000000"
}```
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)
Note that this sets the Visual Properties temporarily unless the `bypass` parameter is set to `true`. If the `bypass` parameter is set to `true`, the Visual Style will be overridden by these Visual Property values. If the `bypass` parameter is not used or is set to `false`, any Visual Properties set will return to those defined in the Visual Style if the Network View is updated.

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`objectType`** Type of Object
* **`objectId`** SUID of the Object
* **`bypass`** Bypass the Visual Style with these Visual Properties -- Not required, can be None
* **`body`** A list of Visual Properties and their values.
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.deleteAllNetworkViews***

**`cyclient.networks.deleteAllNetworkViews(networkId, verbose=None)`**

Deletes all Network Views available in the Network specified by the `networkId` parameter. Cytoscape can have multiple views per network model, but this feature is not exposed in the Cytoscape GUI. GUI access is limited to the first available view only.

* **`networkId`** SUID of the Network
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.getSingleVisualPropertyValueBypass***

**`cyclient.networks.getSingleVisualPropertyValueBypass(networkId, viewId, objectType, objectId, visualProperty, verbose=None)`**

Gets the bypass Visual Property specified by the `visualProperty` parameter from the object specified by the `objectId` and `objectType` parameters in the Network View Specified by the `viewId` and `networkId` parameters. The response is the Visual Property that is used in place of the definition provided by the Visual Style.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`networkId`** Network SUID
* **`viewId`** Network View SUID
* **`objectType`** Type of Object
* **`objectId`** SUID of the Object
* **`visualProperty`** Name of the Visual Property
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getNetworkVisualProp***

**`cyclient.networks.getNetworkVisualProp(networkId, viewId, visualProperty, verbose=None)`**

Gets the Network Visual Property specificed by the `visualProperty`, `viewId`, and `networkId` parameters.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`visualProperty`** Name of the Visual Property
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getNetworkVisualProps***

**`cyclient.networks.getNetworkVisualProps(networkId, viewId, verbose=None)`**

Returns a list of the Visual Properties for the Network View specified by the `viewId` and `networkId` parameters.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.deleteNode***

**`cyclient.networks.deleteNode(networkId, nodeId, verbose=None)`**

Deletes the node specified by the `nodeId` and `networkId` parameters.

* **`networkId`** SUID of the network containing the node.
* **`nodeId`** SUID of the node
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.createGroup***

**`cyclient.networks.createGroup(networkId, body, verbose=None)`**

Create a new group in the network specified by the parameter `networkId`. The contents are specified the message body.

* **`networkId`** SUID of the Network
* **`body`** New Group name and contents
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getFirstNetworkView***

**`cyclient.networks.getFirstNetworkView(networkId, file, verbose=None)`**

This returns the first view of the network. Cytoscape can have multiple views per network model, but this feature is not exposed in the Cytoscape GUI. GUI access is limited to the first available view only.
If the `file` parameter is left unspecified, the response will contain data in [Cytoscape.js](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#cytoscape-js-json) format.
If the `file` parameter is specified, the Network View will be written to a file, and the response will contain the location of the file in the following format:
```
{
"file": "/media/HD1/myFiles/networkView.sif"
}
```
The format of the output file is defined by the extension of the `file` parameter.

* **`networkId`** SUID of the Network
* **`file`** A path to a file relative to the current directory. The format of the file written is defined by the file extension.

| Extension   | Details    |
| ----------- | -----------|
| .cys        | Cytoscape Style format |
| .xml/.xgmml | [XGMML](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html?highlight=xgmml#xgmml-format) format |
| .nnf        | [NNF](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#nnf) format |
| .sif        | [SIF](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#sif-format) format |
| .cyjs       | [Cytoscape.js](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#cytoscape-js-json) format |
-- Not required, can be None
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.deleteColumn***

**`cyclient.networks.deleteColumn(networkId, tableType, columnName, verbose=None)`**

Deletes the column specified by the `columnName` parameter from the table speficied by the `tableType` and `networkId` parameters.

* **`networkId`** SUID of the network containing the table from which to delete the column
* **`tableType`** Table Type from which to delete the column
* **`columnName`** Name of the column to delete
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.createNode***

**`cyclient.networks.createNode(networkId, body, verbose=None)`**

Adds new nodes to the network specified by the `networkId` parameter. The `name` column will be populated by the contents of the message body.

* **`networkId`** SUID of the network containing the node.
* **`body`** Array of new node names
* **`verbose`** print more

* **`returns`** 201: ; 412:

___

## ***cyclient.networks.getNeighborsSelected***

**`cyclient.networks.getNeighborsSelected(networkId, verbose=None)`**

Returns the neighbors of the nodes currently selected in the network specified by the `networkId` parameter as a list of SUIDs.
Note that this does not include the nodes in the original selection.

* **`networkId`** SUID of the network
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getImageAsPng***

**`cyclient.networks.getImageAsPng(networkId, viewId, h, verbose=None)`**

Returns a PNG image of the Network View specified by the `viewId` and `networkId` parameters.
Default size is 600 px.

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`h`** Height of the image. Width is set automatically -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: PNG image stream.

___

## ***cyclient.networks.getAdjEdges***

**`cyclient.networks.getAdjEdges(networkId, nodeId, verbose=None)`**

Returns a list of connected edges as SUIDs for the node specified by the `nodeId` and `networkId` parameters.

* **`networkId`** SUID of the network containing the node
* **`nodeId`** SUID of the node
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getNetworkVisualPropBypass***

**`cyclient.networks.getNetworkVisualPropBypass(networkId, viewId, visualProperty, verbose=None)`**

Gets the bypass Visual Property specified by the `visualProperty`, `viewId`, and `networkId` parameters.  The response is the Visual Property that is used in place of the definition provided by the Visual Style.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`visualProperty`** Name of the Visual Property
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.createColumn***

**`cyclient.networks.createColumn(networkId, tableType, body, verbose=None)`**

Creates a new, empty column in the table specified by the `tableType` parameter, in the network specified by the `networkId` parameter.
This resource can also accept an array of new columns to create multiple columns.

* **`networkId`** SUID of the Network
* **`tableType`** Table Type
* **`body`** New Column Info
* **`verbose`** print more

* **`returns`** 201: Column(s) createed; 412: Could not process column JSON

___

## ***cyclient.networks.setCurrentNetwork***

**`cyclient.networks.setCurrentNetwork(body, verbose=None)`**

Sets the current network.

* **`body`** SUID of the Network -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getNetworkView***

**`cyclient.networks.getNetworkView(networkId, viewId, file, verbose=None)`**

Gets the Network View specified by the `viewId` and `networkId` parameters.
If the `file` parameter is left unspecified, the response will contain data in [Cytoscape.js](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#cytoscape-js-json) format.
If the `file` parameter is specified, the Network View will be written to a file, and the response will contain the location of the file in the following format:
```
{
"file": "/media/HD1/myFiles/networkView.sif"
}
```
The format of the output file is defined by the extension of the `file` parameter.

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`file`** A path to a file relative to the current directory. The format of the file written is defined by the file extension.

| Extension   | Details    |
| ----------- | -----------|
| .cys        | Cytoscape Style format |
| .xml/.xgmml | [XGMML](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html?highlight=xgmml#xgmml-format) format |
| .nnf        | [NNF](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#nnf) format |
| .sif        | [SIF](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#sif-format) format |
| .cyjs       | [Cytoscape.js](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#cytoscape-js-json) format |
-- Not required, can be None
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.getTable***

**`cyclient.networks.getTable(networkId, tableType, verbose=None)`**

Returns the table specified by the `networkId` and 'tableType' parameters.

* **`networkId`** SUID of the network containing the table
* **`tableType`** Table type
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.createEdge***

**`cyclient.networks.createEdge(networkId, body, verbose=None)`**

Add new edge(s) to the network.  Body should include an array of new node names.
Returns and array of objects with fields itentifying the SUIDs of the new edges along with source and target SUIDs.

* **`networkId`** SUID of the network to add edges to.
* **`body`** Array of new edges
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getAllNetworkViews***

**`cyclient.networks.getAllNetworkViews(networkId, verbose=None)`**

Returns an array of all network views belonging to the network specified by the `networkId` paramter. The response is a list of Network SUIDs.

* **`networkId`** SUID of the Network
* **`verbose`** print more

* **`returns`** 200: An array of Network View SUIDs

___

## ***cyclient.networks.updateColumnName***

**`cyclient.networks.updateColumnName(networkId, tableType, body, verbose=None)`**

Renames an existing column in the table specified by the `tableType` and `networkId` parameters.

* **`networkId`** SUID of the network containing the table
* **`tableType`** Table Type
* **`body`** Old and new column name
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.getCurrentNetwork***

**`cyclient.networks.getCurrentNetwork(verbose=None)`**

Returns the current network.

* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.updateViews***

**`cyclient.networks.updateViews(networkId, viewId, objectType, bypass, body, verbose=None)`**

Updates multiple node or edge Visual Properties as defined by the `objectType` parameter, in the Network View specified by the `viewId` and `networkId` parameters.
Examples of Visual Properties:
```
{
"visualProperty": "NODE_BORDER_WIDTH",
"value": 2
}
```
```
{
"visualProperty": "NODE_BORDER_PAINT",
"value": "#CCCCCC"
}
```
```
{
"visualProperty": "EDGE_TRANSPARENCY",
"value": 170
}```
```
{
"visualProperty": "EDGE_PAINT",
"value": "#808080"
}```
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)
Note that this sets the Visual Properties temporarily unless the `bypass` parameter is set to `true`. If the `bypass` parameter is set to `true`, the Visual Style will be overridden by these Visual Property values. If the `bypass` parameter is not used or is set to `false`, any Visual Properties set will return to those defined in the Visual Style if the Network View is updated.

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`objectType`** Type of Object
* **`bypass`** Bypass the Visual Style with these Visual Properties -- Not required, can be None
* **`body`** A list of Objects with Visual Properties.
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.getNodes***

**`cyclient.networks.getNodes(networkId, column, query, verbose=None)`**

Returns a list of all nodes in the network specified by the `networkId` parameter as SUIDs.
If the `column` and `query` parameters are specified, the results will be limited to rows in the node table where the value in the column specified by the `column` parameter matches the value specified by the `query` parameter.

* **`networkId`** SUID of the network containing the nodes
* **`column`** The name of the column that will be queried for matches. -- Not required, can be None
* **`query`** The value to be matched. -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.putNetworkVisualPropBypass***

**`cyclient.networks.putNetworkVisualPropBypass(networkId, viewId, visualProperty, body, verbose=None)`**

Bypasses the Visual Style of the Network with the Visual Property specificed by the `visualProperty`, `viewId`, and `networkId` parameters.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`visualProperty`** Name of the Visual Property
* **`body`** A Visual Property and its value.
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.deleteNetwork***

**`cyclient.networks.deleteNetwork(networkId, verbose=None)`**

Deletes the network specified by the `networkId` parameter.

* **`networkId`** SUID of the network to delete
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.getSingleVisualPropertyValue***

**`cyclient.networks.getSingleVisualPropertyValue(networkId, viewId, objectType, objectId, visualProperty, verbose=None)`**

Gets the Visual Property specificed by the `visualProperty` parameter for the node or edge specified by the `objectId` parameter in the Network View specified by the `viewId` and `networkId` parameters.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`objectType`** Type of Object
* **`objectId`** SUID of the Object
* **`visualProperty`** Name of the Visual Property
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.deleteAllGroups***

**`cyclient.networks.deleteAllGroups(networkId, verbose=None)`**

Deletes all groups in the network specified by `networkId` parameter. The nodes and edges that the groups contained will remain present in the network, however the nodes used to identify the Groups will be deleted.

* **`networkId`** SUID of the Network
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.deleteEdge***

**`cyclient.networks.deleteEdge(networkId, edgeId, verbose=None)`**

Deletes the edge specified by the `edgeId` and `networkId` parameters.

* **`networkId`** SUID of the network containing the edge.
* **`edgeId`** SUID of the edge
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.getFirstImageAsPdf***

**`cyclient.networks.getFirstImageAsPdf(networkId, h, verbose=None)`**

Returns a PDF of the first available Network View for the Network specified by the `networkId` parameter.
Default size is 600 px

* **`networkId`** SUID of the Network
* **`h`** Height of the image. Width is set automatically -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: PDF image stream.

___

## ***cyclient.networks.getTableAsCsv***

**`cyclient.networks.getTableAsCsv(networkId, tableType, verbose=None)`**

Returns a CSV representation of the table specified by the `networkId` and `tableType` parameters. All column names are included in the first row.

* **`networkId`** SUID of the network containing the table
* **`tableType`** Table type
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getTableAsTsv***

**`cyclient.networks.getTableAsTsv(networkId, tableType, verbose=None)`**

Returns a TSV (tab delimited text) representation of the table specified by the `networkId` and `tableType` parameters. All column names are included in the first row.

* **`networkId`** SUID of the network containing the table
* **`tableType`** Table type
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.updateColumnValues***

**`cyclient.networks.updateColumnValues(networkId, tableType, columnName, default, body, verbose=None)`**

Sets the values for cells in the table specified by the `tableType` and `networkId` parameters.
If the 'default` parameter is not specified, the message body should consist of key-value pairs with which to set values.
If the `default` parameter is specified, its value will be used for every cell in the column. This is useful to set columns like "selected."

* **`networkId`** SUID of the network containing the table
* **`tableType`** The type of table
* **`columnName`** Name of the column in which to set values
* **`default`** Default Value. If this value is provided, all cells will be set to this. -- Not required, can be None
* **`body`** Array of SUID Keyed values
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.getEdgeComponent***

**`cyclient.networks.getEdgeComponent(networkId, edgeId, type, verbose=None)`**

Returns the SUID of the source or target node of the edge specified by the `edgeId` and `networkId` parameters.
Return values can be in one of two formats, depending on the value specified in the `type` parameter:
```
{
"source": 101
}
```
```
{
"target": 102
}
```

* **`networkId`** SUID of the network containing the edge
* **`edgeId`** SUID of the edge
* **`type`** The node type to return
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.getGroupCount***

**`cyclient.networks.getGroupCount(networkId, verbose=None)`**

Returns the number of groups in the network

* **`networkId`** Network SUID
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.deleteSingleVisualPropertyValueBypass***

**`cyclient.networks.deleteSingleVisualPropertyValueBypass(networkId, viewId, objectType, objectId, visualProperty, verbose=None)`**

Deletes the bypass Visual Property specified by the `visualProperty` parameter from the object specified by the `objectId` and `objectType` parameters in the Network View Specified by the `viewId` and `networkId` parameters. When this is done, the Visual Property will be defined by the Visual Style
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`networkId`** SUID of the Network
* **`viewId`** SUID of the Network View
* **`objectType`** Type of Object
* **`objectId`** SUID of Object
* **`visualProperty`** Name of the Visual Property
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.networks.deleteAllEdges***

**`cyclient.networks.deleteAllEdges(networkId, verbose=None)`**

Delete all the edges from the network specified by the `networkId` parameter.

* **`networkId`** SUID of the network to delete edges from
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.networks.getNode***

**`cyclient.networks.getNode(networkId, nodeId, verbose=None)`**

Returns a node with its associated row data.

* **`networkId`** SUID of the network containing the node
* **`nodeId`** SUID of the node
* **`verbose`** print more

* **`returns`** 200: successful operation

___

