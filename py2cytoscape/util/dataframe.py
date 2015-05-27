import pandas as pd
import cytoscapejs as cyjs

def from_dataframe(df, source_col='source', target_col='target', interaction_col='interaction',
                   name='From DataFrame', edge_attr_cols=[]):
    """
    Utility to convert Pandas DataFrame object into Cytoscape.js JSON

    :param df:
    :param source_col:
    :param target_col:
    :param interaction_col:
    :param name:
    :param edge_attr_cols:
    :return:
    """
    network = cyjs.get_empty_network(name=name)
    nodes = set()

    for index, row in df.iterrows():
        s = row[source_col]
        t = row[target_col]
        if s not in nodes:
            nodes.add(s)
            source = get_node(s)
            network['elements']['nodes'].append(source)
        if t not in nodes:
            nodes.add(t)
            target = get_node(t)
            network['elements']['nodes'].append(target)

        network['elements']['edges'].append(get_edge(s, t, interaction='pp'))
    return network

def get_node(id):
    node = {
        'data': {
            'id': str(id),
            'name': str(id)
        }
    }
    return node

def get_edge(source, target, interaction):
    edge = {
        'data': {
            'source': source,
            'target': target,
            'interaction': interaction
        }
    }

    return edge
