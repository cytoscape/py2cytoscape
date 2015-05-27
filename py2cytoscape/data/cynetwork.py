# -*- coding: utf-8 -*-
from network import NetworkClient

import requests
import json

from . import BASE_URL, HEADERS, SUID_LIST
from ..util import cytoscapejs as util

BASE_URL_NETWORK = BASE_URL + 'networks'
JSON = 'json'


class CyNetwork(object):

    def __init__(self, suid=None, name=None, data=None):
        # SUID is immutable
        if suid is None:
            self.__id = NetworkClient.create()
        else:
            # Fetch network from current session
            id_list = NetworkClient.get_all()
            try:
                id_list.index(suid)
            except ValueError:
                print('Network does not exist.')
            else:
                self.__id = suid
            finally:
                self.__id = None

        self.__url = BASE_URL_NETWORK + '/' + str(self.__id) + '/'

    def get_id(self):
        return self.__id

    def get_nodes(self):
        return requests.get(self.__url + 'nodes').json()

    def add_node(self, node_name):
        if node_name is None:
            return None
        return self.add_nodes([node_name])

    def add_nodes(self, node_name_list):
        nodes = requests.post(self.__url + 'nodes', data=json.dumps(
            node_name_list), headers=HEADERS).json()
        node_dict = {}
        for node in nodes:
            node_dict[node['name']] = node['SUID']
        return node_dict

    def add_edge(self, source, target, interaction='-', directed=True):
        new_edge = {
            'source': source,
            'target': target,
            'interaction': interaction,
            'directed': directed
        }
        edges = requests.post(self.__url + 'edges', data=json.dumps(
            [new_edge]), headers=HEADERS).json()
        return edges

    def add_edges(self, edge_list):
        new_egdes = []
        for edge_tuple in edge_list:
            new_edge = {
                'source': edge_tuple[0],
                'target': edge_tuple[1],
                'interaction': edge_tuple[2],
            }
            new_egdes.append(new_edge)

        edges = requests.post(self.__url + 'edges', data=json.dumps(
            new_egdes), headers=HEADERS).json()
        return edges

    def get_table(self, type, format=None):
        url = self.__url + 'tables/default' + type
        if format is None:
            return requests.get(url).json()['rows']
        elif format is 'csv' or format is 'tsv':
            return requests.get(url + '.' + format).content

    def set_node_value(self, id, column, value):
        pass

    def set_node_values(self, column, values_tuple):
        pass

    def update_table(self, type, dataframe):
        pass

    def __data_frame_to_table(self):
        pass


class CyTable(object):

    def __init__(self, suid, type):
        self.__id = suid
