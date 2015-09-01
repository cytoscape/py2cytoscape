# -*- coding: utf-8 -*-
import json

import pandas as pd
import requests
from py2cytoscape.data.edge_view import EdgeView
from py2cytoscape.data.node_view import NodeView

from . import BASE_URL, HEADERS
from py2cytoscape.data.util_network import NetworkUtil

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
        return self.__get_views('nodes')

    def get_edge_views(self):
        return self.__get_views('edges')

    def __get_views(self, obj_type=None):
        url = self.__url + '/' + obj_type
        views = requests.get(url).json()
        view_list = []
        for view in views:
            if obj_type is 'nodes':
                view = NodeView(self, view['SUID'], obj_type)
            elif obj_type is 'edges':
                view = EdgeView(self, view['SUID'], obj_type)

            view_list.append(view)
        return view_list

    def update_node_views(self, visual_property=None, values=None, key_type='suid'):
        self.__update_views(visual_property, values, 'nodes', key_type)

    def update_edge_views(self, visual_property=None, values=None, key_type='suid'):
        self.__update_views(visual_property, values, 'edges', key_type)

    def __update_views(self, visual_property, values,
                       object_type=None, key_type='suid'):
        if key_type is 'name':
            name2suid = NetworkUtil.name2suid(self.__network)

        body = []
        for key in values.keys():
            if key_type is 'name':
                suid = name2suid[key]
                if suid is None:
                    continue
            else:
                suid = key

            new_value = {
                "SUID": suid,
                "view": [
                    {
                        "visualProperty": visual_property,
                        "value": values[key]
                    }
                ]
            }
            body.append(new_value)
        requests.put(self.__url + '/' + object_type , data=json.dumps(body), headers=HEADERS)
