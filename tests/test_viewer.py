import unittest
import networkx as nx

from py2cytoscape.util import from_networkx


class CytoscapejsWidgetTests(unittest.TestCase):

    def test_get_style_names(self):
        from py2cytoscape.cytoscapejs import viewer as cyjs
        styles = cyjs.get_style_names()

        self.assertIsNotNone(styles)
        self.assertEqual(type(list()), type(styles))

        self.assertEqual(8, len(styles))

    def test_get_style(self):
        from py2cytoscape.cytoscapejs import viewer as cyjs
        def_style = cyjs.get_style('default')

        self.assertIsNotNone(def_style)
        self.assertEqual(type(list()), type(def_style))

        print(def_style)
        self.assertRaises(ValueError, cyjs.get_style, 'foo')

    def test_render(self):
        from py2cytoscape.cytoscapejs import viewer as cyjs
        g = nx.scale_free_graph(100)
        g_cyjs = from_networkx(g)
        result = cyjs.render(g_cyjs, layout_algorithm='circle')
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
