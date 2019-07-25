# -*- coding: utf-8 -*-
import copy

import warnings
warnings.warn('\n\n\n**** util.cytoscapejs will be deprecated in the next py2cytoscape release. ****\n\n\n')


EMPTY_NETWORK = {
    'data': {
    },

    'elements': {
        'nodes': [],
        'edges': []
    }
}


def get_empty_network(name='Empty Network'):
    empty_network = copy.deepcopy(EMPTY_NETWORK)
    empty_network['data']['name'] = name
    return empty_network
