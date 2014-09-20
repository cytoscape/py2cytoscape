import unittest
import networkx as nx
import json


from py2cytoscape import util

class NetworkConversionTests(unittest.TestCase):

    def test_networkx_emptynetwork(self):
        g = nx.Graph()
        cyjs_g = util.from_networkx(g)

        print('\n---------- Test Start -----------\n')
        print(json.dumps(cyjs_g, indent=4))

        self.assertIsNotNone(cyjs_g)
        self.assertIsNotNone(cyjs_g['data'])
        self.assertEqual(0, len(cyjs_g['elements']['nodes']))
        self.assertEqual(0, len(cyjs_g['elements']['edges']))


    def test_networkx_gml(self):
        g = nx.read_gml('tests/data/galFiltered.gml')
        cyjs_g = util.from_networkx(g)

        print('\n---------- Test Start -----------\n')
        print(json.dumps(cyjs_g, indent=4))

        self.assertIsNotNone(cyjs_g)
        self.assertIsNotNone(cyjs_g['data'])
        self.assertEqual(331, len(cyjs_g['elements']['nodes']))
        self.assertEqual(362, len(cyjs_g['elements']['edges']))
