from py2cytoscape.data.cyrest_client import CyRestClient
from py2cytoscape.data.util_network import NetworkUtil

import unittest

class UtilNetworkTests(unittest.TestCase):

    def setUp(self):
        self.client = CyRestClient()
        # cleanup
        self.client.network.delete_all()

    def test_name2suid(self):
        print('\n---------- name2suid tests start -----------\n')
        locations = [
            'http://chianti.ucsd.edu/cytoscape-data/galFiltered.sif'
        ]
        network = self.client.network.create_from(locations)
        node_count = len(network.get_nodes())
        edge_count = len(network.get_edges())
        result = NetworkUtil.name2suid(network, obj_type='node')
        edge_result = NetworkUtil.name2suid(network, obj_type='edge')
        self.assertEqual(node_count, len(result))
        self.assertEqual(edge_count, len(edge_result))
