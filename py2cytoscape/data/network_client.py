# -*- coding: utf-8 -*-

import requests
import json

from . import HEADERS, SUID_LIST
from ..util import cytoscapejs as util

from ..util import util_networkx as nx_util
from ..util import dataframe as df_util

JSON = 'json'

from cynetwork import CyNetwork


class NetworkClient(object):

    def __init__(self, url):
        self.__url = url + 'networks'

    def create(self, suid=None, name=None, collection=None, data=None):
        if suid is not None:
            # fetch existing network
            res = requests.get(self.__url)
            existing_networks = res.json()
            if suid in existing_networks:
                network_id = suid
            else:
                raise ValueError('No such network')
        else:
            if data is None:
                network_data = util.get_empty_network()
            else:
                network_data = data

            if name is not None:
                network_data['data']['name'] = name

            if collection is None:
                network_collection = 'From cyREST'
            else:
                network_collection = collection

            res = requests.post(self.__url + '?collection=' + network_collection, data=json.dumps(network_data), headers=HEADERS)
            result = res.json()
            network_id = result['networkSUID']

        return CyNetwork(network_id)

    def create_from_networkx(self, network, name=None, collection=None):
        if network is None:
            raise ValueError('NetworkX graph object is required.')

        cyjs = nx_util.from_networkx(network)
        return self.create(name=name, collection=collection, data=cyjs)

    def create_from_dataframe(self, dataframe, source_col='source',
                              target_col='target', interaction_col='interaction',
                              name='Created from DataFrame', collection=None):
        if dataframe is None:
            raise ValueError('DataFrame object is required.')

        cyjs = df_util.from_dataframe(dataframe,source_col=source_col,
                              target_col=target_col, interaction_col=interaction_col,
                              name=name)
        return self.create(collection=collection, data=cyjs)


    def get_all(self, format=SUID_LIST):
        if format is SUID_LIST:
            result = requests.get(self.__url)
        elif format is JSON:
            result = requests.get(self.__url + '.json')
        else:
            raise ValueError('Unsupported format type: ' + format)

        return result.json()

    def get(self, id):
        return requests.get(self.__url + '/' + str(id) + '.json').json()

    def delete_all(self):
        requests.delete(self.__url)

    def delete(self, cynetwork):
        id = cynetwork.get_id()
        requests.delete(self.__url + '/' + str(id))
        del cynetwork

