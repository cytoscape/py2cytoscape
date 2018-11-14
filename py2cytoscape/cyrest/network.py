from .base import *

class network(object):
    """
    cytoscape network interface as shown in CyREST's swagger documentation for 'network'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/network'

    def add(self, edgeList=None, network=None, nodeList=None, verbose=False):
        """
        Adds nodes and edges to an existing network. The nodes and edges to be
        added must already exist in the network collection. This command is
        most often used to populate a subnetwork with selected nodes and edges
        from a parent network.

        :param edgeList: (string, optional), Specifies a list of edges. The
            keywords all, selected, or unselected can be used to specify edges
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list
            of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param network: (string, optional), Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank value
            can also be used to specify the current network.
        :param nodeList: (string, optional), Specifies a list of nodes. The keywords all,
            selected, or unselected can be used to specify nodes by their selection
            state. The pattern COLUMN:VALUE sets this parameter to any rows that
            contain the specified column value; if the COLUMN prefix is not used,
            the NAME column is matched by default. A list of COLUMN:VALUE pairs of
            the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to match multiple
            values.
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["edgeList","network","nodeList"],[edgeList,network,nodeList])
        response=api(url=self.__url+"/add", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def add_edge(self, isDirected=None,name=None,network=None,sourceName=None,targetName=None, verbose=False):
        """
        Add a new edge between two existing nodes in a network. The names of the
        nodes must be specified and much match the value in the 'name' column for
        each node.

        :param isDirected (string, optional): Whether the edge should be directed
            or not. Even though all edges in Cytoscape have a source and target, by
            default they are treated as undirected. Setting this to 'true' will
            flag some algorithms to treat them as directed, although many current
            implementations will ignore this flag.
        :param name (string, optional): Set the 'name' and 'shared name' columns
            for this edge to the provided value. ,
        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value can
            also be used to specify the current network.
        :param sourceName (string): Enter the name of an existing node in the
            network to be the source of the edge. Note that this is the name as
            defined in the 'name' column of the network.
        :param targetName (string): Enter the name of an existing node in the
            network to be the target of the edge. Note that this is the name as
            defined in the 'name' column of the network.
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["isDirected","name","network","sourceName","targetName"],\
        [isDirected,name,network,sourceName,targetName])
        response=api(url=self.__url+"/add edge", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    

    def add_node(self, name=None,network=None, verbose=False):
        """
        Add a new node to an existing network. The name of the node must be provided.

        :param name (string, optional): The name of the node, which will be assigned
            to both the 'name' and 'shared name' columns
        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value can
            also be used to specify the current network.
        :param verbose: print more

        :returns: node SUID
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["name","network"],[name,network])
        response=api(url=self.__url+"/add node", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def clone(self, network=None, verbose=False):
        """
        Create a new network by cloning an existing network. The new network will
        be created as part of a new network collection. The SUID of the new network
        and view (if one is created) are returned.

        :param name (string, optional): The name of the node, which will be assigned
            to both the 'name' and 'shared name' columns
        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value can
            also be used to specify the current network.
        :param verbose: print more

        :returns: { network, view }
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network"], [network])
        response=api(url=self.__url+"/clone", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def connect_nodes(self, network=None, nodes=None, verbose=False):
        """
        Create new edges that connect a list of nodes.

        :param network (string): Specifies a network by name, or by SUID if the
            prefix SUID: is used. The keyword CURRENT, or a blank value can also be
            used to specify the current network.
        :param nodes (string): Specifies a list of nodes. The keywords all,
            selected, or unselected can be used to specify nodes by their selection
            state. The pattern COLUMN:VALUE sets this parameter to any rows that
            contain the specified column value; if the COLUMN prefix is not used,
            the NAME column is matched by default. A list of COLUMN:VALUE pairs of
            the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to match multiple values.
        :param verbose: print more

        :returns: [ list of generated edges ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["nodes","network"],[nodes,network])
        response=api(url=self.__url+"/connect nodes", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def create(self, edgeList=None, excludeEdges=None, networkName=None, nodeList=None, source=None, verbose=False):
        """
        Create a new network from a list of nodes and edges in an existing source network.
        The SUID of the network and view are returned.

        :param edgeList (string, optional): Specifies a list of edges. The keywords
            all, selected, or unselected can be used to specify edges by their
            selection state. The pattern COLUMN:VALUE sets this parameter to any
            rows that contain the specified column value; if the COLUMN prefix is
            not used, the NAME column is matched by default. A list of COLUMN:VALUE
            pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to
            match multiple values.
        :param excludeEdges (string, optional): Unless this is set to true, edges
            that connect nodes in the nodeList are implicitly included
        :param networkName (string, optional):
        :param nodeList (string, optional): Specifies a list of nodes. The keywords
            all, selected, or unselected can be used to specify nodes by their
            selection state. The pattern COLUMN:VALUE sets this parameter to any
            rows that contain the specified column value; if the COLUMN prefix is
            not used, the NAME column is matched by default. A list of COLUMN:VALUE
            pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to
            match multiple values.
        :param source (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value can
            also be used to specify the current network.
        :param verbose: print more

        :returns: { netowrk, view }
        """
        network=check_network(self,source, verbose=verbose)
        PARAMS=set_param(["edgeList","excludeEdges","networkName","nodeList","source"], \
        [edgeList,excludeEdges,networkName,nodeList,network])
        response=api(url=self.__url+"/create", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def create_attribute(self, column=None, listType=None, namespace=None, network=None, atype=None, verbose=False):
        """
        Creates a new network column.

        :param column (string, optional): Unique name of column
        :param listType (string, optional): Can be one of integer, long, double,
            or string. = ['integer', 'long', 'double', 'string', 'boolean']
        :param namespace (string, optional): Node, Edge, and Network objects
            support the default, local, and hidden namespaces. Root networks also
            support the shared namespace. Custom namespaces may be specified
            by Apps.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank value
            can also be used to specify the current network.
        :param atype (string, optional): Can be one of integer, long, double,
            string, or list. = ['integer', 'long', 'double', 'string', 'boolean',
            'list']
        :param verbose: print more

        :returns: { columnName }
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["column","listType","namespace","network","type"], \
        [column,listType,namespace,network,atype])
        response=api(url=self.__url+"/create attribute", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    

    def create_empty(self, name=None, renderers=None, RootNetworkList=None, verbose=False):
        """
        Create a new, empty network. The new network may be created as part of
        an existing network collection or a new network collection.

        :param name (string, optional): Enter the name of the new network.
        :param renderers (string, optional): Select the renderer to use for the
            new network view. By default, the standard Cytoscape 2D renderer (Ding)
            will be used = [''],
        :param RootNetworkList (string, optional): Choose the network collection
            the new network should be part of. If no network collection is selected,
            a new network collection is created. = [' -- Create new network collection --',
            'cy:command_documentation_generation']
        :param verbose: print more
        """
        PARAMS=set_param(["name","renderers","RootNetworkList"],[name,renderers,RootNetworkList])
        response=api(url=self.__url+"/create empty", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    

    def delete(self, edgeList=None, network=None, nodeList=None, verbose=False):
        """
        Deletes nodes and edges provided by the arguments, or if no nodes or edges are provides,
        the selected nodes and edges. When deleting nodes, adjacent edges are also deleted.

        :param edgeList (string, optional): Specifies a list of edges. The keywords
            all, selected, or unselected can be used to specify edges by their
            selection state. The pattern COLUMN:VALUE sets this parameter to any
            rows that contain the specified column value; if the COLUMN prefix is
            not used, the NAME column is matched by default. A list of COLUMN:VALUE
            pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to match
            multiple values.
        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value can
            also be used to specify the current network.
        :param nodeList (string, optional): Specifies a list of nodes. The keywords all,
            selected, or unselected can be used to specify nodes by their selection state.
            The pattern COLUMN:VALUE sets this parameter to any rows that contain the specified
            column value; if the COLUMN prefix is not used, the NAME column is matched by default.
            A list of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be
            used to match multiple values.
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["edgeList","network","nodeList"],[edgeList,network,nodeList])
        response=api(url=self.__url+"/delete", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def deselect(self, edgeList=None, network=None, nodeList=None, verbose=False):
        """
        Deselect nodes and/or edges in a network. A list of nodes and/or edges
        may be provided and those nodes and edges will be deselected.

        :param edgeList (string, optional): Specifies a list of edges. The keywords all,
            selected, or unselected can be used to specify edges by their selection state.
            The pattern COLUMN:VALUE sets this parameter to any rows that contain the
            specified column value; if the COLUMN prefix is not used, the NAME column
            is matched by default. A list of COLUMN:VALUE pairs of the format
            COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to match multiple values.
        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value can
            also be used to specify the current network.
        :param nodeList (string, optional): Specifies a list of nodes. The keywords
            all, selected, or unselected can be used to specify nodes by their
            selection state. The pattern COLUMN:VALUE sets this parameter to any
            rows that contain the specified column value; if the COLUMN prefix is
            not used, the NAME column is matched by default. A list of COLUMN:VALUE
            pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to
            match multiple values.
        :param verbose: print more

        :retunrs: [ list of deselected nodes and edges ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["edgeList","network","nodeList"],[edgeList,network,nodeList])
        response=api(url=self.__url+"/deselect", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def destroy(self, network=None, verbose=False):
        """
        Destroy (delete) a network. The SUID of the destroyed network is returned.

        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value can
            also be used to specify the current network.
        :param verbose: print more

        :returns: id of destroyed network
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network"],[network])
        response=api(url=self.__url+"/destroy", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def export(self, options=None, OutputFile=None, verbose=False):
        """
        Export a network to a network file (e.g. XGMML, SIF, etc.)

        :param options (string, optional): The format of the output file. = ['CX JSON (*.cx)',
            'Cytoscape.js JSON (*.cyjs)', 'GraphML files (*.graphml, *.xml)', 'NNF (*.nnf)',
            'PSI-MI Level 1', 'PSI-MI Level 2.5', 'SIF (*.sif)', 'XGMML (*.xgmml, *.xml)']
        :param OutputFile (string, optional):
        :param verbose: print more

        :returns: { file }
        """
        PARAMS=set_param(["options","OutputFile"],[options,OutputFile])
        response=api(url=self.__url+"/export", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def get(self, network=None, verbose=False):
        """
        Specifies a network by name, or by SUID if the prefix SUID: is used.
        The keyword CURRENT, or a blank value can also be used to specify the
        current network.

        This function sets the self.network.network_name and
        self.network.network_suid of a cyclient object.

        :param network: network (string, optional): Specifies a network by name,
            or by SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        :returns: { dictionary with values for the respective network }
        """

        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network"],[network])
        response=api(url=self.__url+"/get", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def get_attribute(self, columnList=None, namespace=None, network=None, verbose=False):
        """
        Returns the attributes for the network passed as parameter.

        :param columnList (string, optional): A list of column names, separated by commas.
        :param namespace (string, optional): Node, Edge, and Network objects support
            the default, local, and hidden namespaces. Root networks also support the
            shared namespace. Custom namespaces may be specified by Apps.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        :returns: { attributes for the network passed in column list }
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["columnList","namespace","network"],[columnList,namespace,network])
        response=api(url=self.__url+"/get attribute", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def get_porperties(self, network=None, propertyList=None, verbose=False):
        """
        Returns the visual properties for the network that matches the passed parameters.

        :param network (string): Specifies a network by name, or by SUID if the
            prefix SUID: is used. The keyword CURRENT, or a blank value can also
            be used to specify the current network.
        :param propertyList (string): A comma-separated list of network properties
        :param verbose: print more

        :returns: visual properties for the network that matches the passed parameters
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network","propertyList"],[network,propertyList])
        response=api(url=self.__url+"/get properties", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def hide(self, edgeList=None, network=None, nodeList=None, verbose=False):
        """
        Hide nodes and/or edges in a network. A list of nodes and/or edges may
        be provided and those nodes and edges will be hidden in the view associated
        with the provided network.Note that the network '''must''' have a view.
        The SUIDs of the hidden nodes and/or edges are returned.

        :param edgeList (string, optional): Specifies a list of edges. The keywords
            all, selected, or unselected can be used to specify edges by their
            selection state. The pattern COLUMN:VALUE sets this parameter to any
            rows that contain the specified column value; if the COLUMN prefix is
            not used, the NAME column is matched by default. A list of COLUMN:VALUE
            pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to
            match multiple values.
        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value can
            also be used to specify the current network.
        :param nodeList (string, optional): Specifies a list of nodes. The keywords
            all, selected, or unselected can be used to specify nodes by their
            selection state. The pattern COLUMN:VALUE sets this parameter to any
            rows that contain the specified column value; if the COLUMN prefix is
            not used, the NAME column is matched by default. A list of COLUMN:VALUE
            pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to
            match multiple values.
        :param verbose: print more

        :returns: [ list of SUIDs of the hidden nodes and/or edges ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network","edgeList","nodeList"],[network,edgeList,nodeList])
        response=api(url=self.__url+"/hide", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def import_file(self, dataTypeList=None, defaultInteraction=None, delimiters=None, \
        delimitersForDataList=None, afile=None, firstRowAsColumnNames=None, \
        indexColumnSourceInteraction=None, indexColumnTargetInteraction=None, indexColumnTypeInteraction=None, \
        NetworkViewRendererList=None, RootNetworkList=None, startLoadRow=None,\
        TargetColumnList=None, verbose=False):
        """
        Import a new network from a tabular formatted file type (e.g. csv, tsv,
        Excel, etc.). Use network load file to load network formatted files. This
        command will create a new network collection if no current network collection
        is selected, otherwise it will add the network to the current collection. The
        SUIDs of the new networks and views are returned.

        :param dataTypeList (string, optional): List of column data types ordered
            by column index (e.g. "string,int,long,double,boolean,intlist" or
            just "s,i,l,d,b,il"): ,
        :param defaultInteraction (string, optional): Used to set the default
            interaction type to use when there is no interaction type column.
        :param delimiters (string, optional): Select the delimiters to use to
            separate columns in the table, from the list ',',' ','TAB', or ';'.
            TAB and ',' are used by default = [',', ';', ' ', '\t']
        :param delimitersForDataList (string, optional): Select the delimiters
            to use to separate list entries in a list, from the list '|','\','/',
            or ','. | is used by default = ['\|', '\', '/', ',']
        :param afile (string): The path to the file that contains the table or
            network to be imported.
        :param firstRowAsColumnNames (string, optional): If this is true then
            the first row should contain the names of the columns. Note that
            startLoadRow must be set for this to work properly
        :param indexColumnSourceInteraction (string): The column index that
            contains the source node identifiers.
        :param indexColumnTargetInteraction (string, optional): The column index
            that contains the target node identifiers. If this is not specified
            then the resulting network will have no edges
        :param indexColumnTypeInteraction (string, optional): The column index
            that contains the interaction type. This is not required.
        :param NetworkViewRendererList (string, optional): Enter the network
            view renderer that this network should use. This is only useful if
            multiple renderers have been installed, which is rare. = ['']
        :param RootNetworkList (string, optional): The name of the network
            collection (root network) that the imported network should be part of.
            A name of -- Create new network collection -- will result in the
            creation of a new network collection for this import. = ['-- Create
            new network collection --', 'cy:command_documentation_generation']
        :param startLoadRow (string, optional): The starting row of the import.
            This is used to skip over comments and other non-data rows at the
            beginning of the file.
        :param TargetColumnList (string, optional): Enter the name of the column
            in the existing network collection (root network) that you want to
            map your input identifiers to. = ['']
        :param verbose: print more

        :returns:  { SUIDs of the new networks and views }
        """

        PARAMS=set_param(["dataTypeList","defaultInteraction","delimiters","delimitersForDataList",\
        "file","firstRowAsColumnNames","indexColumnSourceInteraction","indexColumnTargetInteraction",\
        "indexColumnTypeInteraction","NetworkViewRendererList","RootNetworkList","startLoadRow","TargetColumnList"],\
        [dataTypeList,defaultInteraction,delimiters,delimitersForDataList,\
        afile,firstRowAsColumnNames,indexColumnSourceInteraction,indexColumnTargetInteraction,\
        indexColumnTypeInteraction,NetworkViewRendererList,RootNetworkList,startLoadRow,TargetColumnList])
        response=api(url=self.__url+"/import file", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def import_url(self, dataTypeList=None, defaultInteraction=None, delimiters=None, \
        delimitersForDataList=None, firstRowAsColumnNames=None, \
        indexColumnSourceInteraction=None, indexColumnTargetInteraction=None, indexColumnTypeInteraction=None, \
        NetworkViewRendererList=None, RootNetworkList=None, startLoadRow=None,\
        TargetColumnList=None, url=None, verbose=False):
        """
        Import a new network from a tabular formatted file type (e.g. csv, tsv,
        Excel, etc.). Use network load file to load network formatted files. This
        command will create a new network collection if no current network collection
        is selected, otherwise it will add the network to the current collection. The
        SUIDs of the new networks and views are returned.

        :param dataTypeList (string, optional): List of column data types ordered
            by column index (e.g. "string,int,long,double,boolean,intlist" or just
            "s,i,l,d,b,il"): ,
        :param defaultInteraction (string, optional): Used to set the default
            interaction type to use when there is no interaction type column.
        :param delimiters (string, optional): Select the delimiters to use to
            separate columns in the table, from the list ',',' ','TAB', or ';'.
            TAB and ',' are used by default = [',', ';', ' ', '\t']
        :param delimitersForDataList (string, optional): Select the delimiters
            to use to separate list entries in a list, from the list '|','\','/',
            or ','. | is used by default = ['\|', '\', '/', ',']
        :param firstRowAsColumnNames (string, optional): If this is true then
            the first row should contain the names of the columns. Note that
            startLoadRow must be set for this to work properly
        :param indexColumnSourceInteraction (string): The column index that
            contains the source node identifiers.
        :param indexColumnTargetInteraction (string, optional): The column index
            that contains the target node identifiers. If this is not specified
            then the resulting network will have no edges
        :param indexColumnTypeInteraction (string, optional): The column index
            that contains the interaction type. This is not required.
        :param NetworkViewRendererList (string, optional): Enter the network view
            renderer that this network should use. This is only useful if multiple
            renderers have been installed, which is rare. = ['']
        :param RootNetworkList (string, optional): The name of the network
            collection (root network) that the imported network should be part of.
            A name of -- Create new network collection -- will result in the creation
            of a new network collection for this import. = ['-- Create new network collection --',
            'cy:command_documentation_generation']
        :param startLoadRow (string, optional): The starting row of the import.
            This is used to skip over comments and other non-data rows at the
            beginning of the file.
        :param TargetColumnList (string, optional): Enter the name of the
            column in the existing network collection (root network) that you
            want to map your input identifiers to. = ['']
        :param url (string): The URL of the file or resource that provides the
            table or network to be imported.
        :param verbose: print more

        :returns:  { SUIDs of the new networks and views }
        """

        PARAMS=set_param(["dataTypeList","defaultInteraction","delimiters","delimitersForDataList",\
        "firstRowAsColumnNames","indexColumnSourceInteraction","indexColumnTargetInteraction",\
        "indexColumnTypeInteraction","NetworkViewRendererList","RootNetworkList","startLoadRow","TargetColumnList","url"],\
        [dataTypeList,defaultInteraction,delimiters,delimitersForDataList,\
        firstRowAsColumnNames,indexColumnSourceInteraction,indexColumnTargetInteraction,\
        indexColumnTypeInteraction,NetworkViewRendererList,RootNetworkList,startLoadRow,TargetColumnList, url])
        response=api(url=self.__url+"/import url", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def list(self, verbose=False):
        """
        List all of the networks in the current session.

        :param verbose: print more

        :returns: [ list of network suids ]
        """

        response=api(url=self.__url+"/list", method="POST", verbose=verbose)
        return response

    def list_attributes(self, namespace=None, network=None, verbose=False):
        """
        Returns a list of column names assocated with a network.

        :param namespace (string, optional): Node, Edge, and Network objects
            support the default, local, and hidden namespaces. Root networks also
                support the shared namespace. Custom namespaces may be specified
                by Apps.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        :returns: [ list of column names assocated with a network ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["namespace","network"],[namespace,network])
        response=api(url=self.__url+"/list attributes", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def list_properties(self, network=None, verbose=False):
        """
        List all of the visual properties for networks.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        :returns: [ List all of the visual properties ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network"],[network])
        response=api(url=self.__url+"/list properties", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def load_file(self, afile=None, verbose=False):
        """
        Load a new network from a network file type (e.g. SIF, XGMML, etc.).
        Use network import file to load networks from Excel or csv files. This
        command will create a new network collection if no current network collection
        is selected, otherwise it will add the network to the current collection.
        The SUIDs of the new networks and views are returned.

        :param afile (string): Select a network format file. This command does
            not support csv or Excel files. Use network import file for that.
        :param verbose: print more

        :returns: { SUIDs of the new networks and views }
        """
        PARAMS=set_param(["file"],[afile])
        response=api(url=self.__url+"/load file", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def load_url(self, url=None, verbose=False):
        """
        Load a new network from a URL that points to a network file type (e.g.
        SIF, XGMML, etc.). Use network import url to load networks from Excel or
        csv files. This command will create a new network collection if no current
        network collection is selected, otherwise it will add the network to the
        current collection. The SUIDs of the new networks and views are returned.

        :param url (string): Select a URL that points to a network format file.
            This command does not support csv or Excel files. Use network import
            url for that.
        :param verbose: print more

        :returns: { SUIDs of the new networks and views }
        """
        PARAMS=set_param(["url"],[url])
        response=api(url=self.__url+"/load url", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def rename(self, name=None, sourceNetwork=None, verbose=False):
        """
        Rename an existing network. The SUID of the network is returned

        :param name (string): Enter a new title for the network
        :param sourceNetwork (string): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value
            can also be used to specify the current network.
        :param verbose: print more

        :returns: SUID of the network is returned
        """
        sourceNetwork=check_network(self,sourceNetwork,verbose=verbose)
        PARAMS=set_param(["name","sourceNetwork"],[name,sourceNetwork])
        response=api(url=self.__url+"/rename", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def select(self, adjacentEdges=None, edgeList=None, extendEdges=None, firstNeighbors=None, \
        invert=None, network=None, nodeList=None, verbose=False):
        """
        Select nodes and/or edges in a network. This command provides options to
        invert the selection, add first neighbors, add adjacent edges of selected
        nodes, and add adjacent nodes of selected edges

        :param adjacentEdges (string, optional): If 'true', then select any edges
            adjacent to any selected nodes. This happens before any inversion
        :param edgeList (string, optional): Specifies a list of edges. The keywords
            all, selected, or unselected can be used to specify edges by their
            selection state. The pattern COLUMN:VALUE sets this parameter to any
            rows that contain the specified column value; if the COLUMN prefix is
            not used, the NAME column is matched by default. A list of COLUMN:VALUE
            pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to
            match multiple values.
        :param extendEdges (string, optional): If 'true', then select any nodes
            adjacent to any selected edges. This happens before any inversion
        :param firstNeighbors (string, optional): If this option is anything other
            than 'none', add nodes to the selection based on the value of the
            argument. If 'incoming', add nodes to the selection that have edges
            pointing to one of the selected nodes. If 'output', add nodes to the
            selection that have edges that point to them from one of the selected
            nodes. If 'undirected' add any neighbors that have undirected edges
            connecting to any of the selected nodes. Finally, if 'any', then add
            all first neighbors to the selection list. = ['none', 'incoming',
            'outgoing', 'undirected', 'any'],
        :param invert (string, optional): If this option is not 'none', then the
            selected nodes or edges (or both) will be deselected and all other
            nodes or edges will be selected = ['none', 'nodes', 'edges', 'both']
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank value
            can also be used to specify the current network.
        :param nodeList (string, optional): Specifies a list of nodes. The keywords
            all, selected, or unselected can be used to specify nodes by their
            selection state. The pattern COLUMN:VALUE sets this parameter to any
            rows that contain the specified column value; if the COLUMN prefix is
            not used, the NAME column is matched by default. A list of COLUMN:VALUE
            pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to
            match multiple values.
        :param verbose: print more

        :returns: [ list of selected edges and nodes ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["adjacentEdges","edgeList","extendEdges","firstNeighbors",\
        "invert","network","nodeList"], \
        [adjacentEdges,edgeList,extendEdges,firstNeighbors,\
        invert,network,nodeList])
        response=api(url=self.__url+"/select", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def set_attribute(self, columnList=None, namespace=None, network=None, valueList=None, verbose=False):
        """
        Set a value in the network table.

        :param columnList (string, optional): A list of column names, separated
            by commas.
        :param namespace (string, optional): Node, Edge, and Network objects
            support the default, local, and hidden namespaces. Root networks also
                support the shared namespace. Custom namespaces may be specified by Apps.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param valueList (string, optional): A list of values, separated by commas.
            List values can be included using the format [value1,value2].
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["columnList","namespace","network","valueList"], \
        [columnList,namespace,network,valueList])
        response=api(url=self.__url+"/set attribute", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response
 

    def set_current(self, network=None, verbose=False):
        """
        Sets the current network, which can also be null.

        This will set the .network.network_name value to network.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more
        """
        PARAMS=set_param(["network"], [network])
        response=api(url=self.__url+"/set current", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def set_properties(self, network=None, propertyList=None, valueList=None, verbose=False):
        """
        Set network visual properties.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param propertyList (string): A comma-separated list of network properties
        :param valueList (string): A comma-separated list of property values.
            This list must have the same number of elements as the propertyList.
            Each value will be applied to the property specified in the same
            position in the propertyList
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network","propertyList","valueList"], \
        [network,propertyList,valueList])
        response=api(url=self.__url+"/set properties", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def show(self, edgeList=None, network=None, nodeList=None, verbose=False):
        """
        Show nodes and/or edges in a network. A list of nodes and/or edges may
        be provided and those nodes and edges will be unhidden in the view associated
        with the provided network.Note that the network '''must''' have a view.
        The SUIDs of the unhidden nodes and/or edges are returned.

        :param edgeList (string, optional): Specifies a list of edges. The keywords
            all, selected, or unselected can be used to specify edges by their
            selection state. The pattern COLUMN:VALUE sets this parameter to any
            rows that contain the specified column value; if the COLUMN prefix is
            not used, the NAME column is matched by default. A list of COLUMN:VALUE
            pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to match
            multiple values.
        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value can
            also be used to specify the current network.
        :param nodeList (string, optional): Specifies a list of nodes. The keywords
            all, selected, or unselected can be used to specify nodes by their
            selection state. The pattern COLUMN:VALUE sets this parameter to any
            rows that contain the specified column value; if the COLUMN prefix is
            not used, the NAME column is matched by default. A list of COLUMN:VALUE
            pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to
            match multiple values.
        :param verbose: print more

        :returns: [ list of SUIDs of the unhidden nodes and/or edges ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["edgeList","network","nodeList"],[edgeList,network,nodeList])
        response=api(url=self.__url+"/show", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response
