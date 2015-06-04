# -*- coding: utf-8 -*-

import unittest
from py2cytoscape.data.cyrest_client import CyRestClient
from py2cytoscape.data.cynetwork import CyNetwork

import py2cytoscape.util.dataframe as df_util
import json
import numpy as np
import pandas as pd

import networkx as nx


def pp(dict_data):
    print(json.dumps(dict_data, indent=4))


class CyRestClientTests(unittest.TestCase):

    def setUp(self):
        self.client = CyRestClient()
        # cleanup
        self.client.network.delete_all()

    def test_cyrest_client(self):
        print('\n---------- Client status tests start -----------\n')
        # Make sure CyREST server is running
        status = self.client.status()
        self.assertIsNotNone(status)
        pp(status)
        self.assertEqual('v1', status['apiVersion'])

        print('\n---------- Client status tests finished! -----------\n')

    def test_create_network(self):
        print('\n---------- Create network Tests Start -----------\n')
        # Create empty network
        num_networks = 5
        for i in range(num_networks):
            self.client.network.create()

        networks = self.client.network.get_all()
        self.assertIsNotNone(networks)
        self.assertEqual(num_networks, len(networks))

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
        network = self.client.network.create()
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
        print(new_edges_result)
        self.assertEqual(2, len(new_edges_result))

        node_table = network.get_node_table()
        print(node_table)
        node_table = network.get_node_table(format='tsv')
        print(node_table)
        node_table = network.get_node_table(format='csv')
        print(node_table)

        edge_table = network.get_edge_table()
        print(edge_table)

        print('\n---------- CyNetwork Tests Finished! -----------\n')

    def test_convert(self):
        print('\n---------- DataFrame Conversion Tests Start -----------\n')
        import os
        dir_name = os.path.dirname(os.path.realpath(__file__))
        df = pd.read_csv(dir_name + '/data/galFiltered.sif', names=[
                                                                           'source',
                                                         'interaction', 'target'], sep=' ')
        print(df.head(3))
        net = df_util.from_dataframe(df)

        network = self.client.network.create(data=net, name='Created from DataFrame')
        # print(network)
        dir_name = os.path.dirname(os.path.realpath(__file__))
        data_table = pd.read_csv(dir_name +
                                 '/data/galFiltered.nodeAttrTable.txt', sep='\t')
        network.update_node_table(df=data_table, data_key_col='ID')
        print('\n---------- DataFrame Conversion Tests Finished! -----------\n')

    def test_delete_network(self):
        network = self.client.network.create()
        suids = self.client.network.get_all()
        self.assertEqual(1, len(suids))
        self.client.network.delete(network)
        suids = self.client.network.get_all()
        self.assertEqual(0, len(suids))

    def test_create_from_networkx(self):
        networkx1 = nx.scale_free_graph(100)

        network = self.client.network.create_from_networkx(networkx1)
        self.assertIsNotNone(network)
