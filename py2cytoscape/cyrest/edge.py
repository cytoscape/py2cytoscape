from .base import *

class edge(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation for 'edge'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/edge'

    def create_attribute(self,column=None,listType=None,namespace=None, network=None, atype=None, verbose=False):
        """
        Creates a new edge column.

        :param column (string, optional): Unique name of column
        :param listType (string, optional): Can be one of integer, long, double,
            or string.
        :param namespace (string, optional): Node, Edge, and Network objects
            support the default, local, and hidden namespaces. Root networks
            also support the shared namespace. Custom namespaces may be specified
            by Apps.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param atype (string, optional): Can be one of integer, long, double,
            string, or list.
        :param verbose: print more

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["column","listType","namespace","network","type"],[column,listType,namespace,network,atype])
        response=api(url=self.__url+"/create attribute", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def get(self,edge=None,network=None,sourceNode=None, targetNode=None, atype=None, verbose=False):
        """
        Returns the SUID of an edge that matches the passed parameters. If
        multiple edges are found, only one will be returned, and a warning will
        be reported in the Cytoscape Task History dialog.

        :param edge (string, optional): Selects an edge by name, or, if the
            parameter has the prefix suid:, selects an edge by SUID. If this
            parameter is set, all other edge matching parameters are ignored.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param sourceNode (string, optional): Selects a node by name, or, if
            the parameter has the prefix suid:, selects a node by SUID. Specifies
            that the edge matched must have this node as its source. This parameter
            must be used with the targetNode parameter to produce results.
        :param targetNode (string, optional): Selects a node by name, or, if
            the parameter has the prefix suid:, selects a node by SUID. Specifies
            that the edge matched must have this node as its target. This parameter
            must be used with the sourceNode parameter to produce results.
        :param atype (string, optional): Specifies that the edge matched must
            be of the specified type. This parameter must be used with the
            sourceNode and targetNode parameters to produce results.
        :param verbose: print more

        :returns: {"columnName": columnName }

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["edge","network","sourceNode","targetNode","type"],[edge,network,sourceNode,targetNode,atype])
        response=api(url=self.__url+"/get", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def get_attribute(self,columnList=None,edgeList=None,namespace=None, network=None, verbose=False):
        """
        Returns the attributes for the edges passed as parameters.

        :param columnList (string, optional): A list of column names, separated
            by commas.
        :param edgeList (string, optional): Specifies a list of edges. The
            keywords all, selected, or unselected can be used to specify edges
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list
            of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param namespace (string, optional): Node, Edge, and Network objects
            support the default, local, and hidden namespaces. Root networks
            also support the shared namespace. Custom namespaces may be specified
            by Apps.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        :returns: eg. [ {"name": "TAT (pp) O60563"}, {"name": "TAT (pp) O60563"}]

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["columnList","edgeList","namespace","network"],[columnList,edgeList,namespace,network])
        response=api(url=self.__url+"/get attribute", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def get_properties(self,edgeList=None,network=None,propertyList=None, verbose=False):
        """
        Returns the visual properties for the edges that match the passed parameters.

        :param edgeList (string, optional): Specifies a list of edges. The
            keywords all, selected, or unselected can be used to specify edges
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list
            of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param propertyList (string, optional): A list of property names
            separated by commas.
        :param verbose: print more

        :returns: eg. [
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
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["edgeList","network","propertyList"],[edgeList,network,propertyList])
        response=api(url=self.__url+"/get properties", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def list(self, edgeList=None, network=None, verbose=False):
        """
        Returns a list of the edge SUIDs associated with the passed network parameter.

        :param edgeList (string, optional): Specifies a list of edges. The
            keywords all, selected, or unselected can be used to specify edges
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list of
            COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        :returns: eg. [ 772, 773, .. ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["edgeList","network"],[edgeList,network])
        response=api(url=self.__url+"/list", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def list_attributes(self,columnList=None,edgeList=None,namespace=None, network=None, verbose=False):
        """
        Returns the attributes for the edges passed as parameters.

        :param columnList (string, optional): A list of column names, separated
            by commas.
        :param edgeList (string, optional): Specifies a list of edges. The
            keywords all, selected, or unselected can be used to specify edges
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list
            of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param namespace (string, optional): Node, Edge, and Network objects
            support the default, local, and hidden namespaces. Root networks
            also support the shared namespace. Custom namespaces may be specified
            by Apps.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        :returns:  eg. [
                        "SUID",
                        "shared name",
                        "shared interaction",
                        "name",
                        "selected",
                        "interaction",
                        "Annotation",
                        .. ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["columnList","edgeList","namespace","network"],[columnList,edgeList,namespace,network])
        response=api(url=self.__url+"/list attributes", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def list_properties(self,columnList=None,edgeList=None,namespace=None, network=None, verbose=False):
        """
        Returns a list of visual properties available for edges.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        :returns:  eg. [
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
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network"],[network])
        response=api(url=self.__url+"/list properties", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def rename(self, edge=None, network=None, newName=None, verbose=False):
        """
        Sets the value of the name column for the passed edge.

        :param edge (string, optional): Selects an edge by name, or, if the
            parameter has the prefix suid:, selects an edge by SUID.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param newName (string, optional): New name of the edge
        :param verbose: print more

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["edge","network","newName"],[edge,network,newName])
        response=api(url=self.__url+"/rename", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def set_attribute(self, columnList=None, edgeList=None, namespace=None, network=None, valueList=None, verbose=False):
        """
        Sets the value of a specified column for the passed edge or set of edges.

        :param columnList (string, optional): A list of column names, separated
            by commas.
        :param edgeList (string, optional): Specifies a list of edges. The
            keywords all, selected, or unselected can be used to specify edges
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list
            of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param namespace (string, optional): Node, Edge, and Network objects
            support the default, local, and hidden namespaces. Root networks
            also support the shared namespace. Custom namespaces may be specified
            by Apps.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param valueList (string, optional): A list of values, separated by
            commas. List values can be included using the format [value1,value2].
        :param verbose: print more

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["columnList","edgeList","namespace","network", "valueList"],[columnList, edgeList, namespace, network, valueList])
        response=api(url=self.__url+"/set attribute", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def set_properties(self, edgeList=None, network=None, propertyList=None, valueList=None, verbose=False):
        """
        Sets the value of a specified property for the passed edge or set of edges.

        :param edgeList (string, optional): Specifies a list of edges. The
            keywords all, selected, or unselected can be used to specify edges
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list of
            COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param propertyList (string, optional): A list of property names
            separated by commas.
        :param valueList (string, optional): A list of values separated by commas.
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["edgeList","network","propertyList","valueList"],[edgeList, network, propertyList, valueList])
        response=api(url=self.__url+"/set properties", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response
