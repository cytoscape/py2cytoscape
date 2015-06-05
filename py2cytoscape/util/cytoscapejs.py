# -*- coding: utf-8 -*-
import copy

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
