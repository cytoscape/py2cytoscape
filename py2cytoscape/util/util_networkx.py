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


def __map_table_data(columns, graph_obj):
    data = {}
    for col in columns:
        data[col] = graph_obj[col]

    return data


def __create_node(node, node_id):
    node_columns = node.keys()
    data = __map_table_data(node_columns, node)
    # Override special keys
    data[ID] = str(node_id)
    data[NAME] = str(node_id)

    return {
        DATA: data
    }


def __create_edge(edge_tuple, g):
    edge =g[edge_tuple[0]][edge_tuple[1]]
    # FIXME Handle multiple edges.
    data = __map_table_data(edge.keys(), edge)[0]
    data['source'] = str(edge_tuple[0])
    data['target'] = str(edge_tuple[1])

    return {
        DATA: data
    }


def __build_empty_graph():
    empty_graph = {
        'data': {},
        'elements': {
            'nodes': [],
            'edges': []
        }
    }
    return empty_graph


def from_networkx(g):
    cygraph = __build_empty_graph()
    nodes = g.nodes()
    edges = g.edges()

    # Map network table data
    cygraph[DATA] = __map_table_data(g.graph.keys(), g.graph)

    for node_id in nodes:
        cygraph['elements']['nodes'].append(__create_node(g.node[node_id], node_id))

    for edge in edges:
        cygraph['elements']['edges'].append(__create_edge(edge, g))

    return cygraph


def to_networkx(cyjs, directed=True):
    if directed:
        g = nx.MultiDiGraph()
    else:
        g = nx.MultiGraph()

    print(cyjs)
    return g