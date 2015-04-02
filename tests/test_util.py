import unittest
import json
import os

import igraph as ig

import networkx as nx
from py2cytoscape import util

import scipy as sp
import tempfile


# Utilities
def compare_edge_sets(nx_edges, cy_edges):
    edge_set = set()
    for cyedge in cy_edges:
        source = cyedge['data']['source']
        target = cyedge['data']['target']
        edge = (long(source), long(target))
        edge_set.add(edge)

    return edge_set.difference(nx_edges)


class NetworkConversionTests(unittest.TestCase):

    def test_networkx_emptynetwork(self):
        g = nx.Graph()
        cyjs_g = util.from_networkx(g)

        print('\n---------- Empty Test Start -----------\n')
        print(json.dumps(cyjs_g, indent=4))

        self.assertIsNotNone(cyjs_g)
        self.assertIsNotNone(cyjs_g['data'])
        self.assertEqual(0, len(cyjs_g['elements']['nodes']))
        self.assertEqual(0, len(cyjs_g['elements']['edges']))

    def test_networkx_edge_attribute(self):
        print('\n---------- Edge Att Test Start -----------\n')
        g = nx.Graph()
        g.add_edge(1, 2, interaction='itr1',  score=0.1)
        original_edge = g[1][2]
        print(original_edge.keys())
        cyjs = util.from_networkx(g)

        print(json.dumps(cyjs, indent=4))

        # There is only one edge, so this should be OK...
        edge = cyjs['elements']['edges'][0]
        print(json.dumps(edge, indent=4))

        self.assertEqual('itr1', cyjs['elements']['edges'][0]['data']['interaction'])

    def test_networkx_empty_edge_attribute(self):
        print('\n---------- Edge Att Test 2 Start -----------\n')
        g = nx.scale_free_graph(5)
        cyjs = util.from_networkx(g)

        print(json.dumps(cyjs, indent=4))

        # There is only one edge, so this should be OK...
        edge = cyjs['elements']['edges'][0]
        print(json.dumps(edge, indent=4))
        self.assertEqual(2, len(edge['data']))


    def test_networkx_ba(self):
        g = nx.barabasi_albert_graph(100, 3)
        nodes = g.nodes()
        edges = g.edges()

        g.graph['name'] = 'ba test'
        cyjs_g = util.from_networkx(g)

        print('\n---------- BA graph Test Start -----------\n')

        self.assertIsNotNone(cyjs_g)
        self.assertIsNotNone(cyjs_g['data'])
        self.assertEqual('ba test', cyjs_g['data']['name'])
        self.assertEqual(len(nodes), len(cyjs_g['elements']['nodes']))
        self.assertEqual(len(edges), len(cyjs_g['elements']['edges']))

        diff = compare_edge_sets(set(edges), cyjs_g['elements']['edges'])
        self.assertEqual(0, len(diff))

    def test_networkx_matrix(self):
        print('\n---------- Matrix Test Start -----------\n')

        g = nx.barabasi_albert_graph(30, 2)
        nodes = g.nodes()
        edges = g.edges()
        print(edges)

        mx1 = nx.adjacency_matrix(g)
        fp = tempfile.NamedTemporaryFile()
        file_name = fp.name
        sp.savetxt(file_name, mx1.toarray(), fmt='%d')

        # Load it back to matrix
        mx2 = sp.loadtxt(file_name)
        fp.close()

        g2 = nx.from_numpy_matrix(mx2)
        cyjs_g = util.from_networkx(g2)

        #print(json.dumps(cyjs_g, indent=4))

        self.assertIsNotNone(cyjs_g)
        self.assertIsNotNone(cyjs_g['data'])
        self.assertEqual(len(nodes), len(cyjs_g['elements']['nodes']))
        self.assertEqual(len(edges), len(cyjs_g['elements']['edges']))

        # Make sure all edges are reproduced
        print(set(edges))
        diff = compare_edge_sets(set(edges), cyjs_g['elements']['edges'])
        self.assertEqual(0, len(diff))

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

        j_nodes = jsonData['elements']['nodes']
        j_edges = jsonData['elements']['edges']

        print('\n---------- JSON Loading Test Start -----------\n')
        # print(json.dumps(jsonData, indent=4))
        g = util.to_networkx(jsonData)
        nodes = g.nodes()
        edges = g.edges()

        self.assertEqual('Yeast Network Sample', g.graph['name'])
        self.assertEqual('Sample network created by JSON export.', g.graph['description'])
        self.assertEqual(4, len(g.graph['numberList']))

        self.assertEqual(len(j_nodes), len(nodes))
        self.assertEqual(len(j_edges), len(edges))

        edge_set = set(list(map(lambda x: (long(x[0]), long(x[1])), edges)))
        self.assertEqual(0, len(compare_edge_sets(edge_set, j_edges)))

    def test_networkx_roundtrip(self):
        print('\n---------- NetworkX Data Roundtrip Test Start -----------\n')

        g = nx.newman_watts_strogatz_graph(100, 3, 0.5)
        nodes = g.nodes()
        edges = g.edges()

        # Add some attributes
        g.graph['name'] = 'original'
        g.graph['density'] = nx.density(g)

        nx.set_node_attributes(g, 'betweenness', nx.betweenness_centrality(g))
        nx.set_node_attributes(g, 'degree', nx.degree(g))
        nx.set_node_attributes(g, 'closeness', nx.closeness_centrality(g))

        nx.set_edge_attributes(g, 'eb', nx.edge_betweenness(g))

        cyjs1 = util.from_networkx(g)
        g2 = util.to_networkx(cyjs1)

        self.assertEqual(len(g2.nodes()), len(nodes))
        self.assertEqual(len(g2.edges()), len(edges))

        edge_set = set(list(map(lambda x: (long(x[0]), long(x[1])), g2.edges())))
        self.assertEqual(0, len(edge_set.difference(set(edges))))

        node_original = g.node[1]
        node_generated = g2.node['1']

        print(node_original)
        print(node_generated)

        self.assertEqual(node_original['degree'], node_generated['degree'])
        self.assertEqual(node_original['betweenness'], node_generated['betweenness'])
        self.assertEqual(node_original['closeness'], node_generated['closeness'])

    def test_from_igraph(self):
        print('---------- From igraph object to Cytoscape.js -----------\n')
        empty = ig.Graph()
        cyjs = util.from_igraph(empty)

        print(json.dumps(cyjs, indent=4))

        self.assertIsNotNone(cyjs)
        self.assertIsNotNone(cyjs['data'])
        self.assertEqual(0, len(cyjs['elements']['nodes']))
        self.assertEqual(0, len(cyjs['elements']['edges']))

    def test_from_igraph_random(self):
        print('---------- From igraph random network object to Cytoscape.js -----------\n')
        ba_graph = ig.Graph.Barabasi(100, 3)
        ba_graph['name'] = 'Barabasi'
        ba_graph['number_attr'] = 12345

        ba_graph.vs['degree'] = ba_graph.degree()
        ba_graph.vs['bw'] = ba_graph.betweenness()
        ba_graph.es['ebw'] = ba_graph.edge_betweenness()

        cyjs = util.from_igraph(ba_graph)

        # print(json.dumps(cyjs, indent=4))

        self.assertIsNotNone(cyjs)
        self.assertIsNotNone(cyjs['data'])
        self.assertEqual('Barabasi', cyjs['data']['name'])
        self.assertEqual(12345, cyjs['data']['number_attr'])
        cyjs_nodes = cyjs['elements']['nodes']
        cyjs_edges = cyjs['elements']['edges']
        self.assertEqual(len(ba_graph.vs), len(cyjs_nodes))
        self.assertEqual(len(ba_graph.es), len(cyjs_edges))

        self.assertEqual(ba_graph.vs[0]['degree'], cyjs_nodes[0]['data']['degree'])
        self.assertEqual(ba_graph.vs[0]['bw'], cyjs_nodes[0]['data']['bw'])

        # Test edge
        target_edge = ba_graph.es[10]
        edge0 = None
        for e in cyjs_edges:
            if e['data']['source'] == str(target_edge.source) \
                    and e['data']['target'] == str(target_edge.target):
                edge0 = e
                break

        self.assertIsNotNone(edge0)
        self.assertEqual(target_edge['ebw'], edge0['data']['ebw'])


if __name__ == '__main__':
    unittest.main()