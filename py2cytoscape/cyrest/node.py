from .base import *

class node(object):
    """
    cytoscape network interface as shown in CyREST's swagger documentation for 'node'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/node'

    def create_attribute(self, column=None, listType=None, namespace=None, network=None, coltype=None, verbose=False):
        """
        Creates a new node column.

        :param column (string, optional): Unique name of column.
        :param listType (string, optional): Can be one of integer, long, double,
            or string. = ['integer', 'long', 'double', 'string', 'boolean']
        :param namespace (string, optional): Node, Edge, and Network objects
            support the default, local, and hidden namespaces. Root networks
            also support the shared namespace. Custom namespaces may be
            specified by Apps.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param coltype (string, optional): Can be one of integer, long, double,
            string, or list. = ['integer', 'long', 'double', 'string', 'boolean', 'list']
        :param verbose: print more

        :returns: {"columnName": columnName}
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["column","listType","namespace","network","type"],[column,listType,namespace,network,coltype])
        response=api(url=self.__url+"/create attribute", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def get(self, network=None, node=None, verbose=False):
        """
        Returns the SUID of a node that matches the passed parameters. If
        multiple nodes are found, only one will be returned, and a warning will
        be printed.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param node (string, optional): Selects a node by name, or, if the
            parameter has the prefix suid: selects a node by SUID.
        :param verbose: print more

        :returns: [ SUIDs of nodes that match the passed parameters ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network","node"],[network,node])
        response=api(url=self.__url+"/get", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def get_attribute(self, columnList=None, namespace=None, network=None, nodeList=None, verbose=False):
        """
        Returns the attributes for the nodes passed as parameters.

        :param columnList (string, optional): A list of column names, separated
            by commas.
        :param namespace (string, optional): Node, Edge, and Network objects
            support the default, local, and hidden namespaces. Root networks
            also support the shared namespace. Custom namespaces may be specified
            by Apps.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param nodeList (string, optional): Specifies a list of nodes. The
            keywords all, selected, or unselected can be used to specify nodes
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list of
            COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param verbose: print more

        :returns: [ { "name": "Q9UQ35"}, { "name": "Q4G0J3" } ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["columnList", "namespace", "network","nodeList"],[columnList, namespace, network, nodeList])
        response=api(url=self.__url+"/get attribute", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def get_properties(self, network=None, nodeList=None, propertyList=None, verbose=False):
        """
        Returns the visual properties for the nodes that match the passed parameters.

        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value
            can also be used to specify the current network.
        :param nodeList (string, optional): Specifies a list of nodes. The
            keywords all, selected, or unselected can be used to specify nodes by
            their selection state. The pattern COLUMN:VALUE sets this parameter to
            any rows that contain the specified column value; if the COLUMN prefix
            is not used, the NAME column is matched by default. A list of COLUMN:VALUE
            pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to match
            multiple values.
        :param propertyList (string, optional): A list of property names separated by commas.
        :param verbose: print more


        :returns: [
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
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network", "nodeList", "propertyList"],[network, nodeList, propertyList])
        response=api(url=self.__url+"/get properties", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    
    def list(self, network=None, nodeList=None, verbose=False):
        """
        Returns a list of the node SUIDs associated with the passed network parameter.

        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value
            can also be used to specify the current network.
        :param nodeList (string, optional): Specifies a list of nodes. The
            keywords all, selected, or unselected can be used to specify nodes by
            their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list of
            COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param verbose: print more

        :returns: [ 283,  295, 311 ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network", "nodeList"],[network, nodeList])
        response=api(url=self.__url+"/list", PARAMS=PARAMS, method="POST", verbose=verbose)

        return response

    def list_attributes(self, namespace=None, network=None, verbose=False):
        """
        Returns a list of column names assocated with nodes.

        :param namespace (string, optional): Node, Edge, and Network objects
            support the default, local, and hidden namespaces. Root networks also
            support the shared namespace. Custom namespaces may be specified by Apps.
        :param network (string, optional): Specifies a network by name, or by SUID
            if the prefix SUID: is used. The keyword CURRENT, or a blank value can
            also be used to specify the current network.
        :param verbose: print more

        :returns: [ list of column names assocated with nodes ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["namespace", "network"],[namespace, network])
        response=api(url=self.__url+"/list attributes", PARAMS=PARAMS, method="POST", verbose=verbose)

        return response

    def list_properties(self, network=None, verbose=False):
        """
        Returns a list of visual properties available for nodes.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        :returns: [ list of visual properties available for nodes ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network"],[network])
        response=api(url=self.__url+"/list properties", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def rename(self, network=None, newName=None, node=None, verbose=False):
        """
        Sets the value of the name column for the passed node.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param newName (string, optional): New name of the node ,
        :param node (string, optional): Selects a node by name, or, if the
            parameter has the prefix suid:, selects a node by SUID.
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network", "newName", "node"],[network, newName, node])
        response=api(url=self.__url+"/rename", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    
    def select_from_file(self, afile=None, verbose=False):
        """
        Selects nodes in the current network based on node names provided by a file.

        :param afile (string, optional): Path to file containing list of nodes to select
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["file"],[afile])
        response=api(url=self.__url+"/select from file", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    
    def set_attribute(self, columnList=None, namespace=None, network=None, nodeList=None, valueList=None, verbose=False):
        """
        Sets the value of a specified column for the passed node or set of nodes.

        :param columnList (string, optional): A list of column names, separated
            by commas.
        :param namespace (string, optional): Node, Edge, and Network objects
            support the default, local, and hidden namespaces. Root networks also
            support the shared namespace. Custom namespaces may be specified by Apps.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network. ,
        :param nodeList (string, optional): Specifies a list of nodes. The
            keywords all, selected, or unselected can be used to specify nodes by
            their selection state. The pattern COLUMN:VALUE sets this parameter to
            any rows that contain the specified column value; if the COLUMN prefix
            is not used, the NAME column is matched by default. A list of COLUMN:VALUE
            pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be used to
            match multiple values.
        :param valueList (string, optional): A list of values, separated by
            commas. List values can be included using the format [value1,value2].
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["columnList", "namespace", "network", "nodeList", "valueList"],[columnList, namespace, network, nodeList, valueList])
        response=api(url=self.__url+"/set attribute", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    
    def set_properties(self, network=None, nodeList=None, propertyList=None, valueList=None, verbose=False):
        """
        Sets the value of a specified property for the passed node or set of nodes.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param nodeList (string, optional): Specifies a list of nodes. The
            keywords all, selected, or unselected can be used to specify nodes
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list of
            COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param propertyList (string, optional): A list of property names
            separated by commas.
        :param valueList (string, optional): A list of values separated by commas.
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network", "nodeList", "propertyList", "valueList"],[network, nodeList, propertyList, valueList])
        response=api(url=self.__url+"/set properties", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    