"""
*******
Data conversion utility for NetworkX
*******

Convert cytoscape.js style graphs from/to NetworkX object.

https://networkx.github.io/

"""

import networkx as nx


def from_networkx(G):
    new_graph = {}
    elements = {}
    nodes = []
    edges = []

    nodes_x = G.nodes()
    edges_x = G.edges()

    # Network Attributes
    net_attr_keys = G.graph.keys()
    network_data = {}
    for net_key in net_attr_keys:
        network_data[net_key] = G.graph[net_key]

    new_graph['data'] = network_data

    for node in nodes_x:
        new_node = {}
        data = {}
        data['id'] = str(node)
        data['name'] = str(node)
        for key in G.node[node].keys():
            data[key] = G.node[node][key]
        new_node['data'] = data
        nodes.append(new_node)

    for edge in edges_x:
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


def to_networkx(cyjs, directed=True):
    if directed:
        g = nx.MultiDiGraph()
    else:
        g = nx.MultiGraph()


    print(cyjs)
    return g