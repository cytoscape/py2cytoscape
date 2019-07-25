__author__ = 'kono'

import warnings
warnings.warn('\n\n\n**** data.util_network will be deprecated in the next py2cytoscape release. ****\n\n\n')


class NetworkUtil(object):

    @staticmethod
    def name2suid(network, obj_type='node'):
        if obj_type is 'node':
            table = network.get_node_table()
        elif obj_type is 'edge':
            table = network.get_edge_table()
        else:
            raise ValueError('No such object type: ' + obj_type)

        subset= table['name']
        name2suid = {}
        for suid in subset.index:
            name2suid[subset[suid]] = suid

        table.set_index(["SUID"],inplace=True)
        return name2suid
