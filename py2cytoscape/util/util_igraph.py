# -*- coding: utf-8 -*-
"""

Conversion utilities for igraph

"""

try:
    import igraph as ig
except Exception as error:
    print(str(error))
    print("py2cytoscape: Error importing igraph. You won't be able to import from igraph.")
    ig = None

DEF_SCALING = 100.0


def from_igraph(igraph_network, layout=None, scale=DEF_SCALING):
    if ig is None:
        raise ImportError('igraph not found')

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


def to_igraph(network):

    nodes = network['elements']['nodes']
    edges = network['elements']['edges']
    network_attr = network['data']

    node_count = len(nodes)
    edge_count = len(edges)

    g = ig.Graph()

    # Graph attributes
    for key in network_attr.keys():
        g[key] = network_attr[key]

    g.add_vertices(nodes)

    # Add node attributes
    node_attributes = {}
    node_id_dict = {}
    for i, node in enumerate(nodes):
        data = node['data']
        for key in data.keys():
            if key not in node_attributes:
                node_attributes[key] = [None] * node_count

            # Save index to map
            if key == 'id':
                node_id_dict[data[key]] = i

            node_attributes[key][i] = data[key]

    for key in node_attributes.keys():
        g.vs[key] = node_attributes[key]

    # Create edges
    edge_tuples = []
    edge_attributes = {}
    for i, edge in enumerate(edges):
        data = edge['data']
        source = data['source']
        target = data['target']
        edge_tuple = (node_id_dict[source], node_id_dict[target])
        edge_tuples.append(edge_tuple)
        for key in data.keys():
            if key not in edge_attributes:
                edge_attributes[key] = [None] * edge_count

            # Save index to map
            edge_attributes[key][i] = data[key]

    g.add_edges(edge_tuples)

    # Assign edge attributes
    for key in edge_attributes.keys():
        if key == 'source' or key == 'target':
            continue
        else:
            g.es[key] = edge_attributes[key]

    return g
