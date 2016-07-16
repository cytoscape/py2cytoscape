import numpy as np


def from_ndarray(data, name=None, labels=None, directed=False, weighted=False):
    mat_dim = data.shape
    if mat_dim[0] != mat_dim[1]:
        raise ValueError('Data should be square matrix.')
    data_size = mat_dim[0]

    if labels is not None:
        label_len = len(labels)
        if label_len != data_size:
            raise ValueError('Label length is not equal to the size of data.')

    network_name = name
    if network_name is None:
        network_name = 'from ndarray'

    g = {
        'data': {
            'name': network_name
        },
        'elements': {
            'nodes': [],
            'edges': []
        }
    }

    g['elements']['nodes'] = __get_nodes(labels, data_size)

    if weighted:
        g['elements']['edges'] = __get_weighted_edges(matrix=data)
    else:
        g['elements']['edges'] = __get_unweighted_edges(matrix=data)

    return g

def __get_nodes(labels, size):

    nodes = []
    if labels is None:
        node_labels = np.arange(size)
    else:
        node_labels = labels

    for idx, label in enumerate(node_labels):
        nodes.append(__get_node(idx, label))

    return nodes


def __get_node(node_id, name):
    n = {
        'data': {
            'id': str(node_id),
            'name': str(name)
        }
    }
    return n


def __get_egdes(matrix, labels):
    pass


def __get_edge(source, target, weight=None):
    e = {
        'data': {
            'id': source + '-' + target,
            'source': source,
            'target': target
        }
    }

    if weight is not None:
        e['data']['weight'] = weight

    return e


def __get_unweighted_edges(matrix):
    size = matrix.shape[0]

    edges = []
    row_idx = 0
    for row in matrix:
        idx = row_idx
        while idx < size:
            if row[idx] == 1:
                e = __get_edge(str(row_idx), str(idx))
                edges.append(e)
            idx += 1
        row_idx += 1
    return edges


def __get_weighted_edges(matrix):
    size = matrix.shape[0]
    edges = []
    row_idx = 0
    for row in matrix:
        idx = row_idx
        while idx < size:
            if not np.isnan(row[idx]):
                e = __get_edge(str(row_idx), str(idx), weight=row[idx])
                edges.append(e)
            idx += 1
        row_idx += 1
    return edges
    pass


