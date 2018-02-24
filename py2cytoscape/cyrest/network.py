from .base import *

class network(object):
    """
    cytoscape network interface as shown in CyREST's swagger documentation for 'network'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/network'

    def add(edgeList=None,network=None,nodeList=None, verbose=False):
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
        network=check_network(self,network)
        PARAMS=set_param(["edgeList","network","nodeList"],[edgeList,network,nodeList])
        response=api(url=self.__url+"/add", PARAMS=PARAMS, method="POST", verbose=verbose)

    def add_edge(isDirected=None,name=None,network=None,sourceName=None,targetName=None, verbose=False):
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
        network=check_network(self,network)
        PARAMS=set_param(["isDirected","name","network","sourceName","targetName"],\
        [isDirected,name,network,sourceName,targetName])
        response=api(url=self.__url+"/add adge", PARAMS=PARAMS, method="POST", verbose=verbose)

    def add_node(name=None,network=None, verbose=False):
        """
        Add a new node to an existing network. The name of the node must be provided.

        :param name (string, optional): The name of the node, which will be assigned
            to both the 'name' and 'shared name' columns
        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value can
            also be used to specify the current network.
        :param verbose: print more
        """
        network=check_network(self,network)
        PARAMS=set_param(["name","network"],[name,network])
        response=api(url=self.__url+"/add node", PARAMS=PARAMS, method="POST", verbose=verbose)

    def clone(network=None, verbose=False):
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
        """
        network=check_network(self,network)
        PARAMS=set_param(["network"], [network])
        response=api(url=self.__url+"/add node", PARAMS=PARAMS, method="POST", verbose=verbose)

    def connect_nodes(network=None, nodes=None, verbose=False):
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
        """
        network=check_network(self,network)
        PARAMS=set_param(["name","network"],[name,network])
        response=api(url=self.__url+"/connect nodes", PARAMS=PARAMS, method="POST", verbose=verbose)

    def create(edgeList=None, excludeEdges=None, networkName=None, nodeList=None, source=None, verbose=False):
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
        """
        network=check_network(self,source)
        PARAMS=set_param(["edgeList","excludeEdges","networkName","nodeList","source"], \
        [edgeList,excludeEdges,networkName,nodeList,network])
        response=api(url=self.__url+"/create", PARAMS=PARAMS, method="POST", verbose=verbose)

    def create_attribute(column=None, listType=None, namespace=None, network=None, atype=None, verbose=False):
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
        """
        network=check_network(self,network)
        PARAMS=set_param(["column","listType","namespace","network","type"], \
        [column,listType,namespace,network,atype])
        response=api(url=self.__url+"/create attribute", PARAMS=PARAMS, method="POST", verbose=verbose)

    def create_empty(name=None, renderers=None, RootNetworkList=None, verbose=False):
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

    def delete(edgeList=None, network=None, nodeList=None, verbose=False):
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
        network=check_network(self,network)
        PARAMS=set_param(["edgeList","network","nodeList"],[edgeList,network,nodeList])
        response=api(url=self.__url+"/delete", PARAMS=PARAMS, method="POST", verbose=verbose)

    def deselect(edgeList=None, network=None, nodeList=None, verbose=False):
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
        """
        network=check_network(self,network)
        PARAMS=set_param(["edgeList","network","nodeList"],[edgeList,network,nodeList])
        response=api(url=self.__url+"/deselect", PARAMS=PARAMS, method="POST", verbose=verbose)

    def destroy(network=None, verbose=False):
        """
        Destroy (delete) a network. The SUID of the destroyed network is returned.

        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value can
            also be used to specify the current network.
        :param verbose: print more
        """
        network=check_network(self,network)
        PARAMS=set_param(["network"],[network])
        response=api(url=self.__url+"/destroy", PARAMS=PARAMS, method="POST", verbose=verbose)

    def export(options=None, OutputFile=None, verbose=False):
        """
        Export a network to a network file (e.g. XGMML, SIF, etc.)

        :param options (string, optional): The format of the output file. = ['CX JSON (*.cx)',
            'Cytoscape.js JSON (*.cyjs)', 'GraphML files (*.graphml, *.xml)', 'NNF (*.nnf)',
            'PSI-MI Level 1', 'PSI-MI Level 2.5', 'SIF (*.sif)', 'XGMML (*.xgmml, *.xml)']
        :param OutputFile (string, optional):
        :param verbose: print more
        """
        PARAMS=set_param(["options","OutputFile"],[netoptions,OutputFile])
        response=api(url=self.__url+"/export", PARAMS=PARAMS, method="POST", verbose=verbose)

    def get(network=None, verbose=False):
        """
        Specifies a network by name, or by SUID if the prefix SUID: is used.
        The keyword CURRENT, or a blank value can also be used to specify the
        current network.

        :param network: network (string, optional): Specifies a network by name,
            or by SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more
        """

        print("Getting '%s' network.")
        network=check_network(self,network)
        PARAMS=set_param(["network"],[network])
        response=api(url=self.__url+"/get", PARAMS=PARAMS, method="POST", verbose=verbose)
        if len(response.keys()) > 0:
            self.network_name=response["name"]
            self.network_suid=response["SUID"]
            for p in response.keys():
                print(p , ":", response[p])
        else:
            print "Could not get network."
