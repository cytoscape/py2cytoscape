"""
*******
Data conversion utility for NetworkX
*******

Convert cytoscape.js style graphs from/to NetworkX object.

https://networkx.github.io/

"""

import networkx as nx

# Special Keys
ID = 'id'
NAME = 'name'
DATA = 'data'
ELEMENTS = 'elements'

NODES = 'nodes'
EDGES = 'edges'

SOURCE = 'source'
TARGET = 'target'


def __map_table_data(columns, graph_obj):
    data = {}
    for col in columns:
        data[col] = graph_obj[col]

    return data


def __create_node(node, node_id):
    new_node = {}
    node_columns = node.keys()
    data = __map_table_data(node_columns, node)
    # Override special keys
    data[ID] = str(node_id)
    data[NAME] = str(node_id)

    if 'position' in node.keys():
        position = node['position']
        new_node['position'] = position

    new_node[DATA] = data
    return new_node


def __create_edge(edge_tuple, g):
    edge = g[edge_tuple[0]][edge_tuple[1]]
    data = __map_table_data(edge.keys(), edge)

    data['source'] = str(edge_tuple[0])
    data['target'] = str(edge_tuple[1])
    return {DATA: data}


def __build_empty_graph():
    return {
        DATA: {},
        ELEMENTS: {
            NODES: [],
            EDGES: []
        }
    }


def from_networkx(g):
    cygraph = __build_empty_graph()
    nodes = g.nodes()
    edges = g.edges()

    # print('NetworkX egdes = ' + str(g.number_of_edges()))
    # print('egdes len = ' + str(len(edges)))

    # Map network table data
    cygraph[DATA] = __map_table_data(g.graph.keys(), g.graph)

    for node_id in nodes:
        cygraph['elements']['nodes'].append(__create_node(g.node[node_id], node_id))

    for edge in edges:
        cygraph['elements']['edges'].append(__create_edge(edge, g))

    return cygraph


def to_networkx(cyjs, directed=True):
    """
    Convert Cytoscape.js-style JSON object into NetworkX object.

    By default, data will be handles as a directed graph.
    """

    if directed:
        g = nx.MultiDiGraph()
    else:
        g = nx.MultiGraph()

    network_data = cyjs[DATA]
    if network_data is not None:
        for key in network_data.keys():
            g.graph[key] = network_data[key]

    nodes = cyjs[ELEMENTS][NODES]
    edges = cyjs[ELEMENTS][EDGES]

    for node in nodes:
        data = node[DATA]
        g.add_node(data[ID], attr_dict=data)

    for edge in edges:
        data = edge[DATA]
        source = data[SOURCE]
        target = data[TARGET]

        g.add_edge(source, target, attr_dict=data)

    return g