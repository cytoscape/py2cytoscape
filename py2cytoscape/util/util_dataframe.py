import pandas as pd

from . import cytoscapejs as cyjs


def from_dataframe(df,
                   source_col='source',
                   target_col='target',
                   interaction_col='interaction',
                   name='From DataFrame',
                   edge_attr_cols=[]):
    """
    Utility to convert Pandas DataFrame object into Cytoscape.js JSON

    :param df: Dataframe to convert.
    :param source_col: Name of source column.
    :param target_col: Name of target column.
    :param interaction_col: Name of interaction column.
    :param name: Name of network.
    :param edge_attr_cols: List containing other columns to consider in df as
        edges' attributes.
    :return: Dictionary version of df.
    """

    network = cyjs.get_empty_network(name=name)
    nodes = set()
    if edge_attr_cols is None:
        edge_attr_cols = []

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

        extra_values = {column: row[column]
                        for column in edge_attr_cols
                        if column in df.columns}

        network['elements']['edges'].append(
            get_edge(s, t, interaction=row[interaction_col], **extra_values)
        )
    return network


def to_dataframe(network,
                 interaction='interaction',
                 default_interaction='-',
                 edges_attr_cols=[]):
    """
    Utility to convert a Cytoscape dictionary into a Pandas Dataframe.

    :param network: Dictionary to convert.
    :param interaction: Name of interaction column.
    :param default_interaction: Default value for missing interactions.
    :param edges_attr_cols: List containing other edges' attributes to include
        in the Dataframe, if present in network.
    :return: Converted Pandas Dataframe.
    """

    edges = network['elements']['edges']
    if edges_attr_cols is None:
        edges_attr_cols = []
    edges_attr_cols = sorted(edges_attr_cols)

    network_array = []
    # the set avoids duplicates
    valid_extra_cols = set()
    for edge in edges:
        edge_data = edge['data']
        source = edge_data['source']
        target = edge_data['target']
        if interaction in edge_data:
            itr = edge_data[interaction]
        else:
            itr = default_interaction
        extra_values = []
        for extra_column in edges_attr_cols:
            if extra_column in edge_data:
                extra_values.append(edge_data[extra_column])
                valid_extra_cols.add(extra_column)
        row = tuple([source, itr, target] + extra_values)
        network_array.append(row)

    return pd.DataFrame( network_array, columns=['source', 'interaction', 'target'] + sorted(valid_extra_cols))


def get_node(id):
    node = {
        'data': {
            'id': str(id),
            'name': str(id)
        }
    }
    return node


def get_edge(source, target, interaction, **kwargs):
    if interaction is None:
        itr = '-'
    else:
        itr = interaction

    edge = {
        'data': {
            'source': source,
            'target': target,
            'interaction': itr
        }
    }

    # inserts extra <key:value> in the edge.
    for key, value in kwargs.items():
        edge["data"][key] = value

    return edge
