# -*- coding: utf-8 -*-

import unittest

import networkx as nx

from py2cytoscape.data.cyrest_client import CyRestClient
import py2cytoscape.util.dataframe as df_util
import json


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

    def test_create_from(self):
        print('\n---------- Loading network tests start -----------\n')
        # Create from URL
        locations = [
            'http://chianti.ucsd.edu/cytoscape-data/galFiltered.sif',
            'http://www.ebi.ac.uk/Tools/webservices/psicquic/intact/'
            + 'webservices/current/search/interactor/brca2_human?format=xml25'

        ]

        networks = self.client.network.create_from(locations)
        print(networks)
        self.assertIsNotNone(networks)
        print('---------- Loading networks done! -----------\n')

    def test_network_api(self):
        print('\n---------- Network API Tests Start -----------\n')
        # Create empty network
        for i in range(5):
            self.client.network.create()

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
        print(edge)

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

    def test_create_view(self):
        print('\n---------- CyNetworkView Tests Start -----------\n')
        network = self.client.network.create()
        self.assertIsNotNone(network)
        nodes = network.get_nodes()
        pp(nodes)
        new_nodes = ['a', 'b', 'c']
        nd = network.add_nodes(new_nodes)
        views = network.get_views()
        print('Views: ')
        print(views)
        view_id = views[0]
        view = network.get_view(view_id, format='view')
        self.assertIsNotNone(view)
        self.assertEqual(view_id, view.get_id())

        node_views = view.get_node_views()
        self.assertIsNotNone(node_views)
        self.assertEqual(3, len(node_views))

        view1 = node_views[0]
        self.assertIsNotNone(view1)
        all_values = view1.get_values()
        print(all_values)

    def test_view_api(self):
        print('\n---------- View API test start -----------\n')
        network = self.client.network.create()
        self.assertIsNotNone(network)
        nodes = network.get_nodes()
        pp(nodes)
        new_nodes = ['a', 'b', 'c']
        nd = network.add_nodes(new_nodes)
        print(nd)
        views = network.get_views()
        print('Views: ')
        print(views)
        view_id = views[0]
        view = network.get_view(view_id, format='view')
        self.assertIsNotNone(view)
        self.assertEqual(view_id, view.get_id())

        node_views = view.get_node_views()
        self.assertIsNotNone(node_views)
        self.assertEqual(3, len(node_views))

        view1 = node_views[0]
        self.assertIsNotNone(view1)
        self.assertEqual(0, view1.get_x())
        view1.set_x(100)
        self.assertEqual(100, view1.get_value('NODE_X_LOCATION'))

        new_values = {}
        for key in nd.keys():
            suid = nd[key]
            new_values[suid] = 'red'

        view.update_node_views('NODE_FILL_COLOR', new_values)

        new_values_name = {}
        for node_name in new_nodes:
            new_values_name[node_name] = 'pink'

        print('---------- New Fill colors -----------')
        print(new_values_name)

        view.update_node_views('NODE_FILL_COLOR', new_values_name, key_type='name')
        view.update_network_view('NETWORK_BACKGROUND_PAINT', 'red')
        net_view = view.get_network_view_as_dict()
        bg_paint = net_view['NETWORK_BACKGROUND_PAINT']
        self.assertEqual('#FF0000', bg_paint)

    def test_convert(self):
        print('\n---------- DataFrame Conversion Tests Start -----------\n')

        import os
        import pandas as pd

        # Clean up Cytoscape session
        self.client.session.delete()

        dir_name = os.path.dirname(os.path.realpath(__file__))
        df = pd.read_csv(
            dir_name + '/data/galFiltered.sif',
            names=['source', 'interaction', 'target'], sep=' ')
        print(df.head(3))
        net = df_util.from_dataframe(df)

        network = self.client.network.create(data=net, name='Created from DataFrame')

        original_column_count = len(network.get_node_columns())

        dir_name = os.path.dirname(os.path.realpath(__file__))
        file_name = dir_name + '/data/galFiltered.nodeAttrTable.txt'
        data_table = pd.read_csv(file_name, sep='\t')

        network.update_node_table(df=data_table, data_key_col='ID')
        table_column_count = len(data_table.columns)
        total_column_count = len(network.get_node_columns())

        self.assertEqual(total_column_count, (original_column_count+table_column_count-1))

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
