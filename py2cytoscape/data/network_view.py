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

    def get_node_views_as_dict(self):
        return self.__get_views('nodes', format='dict')

    def get_edge_views_as_dict(self):
        return self.__get_views('edges', format='dict')

    def __get_views(self, obj_type=None, format='view'):
        url = self.__url + '/' + obj_type
        views = requests.get(url).json()
        if format is 'dict':
            return self.__get_view_dict(views)

        elif format is 'view':
            return self.__get_view_objects(views, obj_type)

        else:
            raise ValueError('Format not supported: ' + format)

    def __get_view_objects(self, views, obj_type):
        view_list = []
        if obj_type is 'nodes':
            for view in views:
                view = NodeView(self, view['SUID'], obj_type)
                view_list.append(view)

        elif obj_type is 'edges':
            for view in views:
                view = EdgeView(self, view['SUID'], obj_type)
                view_list.append(view)

        else:
            raise ValueError('No such object type: ' + obj_type)

        return view_list

    def __get_view_dict(self, views):
        # reformat return value to simple dict
        view_dict = {}
        for view in views:
            key = view['SUID']
            values = view['view']
            # Flatten the JSON
            key_val_pair = {}
            for entry in values:
                vp = entry['visualProperty']
                value = entry['value']
                key_val_pair[vp] = value
            view_dict[key] = key_val_pair

        return view_dict

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
