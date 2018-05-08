from .base import *

class group(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation for 'group'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/group'

    def add(self, edgeList=None, groupName=None, network=None, nodeList=None, verbose=False):
        """
        Adds the specified nodes and edges to the specified group.

        :param edgeList (string, optional): Specifies a list of edges. The
            keywords all, selected, or unselected can be used to specify edges
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list
            of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param groupName (string, optional): Specifies the name used to
            identify the group.
        :param network (string, optional): Specifies a network by name, or
            by SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param nodeList (string, optional): Specifies a list of nodes. The
            keywords all, selected, or unselected can be used to specify nodes
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list of
            COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param verbose: print more

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["edgeList","groupName","network","nodeList"],[edgeList,groupName,network,nodeList])
        response=api(url=self.__url+"/add", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def collapse(self, groupList=None, network=None, verbose=False):
        """
        Replaces the representation of all of the nodes and edges in a group with a single node.

        :param groupList (string, optional): Specifies a list of groups. The
            keywords all, selected, or unselected can be used to specify groups
            by their selection state.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["groupList","network"],[groupList,network])
        response=api(url=self.__url+"/collapse", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def create(self, groupName=None, network=None, nodeList=None, verbose=False):
        """
        Create a group from the specified nodes.

        :param groupName (string, optional): Specifies the name used to identify
            the group.
        :param network (string, optional): Specifies a network by name, or
            by SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param nodeList (string, optional): Specifies a list of nodes. The
            keywords all, selected, or unselected can be used to specify nodes
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list of
            COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param verbose: print more

        :return: SUID of created group

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["groupName","network","nodeList"],[groupName,network,nodeList])
        response=api(url=self.__url+"/create", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def expand(self, groupList=None, network=None, verbose=False):
        """
        Replaces the group node with member nodes for a set of groups.

        :param groupList (string, optional): Specifies a list of groups. The
            keywords all, selected, or unselected can be used to specify groups
            by their selection state.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["groupList","network"],[groupList,network])
        response=api(url=self.__url+"/expand", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def get(self, network=None, node=None, verbose=False):
        """
        Get a group by providing a network and the group node identifier.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param node (string, optional): Selects a node by name, or, if the
            parameter has the prefix suid:, selects a node by SUID.
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network","node"],[network,node])
        response=api(url=self.__url+"/get", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def glist(self, network=None, verbose=False):
        """
        Lists the SUIDs of all of the groups in a network.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be to specify the current network.
        :param verbose: print more

        :returns: eg. [ 3545 ]
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network"],[network])
        response=api(url=self.__url+"/list", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def remove(self, edgeList=None, groupName=None, network=None, nodeList=None, verbose=False):
        """
        Remove the selected nodes and edges from their current group.

        :param edgeList (string, optional): Specifies a list of edges. The
            keywords all, selected, or unselected can be used to specify edges
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list
            of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param groupName (string, optional): Specifies the name used to identify
            the group.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param nodeList (string, optional): Specifies a list of nodes. The
            keywords all, selected, or unselected can be used to specify nodes
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list
            of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["edgeList","groupName","network","nodeList"],[edgeList,groupName,network,nodeList])
        response=api(url=self.__url+"/remove", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def rename(self, groupName=None, network=None, newName=None, verbose=False):
        """
        Changes the name of the selected group or groups.

        :param groupName (string, optional): Specifies the name used to identify
            the group.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param newName (string, optional): Specifies the NEW name used to
            identify the group.
        :param verbose: print more
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network","nodeList","newName"],[network,nodeList,newName])
        response=api(url=self.__url+"/rename", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def ungroup(self, network=None, nodeList=None, verbose=False):
        """
        Ungroups one or more groups, expanding them if they are collapsed and removing the group nodes.

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
        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network","nodeList"],[network,nodeList])
        response=api(url=self.__url+"/ungroup", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response
