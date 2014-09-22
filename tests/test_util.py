import unittest
import json

import networkx as nx

from py2cytoscape import util


class NetworkConversionTests(unittest.TestCase):
    def test_networkx_emptynetwork(self):
        g = nx.Graph()
        cyjs_g = util.from_networkx(g)

        print('\n---------- Empty Test Start -----------\n')
        # print(json.dumps(cyjs_g, indent=4))

        self.assertIsNotNone(cyjs_g)
        self.assertIsNotNone(cyjs_g['data'])
        self.assertEqual(0, len(cyjs_g['elements']['nodes']))
        self.assertEqual(0, len(cyjs_g['elements']['edges']))


    def test_networkx_gml(self):
        g = nx.read_gml('tests/data/galFiltered.gml')
        g.graph['name'] = 'gml_test'

        cyjs_g = util.from_networkx(g)

        print('\n---------- GML Test Start -----------\n')
        # print(json.dumps(cyjs_g, indent=4))

        self.assertIsNotNone(cyjs_g)

        net_data = cyjs_g['data']
        self.assertIsNotNone(net_data)
        self.assertEqual('gml_test', net_data['name'])
        self.assertEqual(331, len(cyjs_g['elements']['nodes']))
        self.assertEqual(362, len(cyjs_g['elements']['edges']))

        nodes = cyjs_g['elements']['nodes']
        node0 = nodes[0]
        self.assertEqual(type("1"), type(node0['data']['id']))

    def test_networkx_scale_free(self):
        g = nx.scale_free_graph(100)
        edge_count = g.number_of_edges()

        g.graph['name'] = 'scale_free_test'

        cyjs_g = util.from_networkx(g)

        print('\n---------- Scale free network Test Start -----------\n')
        print('Edge count = ' + str(edge_count))
        # print(json.dumps(cyjs_g, indent=4))

        self.assertIsNotNone(cyjs_g)

        net_data = cyjs_g['data']
        self.assertIsNotNone(net_data)
        self.assertEqual('scale_free_test', net_data['name'])
        self.assertEqual(100, len(cyjs_g['elements']['nodes']))
        self.assertEqual(edge_count, len(cyjs_g['elements']['edges']))

        nodes = cyjs_g['elements']['nodes']
        node0 = nodes[0]
        self.assertEqual(type("1"), type(node0['data']['id']))

    def test_networkx_parse_network(self):
        f = open('tests/data/galFiltered.json', 'r')
        jsonData = json.load(f)
        print('\n---------- JSON Loading Test Start -----------\n')
        # print(json.dumps(jsonData, indent=4))
        g = util.to_networkx(jsonData)
        nodes = g.nodes()
        edges = g.edges()

        # print(json.dumps(g.node[nodes[0]], indent=4))

        # TODO add more test cases!
        self.assertEqual('Yeast Network Sample', g.graph['name'])
        self.assertEqual('Sample network created by JSON export.', g.graph['description'])
        self.assertEqual(4, len(g.graph['numberList']))

        self.assertEqual(331, len(nodes))
        self.assertEqual(362, len(edges))