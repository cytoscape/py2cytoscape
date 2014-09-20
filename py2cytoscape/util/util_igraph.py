# -*- coding: utf-8 -*-
"""

Conversion utilities for igraph

"""

DEF_SCALING = 1.0

def from_igraph(igraph_network, layout, scale=DEF_SCALING):
    new_graph = {}
    elements = {}
    nodes = []
    edges = []

    el = igraph_network.get_edgelist()
    nodes_original = igraph_network.vs

    node_attr = igraph_network.vs.attributes()

    idx = 0
    for node in nodes_original:
        new_node = {}
        data = {}
        data['id'] = str(node.index)
        data['name'] = str(node.index)
        for key in node_attr:
            data[key] = node[key]
        new_node['data'] = data
        if layout is not None:
            position = {}
            position['x'] = layout[idx][0] * scale
            position['y'] = layout[idx][1] * scale
            new_node['position'] = position

        nodes.append(new_node)
        idx = idx + 1

    for edge in el:
        new_edge = {}
        data = {}
        data['source'] = str(edge[0])
        data['target'] = str(edge[1])
        new_edge['data'] = data
        edges.append(new_edge)

    elements['nodes'] = nodes
    elements['edges'] = edges
    new_graph['elements'] = elements

    return new_graph