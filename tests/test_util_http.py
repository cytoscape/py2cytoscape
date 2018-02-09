
import unittest
import warnings

from py2cytoscape.data.cynetwork import CyNetwork
from py2cytoscape.data.cyrest_client import CyRestClient
from py2cytoscape.data.util_network import NetworkUtil


class CheckResponseTests(unittest.TestCase):

    def setUp(self):
        self.client = CyRestClient()
        self.client.network.delete_all()        
        locations = [
            'http://chianti.ucsd.edu/cytoscape-data/galFiltered.sif'
        ]
        self.network = self.client.network.create_from(locations)
        view_id_list = self.network.get_views() 
        self.view = self.network.get_view(view_id_list[0], format='view')        

    def test_network_view(self):
        # 'arc' is AssertRaisesContext
        with self.assertRaises(Exception) as arc: 
            # Try to request with non-integer values            
            self.view.update_network_view(visual_property="NETWORK_CENTER_X_LOCATION",
                                          value="non-integer-value")
        # end of with
        
        res = arc.exception.response
        self.assertEqual(res.status_code, 500)
        print(arc.exception.args[0]) # HTTP status code information
        print(arc.exception.args[1]) # Error message
    # end of def
    
    def test_node_views(self):
        d_nodes = self.view.get_node_views_as_dict()
        vals = {}
        for node_id in d_nodes:
            vals[node_id] = "non-integer-value" # Non-integer
        with self.assertRaises(Exception) as arc:
            # Try to request with non-integer values            
            self.view.update_node_views(visual_property="NODE_X_LOCATION", values=vals)
        # end of with
        
        res = arc.exception.response
        self.assertEqual(res.status_code, 500)
        print(arc.exception.args[0]) # HTTP status code information
        print(arc.exception.args[1]) # Error message
    # end of def
    
    def test_edge_views(self):
        d_edges = self.view.get_edge_views_as_dict()
        vals = {}
        for edge_id in d_edges:
            vals[edge_id] = "non-integer-value`" # Non-integer
        with self.assertRaises(Exception) as arc:
            # Try to request with non-integer values            
            self.view.update_edge_views(visual_property="EDGE_LABEL_WIDTH", values=vals)
        # end of with
        
        res = arc.exception.response
        self.assertEqual(res.status_code, 500)
        print(arc.exception.args[0]) # HTTP status code information
        print(arc.exception.args[1]) # Error message
    # end of def
    
# end of class

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
