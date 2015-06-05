# -*- coding: utf-8 -*-
"""

Conversion utilities for igraph

"""

DEF_SCALING = 1.0


def from_igraph(igraph_network, layout=None, scale=DEF_SCALING):
    new_graph = {}
    network_data = {}
    elements = {}
    nodes = []
    edges = []

    # Convert network attributes
    network_attr = igraph_network.attributes()
    for key in network_attr:
        network_data[key] = igraph_network[key]

    # get network as a list of edges
    edges_original = igraph_network.es
    nodes_original = igraph_network.vs

    node_attr = igraph_network.vs.attributes()
    for idx, node in enumerate(nodes_original):
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

    # Add edges to the elements
    edge_attr = igraph_network.es.attributes()
    for edge in edges_original:
        new_edge = {}
        data = {}
        data['source'] = str(edge.source)
        data['target'] = str(edge.target)
        for key in edge_attr:
            data[key] = edge[key]
        new_edge['data'] = data
        edges.append(new_edge)

    elements['nodes'] = nodes
    elements['edges'] = edges
    new_graph['elements'] = elements
    new_graph['data'] = network_data

    return new_graph
