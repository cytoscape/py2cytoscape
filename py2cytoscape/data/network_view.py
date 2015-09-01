# -*- coding: utf-8 -*-
import json

import pandas as pd
import requests
from py2cytoscape.data.edge_view import EdgeView
from py2cytoscape.data.node_view import NodeView

from ..util import util_networkx as nx_util
from ..util import dataframe as df_util

from . import BASE_URL, HEADERS

BASE_URL_NETWORK = BASE_URL + 'networks'


class CyNetworkView(object):

    def __init__(self, network=None, suid=None):
        if network is None:
            raise ValueError('Network is required.')

        # Validate required argument
        if pd.isnull(suid):
            raise ValueError("View SUID is missing.")
        else:
            self.__network = network
            self.__id = suid

        self.__url = BASE_URL_NETWORK + '/' \
                     + str(self.__network.get_id()) + '/views/' + str(self.__id)

    def get_id(self):
        """
        Get session-unique ID of this network view

        :return: SUID as integer
        """
        return self.__id

    def get_model_id(self):
        """
        Get network model SUID

        :return: model SUID as integer
        """
        return self.__network.get_id()

    def get_node_views(self):
        url = self.__url + '/nodes'
        node_views = requests.get(url).json()
        view_list = []
        for view in node_views:
            node_view = NodeView(self, view, 'nodes')
            view_list.append(node_view)

        return view_list

    def get_edge_views(self):
        url = self.__url + '/edges'
        edge_views = requests.get(url).json()
        view_list = []
        for view in edge_views:
            edge_view = EdgeView(self, view, 'edges')
            view_list.append(edge_view)

        return view_list

    def set_edge_views(self, new_views):
        pass


