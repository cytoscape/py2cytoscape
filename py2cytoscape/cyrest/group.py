from .base import *

class group(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation for 'group'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/edge'

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
