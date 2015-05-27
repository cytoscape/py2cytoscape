# -*- coding: utf-8 -*-

import unittest
from py2cytoscape.data.cyrest_client import CyRestClient
from py2cytoscape.data.cynetwork import CyNetwork

import py2cytoscape.util.dataframe as df_util
import json
import numpy as np
import pandas as pd


def pp(dict_data):
    print(json.dumps(dict_data, indent=4))


class CyRestClientTests(unittest.TestCase):

    def setUp(self):
        self.client = CyRestClient()
        # Make sure CyREST server is running
        status = self.client.status()
        self.assertIsNotNone(status)
        # cleanup
        self.client.network.delete_all()

    def test_network_api(self):
        print('\n---------- Network API Tests Start -----------\n')
        # Create empty network
        for i in range(5):
            network = self.client.network.create()

        networks = self.client.network.get_all(format='json')
        self.assertIsNotNone(networks)
        pp(networks)

    def test_cynetwork(self):
        print('\n---------- CyNetwork Tests Start -----------\n')
        network = CyNetwork()
        self.assertIsNotNone(network)
        nodes = network.get_nodes()
        pp(nodes)
        new_nodes = ['a', 'b', 'c']
        nd = network.add_nodes(new_nodes)

        self.assertIsNotNone(nd)
        pp(nd)

        edge = network.add_edge(nd['a'], nd['b'])
        self.assertIsNotNone(edge)
        pp(edge)

        new_edges = ((nd['a'], nd['b'], 'i1'), (nd['a'], nd['c'], 'i1'))
        new_edges_result = network.add_edges(new_edges)
        pp(new_edges_result)

        node_table = network.get_table('node')
        pp(node_table)
        node_table = network.get_table('node', format='tsv')
        print(node_table)
        node_table = network.get_table('node', format='csv')
        print(node_table)

        edge_table = network.get_table('edge')
        pp(edge_table)

    def test_convert(self):
        print('\n---------- DataFrame Conversion Tests Start -----------\n')
        df = pd.read_csv('data/galFiltered.sif', names=['source', 'interaction', 'target'], sep=' ')
        print(df.head(3))

        net = df_util.from_dataframe(df)

        network = CyNetwork(data=net)
        # print(network)
        data_table = pd.read_csv('data/galFiltered.nodeAttrTable.txt', sep='\t')
        result = network.update_table(type='node', df=data_table, data_key_col='ID')
        pp(result)






