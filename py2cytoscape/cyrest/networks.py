from .base import *

class networks(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/networks'
        self.___url=url


    def collapseGroup(self, networkId, groupNodeId, verbose=None):
        """
        Collapses the group specified by the `groupNodeId` and `networkId` parameters.

        :param networkId: SUID of the Network
        :param groupNodeId: SUID of the Node representing the Group
        :param verbose: print more

        :returns: 204: Group collapsed; 500: Failed to collapse group
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/groups/'+str(groupNodeId)+'/collapse', method="GET", verbose=verbose, parse_params=False)
        return response


    def expandGroup(self, networkId, groupNodeId, verbose=None):
        """
        Expands the group specified by the `groupNodeId` and `networkId` parameters.

        :param networkId: SUID of the Network
        :param groupNodeId: SUID of the Node representing the Group
        :param verbose: print more

        :returns: 204: Group expanded; 500: Failed to expand group
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/groups/'+str(groupNodeId)+'/expand', method="GET", verbose=verbose, parse_params=False)
        return response


    def getNetworkViewCount(self, networkId, verbose=None):
        """
        Returns a count of the Network Views available for the Network specified by the `networkId` parameter.
        
        Cytoscape can have multiple views per network model, but this feature is not exposed in the Cytoscape GUI. GUI access is limited to the first available view only.

        :param networkId: SUID of the Network
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/count', method="GET", verbose=verbose, parse_params=False)
        return response


    def getFirstImageAsPdf(self, networkId, h, verbose=None):
        """
        Returns a PDF of the first available Network View for the Network specified by the `networkId` parameter.
        
        Default size is 600 px

        :param networkId: SUID of the Network
        :param h: Height of the image. Width is set automatically -- Not required, can be None
        :param verbose: print more

        :returns: 200: PDF image stream.
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/first.pdf', PARAMS={'h':h}, method="GET", verbose=verbose, parse_params=False)
        return response


    def updateView(self, networkId, viewId, objectType, objectId, bypass, body, verbose=None):
        """
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

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param objectType: Type of Object
        :param objectId: SUID of the Object
        :param bypass: Bypass the Visual Style with these Visual Properties -- Not required, can be None
        :param body: A list of Visual Properties and their values.
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/'+str(objectType)+'/'+str(objectId)+'', method="PUT", body=body, verbose=verbose)
        return response


    def getView(self, networkId, viewId, objectType, objectId, verbose=None):
        """
        Gets a list of Visual Properties for the Object specified by the `objectId` and `objectType` parameters in the Network View specified by the `viewId` and `networkId` parameters.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param objectType: Type of Object
        :param objectId: SUID of the Object
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/'+str(objectType)+'/'+str(objectId)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def getTableAsCsv(self, networkId, tableType, verbose=None):
        """
        Returns a CSV representation of the table specified by the `networkId` and `tableType` parameters. All column names are included in the first row.

        :param networkId: SUID of the network containing the table
        :param tableType: Table type
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'.csv', method="GET", verbose=verbose, parse_params=False)
        return response


    def getNeighbours(self, networkId, nodeId, verbose=None):
        """
        Returns the neighbors of the node specified by the `nodeId` and `networkId` parameters as a list of SUIDs.

        :param networkId: SUID of the network containing the node.
        :param nodeId: SUID of the node
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/nodes/'+str(nodeId)+'/neighbors', method="GET", verbose=verbose, parse_params=False)
        return response


    def putNetworkVisualPropBypass(self, networkId, viewId, visualProperty, body, verbose=None):
        """
        Bypasses the Visual Style of the Network with the Visual Property specificed by the `visualProperty`, `viewId`, and `networkId` parameters.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param visualProperty: Name of the Visual Property
        :param body: A Visual Property and its value.
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/network/'+str(visualProperty)+'/bypass', method="PUT", body=body, verbose=verbose)
        return response


    def deleteNetworkVisualProp(self, networkId, viewId, visualProperty, verbose=None):
        """
        Deletes the bypass Visual Property specificed by the `visualProperty`, `viewId`, and `networkId` parameters. When this is done, the Visual Property will be defined by the Visual Style
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param visualProperty: Name of the Visual Property
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/network/'+str(visualProperty)+'/bypass', method="DELETE", verbose=verbose)
        return response


    def getNetworkVisualPropBypass(self, networkId, viewId, visualProperty, verbose=None):
        """
        Gets the bypass Visual Property specified by the `visualProperty`, `viewId`, and `networkId` parameters.  The response is the Visual Property that is used in place of the definition provided by the Visual Style.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param visualProperty: Name of the Visual Property
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/network/'+str(visualProperty)+'/bypass', method="GET", verbose=verbose, parse_params=False)
        return response


    def setCurrentNetwork(self, body, verbose=None):
        """
        Sets the current network.

        :param body: SUID of the Network -- Not required, can be None
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/currentNetwork', method="PUT", body=body, verbose=verbose)
        return response


    def getCurrentNetwork(self, verbose=None):
        """
        Returns the current network.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/currentNetwork', method="GET", verbose=verbose, parse_params=False)
        return response


    def getNetworkVisualProp(self, networkId, viewId, visualProperty, verbose=None):
        """
        Gets the Network Visual Property specificed by the `visualProperty`, `viewId`, and `networkId` parameters.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param visualProperty: Name of the Visual Property
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/network/'+str(visualProperty)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def createNetworkFromSelected(self, networkId, title, verbose=None):
        """
        Creates new sub-network from current selection, with the name specified by the `title` parameter.
        
        Returns the SUID of the new sub-network.

        :param networkId: SUID of the network containing the selected nodes and edges
        :param title: Name for the new sub-network -- Not required, can be None
        :param verbose: print more

        :returns: 200: successful operation
        """

        PARAMS=set_param(['networkId','title'],[networkId,title])
        response=api(url=self.___url+'networks/'+str(networkId)+'', PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def deleteNetwork(self, networkId, verbose=None):
        """
        Deletes the network specified by the `networkId` parameter.

        :param networkId: SUID of the network to delete
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'', method="DELETE", verbose=verbose)
        return response


    def getNetwork(self, networkId, verbose=None):
        """
        Returns the Network specified by the `networkId` parameter with all associated tables in [Cytoscape.js](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#cytoscape-js-json) format

        :param networkId: SUID of the Network
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'', method="H", verbose=verbose, parse_params=False)
        return response


    def updateTable(self, networkId, tableType, body, class_, verbose=None):
        """
        Updates the table specified by the `tableType` and `networkId` parameters.  New columns will be created if they do not exist in the target table.
        
        Current limitations:
        * Numbers are handled as Double
        * List column is not supported in this version

        :param networkId: SUID containing the table
        :param tableType: Type of table
        :param body: The data with which to update the table.
        :param class_: None -- Not required, can be None
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'', method="PUT", body=body, verbose=verbose)
        return response


    def getTable(self, networkId, tableType, verbose=None):
        """
        Returns the table specified by the `networkId` and 'tableType' parameters.

        :param networkId: SUID of the network containing the table
        :param tableType: Table type
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'', method="H", verbose=verbose, parse_params=False)
        return response


    def getSingleVisualPropertyValue(self, networkId, viewId, objectType, objectId, visualProperty, verbose=None):
        """
        Gets the Visual Property specificed by the `visualProperty` parameter for the node or edge specified by the `objectId` parameter in the Network View specified by the `viewId` and `networkId` parameters.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param objectType: Type of Object
        :param objectId: SUID of the Object
        :param visualProperty: Name of the Visual Property
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/'+str(objectType)+'/'+str(objectId)+'/'+str(visualProperty)+'', method="H", verbose=verbose, parse_params=False)
        return response


    def updateViews(self, networkId, viewId, objectType, bypass, body, verbose=None):
        """
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

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param objectType: Type of Object
        :param bypass: Bypass the Visual Style with these Visual Properties -- Not required, can be None
        :param body: A list of Objects with Visual Properties.
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/'+str(objectType)+'', method="PUT", body=body, verbose=verbose)
        return response


    def getViews(self, networkId, viewId, objectType, visualProperty, verbose=None):
        """
        Returns a list of all Visual Property values for the Visual Property specified by the `visualProperty` and `objectType` parameters, in the Network View specified by the `viewId` and `networkId` parameters.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param objectType: Type of Object
        :param visualProperty: Name of the Visual Property -- Not required, can be None
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/'+str(objectType)+'', PARAMS={'visualProperty':visualProperty}, method="H", verbose=verbose, parse_params=False)
        return response


    def getTableAsTsv(self, networkId, tableType, verbose=None):
        """
        Returns a TSV (tab delimited text) representation of the table specified by the `networkId` and `tableType` parameters. All column names are included in the first row.

        :param networkId: SUID of the network containing the table
        :param tableType: Table type
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'.tsv', method="G", verbose=verbose, parse_params=False)
        return response


    def getNetworkViewAsCx(self, networkId, viewId, verbose=None):
        """
        Returns the Network View specified by the `viewId` and `networkId` parameters in [CX format](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#cytoscape-cx)

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'.cx', method="G", verbose=verbose, parse_params=False)
        return response


    def getImageAsPdf(self, networkId, viewId, verbose=None):
        """
        Returns a PDF of the Network View specified by the `viewId` and `networkId` parameters.
        
        Default size is 500 px.

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param verbose: print more

        :returns: 200: PDF image stream.
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'.pdf', method="G", verbose=verbose, parse_params=False)
        return response


    def getNetworkPointer(self, networkId, nodeId, verbose=None):
        """
        If the node specified by the `nodeId` and `networkId` parameters has an associated nested network, returns the SUID of the nested network.

        :param networkId: SUID of the network containing the node
        :param nodeId: SUID of the node
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/nodes/'+str(nodeId)+'/pointer', method="GET", verbose=verbose, parse_params=False)
        return response


    def getTables(self, networkId, verbose=None):
        """
        Returns every table in the network specified by the `networkId` parameter.

        :param networkId: SUID of the Network
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables', method="GET", verbose=verbose, parse_params=False)
        return response


    def updateColumnName(self, networkId, tableType, body, verbose=None):
        """
        Renames an existing column in the table specified by the `tableType` and `networkId` parameters.

        :param networkId: SUID of the network containing the table
        :param tableType: Table Type
        :param body: Old and new column name
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'/columns', method="PUT", body=body, verbose=verbose)
        return response


    def createColumn(self, networkId, tableType, body, verbose=None):
        """
        Creates a new, empty column in the table specified by the `tableType` parameter, in the network specified by the `networkId` parameter.
        
        This resource can also accept an array of new columns to create multiple columns.

        :param networkId: SUID of the Network
        :param tableType: Table Type
        :param body: New Column Info
        :param verbose: print more

        :returns: 201: Column(s) createed; 412: Could not process column JSON
        """

        PARAMS=set_param(['networkId','tableType','body'],[networkId,tableType,body])
        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'/columns', PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def getColumnNames(self, networkId, tableType, verbose=None):
        """
        Returns all the columns in the table specified by the `networkId` and `tableType` parameters.

        :param networkId: SUID of the network containing the table
        :param tableType: Table Type
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'/columns', method="GET", verbose=verbose, parse_params=False)
        return response


    def getRow(self, networkId, tableType, primaryKey, verbose=None):
        """
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

        :param networkId: SUID of the network containing the table
        :param tableType: Table type
        :param primaryKey: Primary key of the row Object, normally an SUID
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'/rows/'+str(primaryKey)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def getEdgeDirected(self, networkId, edgeId, verbose=None):
        """
        Returns true if the edge specified by the `edgeId` and `networkId` parameters is directed.

        :param networkId: SUID of the network containing the edge
        :param edgeId: SUID of the edge
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/edges/'+str(edgeId)+'/isDirected', method="GET", verbose=verbose, parse_params=False)
        return response


    def getNetworkCount(self, verbose=None):
        """
        Returns the number of networks in current Cytoscape session.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/count', method="GET", verbose=verbose, parse_params=False)
        return response


    def getNetworkView(self, networkId, viewId, file, verbose=None):
        """
        Gets the Network View specified by the `viewId` and `networkId` parameters.
        
        If the `file` parameter is left unspecified, the response will contain data in [Cytoscape.js](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#cytoscape-js-json) format.
        
        If the `file` parameter is specified, the Network View will be written to a file, and the response will contain the location of the file in the following format:
        
        ```
        
        {
        "file": "/media/HD1/myFiles/networkView.sif"
        }
        ```
        
        The format of the output file is defined by the extension of the `file` parameter.

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param file: A path to a file relative to the current directory. The format of the file written is defined by the file extension.

    | Extension   | Details    |
    | ----------- | -----------|
    | .cys        | Cytoscape Style format |
    | .xml/.xgmml | [XGMML](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html?highlight=xgmml#xgmml-format) format |
    | .nnf        | [NNF](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#nnf) format |
    | .sif        | [SIF](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#sif-format) format |
    | .cyjs       | [Cytoscape.js](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#cytoscape-js-json) format |
    -- Not required, can be None
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'', PARAMS={'file':file}, method="GET", verbose=verbose, parse_params=False)
        return response


    def putSingleVisualPropertyValueBypass(self, networkId, viewId, objectType, objectId, visualProperty, body, verbose=None):
        """
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

        :param networkId: Network SUID
        :param viewId: Network View SUID
        :param objectType: Type of Object
        :param objectId: SUID of the Object
        :param visualProperty: Name of the Visual Property
        :param body: A Visual Property and its value.
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/'+str(objectType)+'/'+str(objectId)+'/'+str(visualProperty)+'/bypass', method="PUT", body=body, verbose=verbose)
        return response


    def deleteSingleVisualPropertyValueBypass(self, networkId, viewId, objectType, objectId, visualProperty, verbose=None):
        """
        Deletes the bypass Visual Property specified by the `visualProperty` parameter from the object specified by the `objectId` and `objectType` parameters in the Network View Specified by the `viewId` and `networkId` parameters. When this is done, the Visual Property will be defined by the Visual Style
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param objectType: Type of Object
        :param objectId: SUID of Object
        :param visualProperty: Name of the Visual Property
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/'+str(objectType)+'/'+str(objectId)+'/'+str(visualProperty)+'/bypass', method="DELETE", verbose=verbose)
        return response


    def getSingleVisualPropertyValueBypass(self, networkId, viewId, objectType, objectId, visualProperty, verbose=None):
        """
        Gets the bypass Visual Property specified by the `visualProperty` parameter from the object specified by the `objectId` and `objectType` parameters in the Network View Specified by the `viewId` and `networkId` parameters. The response is the Visual Property that is used in place of the definition provided by the Visual Style.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param networkId: Network SUID
        :param viewId: Network View SUID
        :param objectType: Type of Object
        :param objectId: SUID of the Object
        :param visualProperty: Name of the Visual Property
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/'+str(objectType)+'/'+str(objectId)+'/'+str(visualProperty)+'/bypass', method="GET", verbose=verbose, parse_params=False)
        return response


    def deleteNode(self, networkId, nodeId, verbose=None):
        """
        Deletes the node specified by the `nodeId` and `networkId` parameters.

        :param networkId: SUID of the network containing the node.
        :param nodeId: SUID of the node
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/nodes/'+str(nodeId)+'', method="DELETE", verbose=verbose)
        return response


    def getNode(self, networkId, nodeId, verbose=None):
        """
        Returns a node with its associated row data.

        :param networkId: SUID of the network containing the node
        :param nodeId: SUID of the node
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/nodes/'+str(nodeId)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def createEdge(self, networkId, body, verbose=None):
        """
        Add new edge(s) to the network.  Body should include an array of new node names.
        
        Returns and array of objects with fields itentifying the SUIDs of the new edges along with source and target SUIDs.

        :param networkId: SUID of the network to add edges to.
        :param body: Array of new edges
        :param verbose: print more

        :returns: 200: successful operation
        """

        PARAMS=set_param(['networkId','body'],[networkId,body])
        response=api(url=self.___url+'networks/'+str(networkId)+'/edges', PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def deleteAllEdges(self, networkId, verbose=None):
        """
        Delete all the edges from the network specified by the `networkId` parameter.

        :param networkId: SUID of the network to delete edges from
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/edges', method="DELETE", verbose=verbose)
        return response


    def getEdges(self, networkId, column, query, verbose=None):
        """
        Returns a list of all edges in the network specified by the `networkId` parameter as SUIDs.
        
        If the `column` and `query` parameters are specified, the results will be limited to rows in the edge table where the value in the column specified by the `column` parameter matches the value specified by the `query` parameter.

        :param networkId: SUID of the network containing the edges
        :param column: The name of the column that will be queried for matches. -- Not required, can be None
        :param query: The value to be matched. -- Not required, can be None
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/edges', PARAMS={'column':column, 'query':query}, method="GET", verbose=verbose, parse_params=False)
        return response


    def setSelectedEdges(self, networkId, body, verbose=None):
        """
        Sets as selected the edges specified by the `suids` and `networkId` parameters.
        
        Returns a list of selected SUIDs.

        :param networkId: SUID of the network containing the edges
        :param body: Array of edge SUIDs to select -- Not required, can be None
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/edges/selected', method="PUT", body=body, verbose=verbose)
        return response


    def getSelectedEdges(self, networkId, verbose=None):
        """
        Gets the selected edges in the network specified by the `networkId` parameter. The results are presented as a list of SUIDs.

        :param networkId: SUID of the network containing the edges
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/edges/selected', method="GET", verbose=verbose, parse_params=False)
        return response


    def getFirstImageAsPng(self, networkId, h, verbose=None):
        """
        Returns a PNG image of the first available Network View for the Network specified by the `networkId` parameter.
        
        Default size is 600 px

        :param networkId: SUID of the Network
        :param h: Height of the image. Width is set automatically -- Not required, can be None
        :param verbose: print more

        :returns: 200: PNG image stream.
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/first.png', PARAMS={'h':h}, method="GET", verbose=verbose, parse_params=False)
        return response


    def getCell(self, networkId, tableType, primaryKey, columnName, verbose=None):
        """
        Return the value of a cell specified by the `primaryKey` and `columnName` parameters in the table specified by the `tableType` and `networkId` parameters.
        
        Returns a JSON representation of a String, Boolean, Number, or List.

        :param networkId: SUID of the network containing the table
        :param tableType: Table type
        :param primaryKey: Primary key of the row Object, normally an SUID
        :param columnName: Name of the Column
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'/rows/'+str(primaryKey)+'/'+str(columnName)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def setSelectedNodes(self, networkId, body, verbose=None):
        """
        Sets as selected the nodes specified by the `suids` and `networkId` parameters.
        
        Returns a list of selected SUIDs.

        :param networkId: SUID of the network containing the nodes
        :param body: Array of node SUIDs to select -- Not required, can be None
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/nodes/selected', method="PUT", body=body, verbose=verbose)
        return response


    def getSelectedNodes(self, networkId, verbose=None):
        """
        Gets the selected nodes in the network specified by the `networkId` parameter. The results are presented as a list of SUIDs.

        :param networkId: SUID of the network containing the nodes
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/nodes/selected', method="GET", verbose=verbose, parse_params=False)
        return response


    def deleteGroup(self, networkId, groupNodeId, verbose=None):
        """
        Deletes the group specified by the `groupNodeId` and `networkId` parameters. The nodes and edges that the group contained will remain present in the network, however the node used to identify the Group will be deleted.

        :param networkId: SUID of the Network
        :param groupNodeId: SUID of the Node representing the Group
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/groups/'+str(groupNodeId)+'', method="DELETE", verbose=verbose)
        return response


    def getGroup(self, networkId, groupNodeId, verbose=None):
        """
        Returns the group specified by the `groupNodeId` and `networkId` parameters.

        :param networkId: SUID of the Network
        :param groupNodeId: SUID of the Node representing the Group
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/groups/'+str(groupNodeId)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def getEdgeCount(self, networkId, verbose=None):
        """
        Returns the number of edges in the network specified by the `networkId` parameter.

        :param networkId: SUID of the network containing the edges
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/edges/count', method="GET", verbose=verbose, parse_params=False)
        return response


    def updateColumnValues(self, networkId, tableType, columnName, default, body, verbose=None):
        """
        Sets the values for cells in the table specified by the `tableType` and `networkId` parameters.
        
        If the 'default` parameter is not specified, the message body should consist of key-value pairs with which to set values.
        
        If the `default` parameter is specified, its value will be used for every cell in the column. This is useful to set columns like "selected."

        :param networkId: SUID of the network containing the table
        :param tableType: The type of table
        :param columnName: Name of the column in which to set values
        :param default: Default Value. If this value is provided, all cells will be set to this. -- Not required, can be None
        :param body: Array of SUID Keyed values
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'/columns/'+str(columnName)+'', method="PUT", body=body, verbose=verbose)
        return response


    def deleteColumn(self, networkId, tableType, columnName, verbose=None):
        """
        Deletes the column specified by the `columnName` parameter from the table speficied by the `tableType` and `networkId` parameters.

        :param networkId: SUID of the network containing the table from which to delete the column
        :param tableType: Table Type from which to delete the column
        :param columnName: Name of the column to delete
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'/columns/'+str(columnName)+'', method="DELETE", verbose=verbose)
        return response


    def getColumnValues(self, networkId, tableType, columnName, verbose=None):
        """
        Returns all the values for the column specified by the `columnType` parameter, in the table specified by the `networkId` and `tableType` parameters.

        :param networkId: SUID of the Network
        :param tableType: Type of Table
        :param columnName: Name of the Column
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'/columns/'+str(columnName)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def createNode(self, networkId, body, verbose=None):
        """
        Adds new nodes to the network specified by the `networkId` parameter. The `name` column will be populated by the contents of the message body.

        :param networkId: SUID of the network containing the node.
        :param body: Array of new node names
        :param verbose: print more

        :returns: 201: ; 412: 
        """

        PARAMS=set_param(['networkId','body'],[networkId,body])
        response=api(url=self.___url+'networks/'+str(networkId)+'/nodes', PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def deleteAllNodes(self, networkId, verbose=None):
        """
        Delete all the nodes from the network specified by the `networkId` parameter.

        :param networkId: SUID of the network to delete nodes from
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/nodes', method="DELETE", verbose=verbose)
        return response


    def getNodes(self, networkId, column, query, verbose=None):
        """
        Returns a list of all nodes in the network specified by the `networkId` parameter as SUIDs.
        
        If the `column` and `query` parameters are specified, the results will be limited to rows in the node table where the value in the column specified by the `column` parameter matches the value specified by the `query` parameter.

        :param networkId: SUID of the network containing the nodes
        :param column: The name of the column that will be queried for matches. -- Not required, can be None
        :param query: The value to be matched. -- Not required, can be None
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/nodes', PARAMS={'column':column, 'query':query}, method="GET", verbose=verbose, parse_params=False)
        return response


    def setCurrentNetworkView(self, body, verbose=None):
        """
        Sets the current Network View.

        :param body: SUID of the Network View -- Not required, can be None
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/views/currentNetworkView', method="PUT", body=body, verbose=verbose)
        return response


    def getCurrentNetworkView(self, verbose=None):
        """
        Returns the current Network View.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/views/currentNetworkView', method="GET", verbose=verbose, parse_params=False)
        return response


    def getGroupCount(self, networkId, verbose=None):
        """
        Returns the number of groups in the network

        :param networkId: Network SUID
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/groups/count', method="GET", verbose=verbose, parse_params=False)
        return response


    def deleteEdge(self, networkId, edgeId, verbose=None):
        """
        Deletes the edge specified by the `edgeId` and `networkId` parameters.

        :param networkId: SUID of the network containing the edge.
        :param edgeId: SUID of the edge
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/edges/'+str(edgeId)+'', method="DELETE", verbose=verbose)
        return response


    def getEdge(self, networkId, edgeId, verbose=None):
        """
        Returns an edge with its associated row data.

        :param networkId: SUID of the network containing the edge
        :param edgeId: SUID of the edge
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/edges/'+str(edgeId)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def getRows(self, networkId, tableType, verbose=None):
        """
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

        :param networkId: SUID of the network containing the table
        :param tableType: Table Type
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/tables/'+str(tableType)+'/rows', method="GET", verbose=verbose, parse_params=False)
        return response


    def getNodeCount(self, networkId, verbose=None):
        """
        Returns the number of nodes in the network specified by the `networkId` parameter.

        :param networkId: SUID of the network containing the nodes
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/nodes/count', method="GET", verbose=verbose, parse_params=False)
        return response


    def getNeighborsSelected(self, networkId, verbose=None):
        """
        Returns the neighbors of the nodes currently selected in the network specified by the `networkId` parameter as a list of SUIDs.
        
        Note that this does not include the nodes in the original selection.

        :param networkId: SUID of the network
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/nodes/selected/neighbors', method="GET", verbose=verbose, parse_params=False)
        return response


    def deleteFirstNetworkView(self, networkId, verbose=None):
        """
        Deletes the first available Network View for the Network specified by the `networkId` parameter. Cytoscape can have multiple views per network model, but this feature is not exposed in the Cytoscape GUI. GUI access is limited to the first available view only.

        :param networkId: SUID of the Network
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/first', method="DELETE", verbose=verbose)
        return response


    def getFirstNetworkView(self, networkId, file, verbose=None):
        """
        This returns the first view of the network. Cytoscape can have multiple views per network model, but this feature is not exposed in the Cytoscape GUI. GUI access is limited to the first available view only.
        
        If the `file` parameter is left unspecified, the response will contain data in [Cytoscape.js](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#cytoscape-js-json) format.
        
        If the `file` parameter is specified, the Network View will be written to a file, and the response will contain the location of the file in the following format:
        
        ```
        
        {
        "file": "/media/HD1/myFiles/networkView.sif"
        }
        ```
        
        The format of the output file is defined by the extension of the `file` parameter.

        :param networkId: SUID of the Network
        :param file: A path to a file relative to the current directory. The format of the file written is defined by the file extension.

    | Extension   | Details    |
    | ----------- | -----------|
    | .cys        | Cytoscape Style format |
    | .xml/.xgmml | [XGMML](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html?highlight=xgmml#xgmml-format) format |
    | .nnf        | [NNF](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#nnf) format |
    | .sif        | [SIF](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#sif-format) format |
    | .cyjs       | [Cytoscape.js](http://manual.cytoscape.org/en/stable/Supported_Network_File_Formats.html#cytoscape-js-json) format |
    -- Not required, can be None
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/first', PARAMS={'file':file}, method="GET", verbose=verbose, parse_params=False)
        return response


    def getAdjEdges(self, networkId, nodeId, verbose=None):
        """
        Returns a list of connected edges as SUIDs for the node specified by the `nodeId` and `networkId` parameters.

        :param networkId: SUID of the network containing the node
        :param nodeId: SUID of the node
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/nodes/'+str(nodeId)+'/adjEdges', method="GET", verbose=verbose, parse_params=False)
        return response


    def createNetworkView(self, networkId, verbose=None):
        """
        Creates a new Network View for the Network specified by the `networkId` parameter.

        :param networkId: SUID of the Network
        :param verbose: print more

        :returns: 201: Network View SUID
        """

        PARAMS=set_param(['networkId'],[networkId])
        response=api(url=self.___url+'networks/'+str(networkId)+'/views', PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def deleteAllNetworkViews(self, networkId, verbose=None):
        """
        Deletes all Network Views available in the Network specified by the `networkId` parameter. Cytoscape can have multiple views per network model, but this feature is not exposed in the Cytoscape GUI. GUI access is limited to the first available view only.

        :param networkId: SUID of the Network
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views', method="DELETE", verbose=verbose)
        return response


    def getAllNetworkViews(self, networkId, verbose=None):
        """
        Returns an array of all network views belonging to the network specified by the `networkId` paramter. The response is a list of Network SUIDs.

        :param networkId: SUID of the Network
        :param verbose: print more

        :returns: 200: An array of Network View SUIDs
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views', method="GET", verbose=verbose, parse_params=False)
        return response


    def getEdgeComponent(self, networkId, edgeId, type, verbose=None):
        """
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

        :param networkId: SUID of the network containing the edge
        :param edgeId: SUID of the edge
        :param type: The node type to return
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/edges/'+str(edgeId)+'/'+str(type)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def updateNetworkView(self, networkId, viewId, bypass, body, verbose=None):
        """
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

        :param networkId: Network SUID
        :param viewId: Network View SUID
        :param bypass: Bypass the Visual Style with these properties -- Not required, can be None
        :param body: A list of Visual Properties and their values.
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/network', method="PUT", body=body, verbose=verbose)
        return response


    def getNetworkVisualProps(self, networkId, viewId, verbose=None):
        """
        Returns a list of the Visual Properties for the Network View specified by the `viewId` and `networkId` parameters.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'/network', method="GET", verbose=verbose, parse_params=False)
        return response


    def createGroup(self, networkId, body, verbose=None):
        """
        Create a new group in the network specified by the parameter `networkId`. The contents are specified the message body.

        :param networkId: SUID of the Network
        :param body: New Group name and contents
        :param verbose: print more

        :returns: 200: successful operation
        """

        PARAMS=set_param(['networkId','body'],[networkId,body])
        response=api(url=self.___url+'networks/'+str(networkId)+'/groups', PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def deleteAllGroups(self, networkId, verbose=None):
        """
        Deletes all groups in the network specified by `networkId` parameter. The nodes and edges that the groups contained will remain present in the network, however the nodes used to identify the Groups will be deleted.

        :param networkId: SUID of the Network
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/groups', method="DELETE", verbose=verbose)
        return response


    def getAllGroups(self, networkId, verbose=None):
        """
        Returns a list of all the groups in the network specified by the `networkId` parameter.

        :param networkId: Network SUID
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/groups', method="GET", verbose=verbose, parse_params=False)
        return response


    def getImageAsSvg(self, networkId, viewId, h, verbose=None):
        """
        Returns an SVG image of the Network View specified by the `viewId` and `networkId` parameters.
        
        Default size is 600 px.

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param h: Height of the image. Width is set automatically -- Not required, can be None
        :param verbose: print more

        :returns: 200: SVG image stream.
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'.svg', PARAMS={'h':h}, method="GET", verbose=verbose, parse_params=False)
        return response


    def getImageAsPng(self, networkId, viewId, h, verbose=None):
        """
        Returns a PNG image of the Network View specified by the `viewId` and `networkId` parameters.
        
        Default size is 600 px.

        :param networkId: SUID of the Network
        :param viewId: SUID of the Network View
        :param h: Height of the image. Width is set automatically -- Not required, can be None
        :param verbose: print more

        :returns: 200: PNG image stream.
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/'+str(viewId)+'.png', PARAMS={'h':h}, method="GET", verbose=verbose, parse_params=False)
        return response


    def getFirstImageAsSvg(self, networkId, h, verbose=None):
        """
        Returns an SVG image of the first available Network View for the Network specified by the `networkId` parameter.
        
        Default size is 600 px

        :param networkId: SUID of the Network
        :param h: Height of the image. Width is set automatically -- Not required, can be None
        :param verbose: print more

        :returns: 200: SVG image stream.
        """

        response=api(url=self.___url+'networks/'+str(networkId)+'/views/first.svg', PARAMS={'h':h}, method="GET", verbose=verbose, parse_params=False)
        return response

