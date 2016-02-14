import json

import pandas as pd
import requests
from py2cytoscape.data.network_view import CyNetworkView

from ..util import util_networkx as nx_util
from ..util import dataframe as df_util

from . import BASE_URL, HEADERS

BASE_URL_NETWORK = BASE_URL + 'networks'
# JSON = 'json'


class CyNetwork(object):

    def __init__(self, suid=None):
        # Validate required argument
        if pd.isnull(suid):
            raise ValueError("SUID is missing.")
        else:
            self.__id = suid

        self.__url = BASE_URL_NETWORK + '/' + str(self.__id) + '/'

    def get_id(self):
        """
        Get session-unique ID of this network

        :return: SUID as integer
        """
        return self.__id

    def to_json(self):
        """
        Return this network in Cytoscape.js format.

        :return: Cytoscape.js Style JSON as dictionary.
        """
        return requests.get(self.__url).json()

    def to_networkx(self):
        """
        Return this network in NetworkX graph object.

        :return: Network as NetworkX graph object
        """
        return nx_util.to_networkx(requests.get(self.__url).json())

    def to_dataframe(self):
        """
        Return this network in pandas DataFrame.

        :return: Network as DataFrame.  This is equivalent to SIF.
        """
        return df_util.to_dataframe(requests.get(self.__url).json())

    def get_nodes(self):
        """
        Get all nodes as a list of SUIDs

        :return:
        """
        return requests.get(self.__url + 'nodes').json()

    def get_edges(self, format='suid'):
        if format is 'suid':
            return requests.get(self.__url + 'edges').json()
        elif format is 'edgelist':
            # TODO: implement this
            pass
        else:
            raise ValueError(format + ' is not supported for edge format.')

    def add_node(self, node_name):
        if node_name is None:
            return None
        return self.add_nodes([node_name])

    def add_nodes(self, node_name_list):
        """
        Add new nodes to the network

        :param node_name_list:
        :return:
        """
        nodes = requests.post(self.__url + 'nodes', data=json.dumps(
            node_name_list), headers=HEADERS).json()
        node_dict = {}
        for node in nodes:
            node_dict[node['name']] = node['SUID']
        return node_dict

    def add_edge(self, source, target, interaction='-', directed=True):
        new_edge = {
            'source': source,
            'target': target,
            'interaction': interaction,
            'directed': directed
        }
        edges = requests.post(self.__url + 'edges', data=json.dumps(
            [new_edge]), headers=HEADERS).json()
        return edges

    def add_edges(self, edge_list):
        new_egdes = []
        for edge_tuple in edge_list:
            new_edge = {
                'source': edge_tuple[0],
                'target': edge_tuple[1],
                'interaction': edge_tuple[2],
            }
            new_egdes.append(new_edge)

        edges = requests.post(self.__url + 'edges', data=json.dumps(
            new_egdes), headers=HEADERS).json()
        df = pd.DataFrame(edges)
        return df.set_index(['SUID'])

    def delete_node(self, id):
        url = self.__url + 'nodes/' + str(id)
        requests.delete(url)

    def delete_edge(self, id):
        url = self.__url + 'edges/' + str(id)
        requests.delete(url)

    def __get_table(self, type, format=None):
        url = self.__url + 'tables/default' + type
        if format is None or format is 'dataframe':
            uri = url + '.tsv'
            return pd.read_csv(uri, sep='\t', index_col=0, header=0)
        elif format is 'csv' or format is 'tsv':
            return requests.get(url + '.' + format).content
        elif format is 'cytoscapejs':
            return requests.get(url).json()['rows']
        else:
            raise ValueError('Unsupported format: ' + format)

    def get_node_table(self, format=None):
        return self.__get_table('node', format)

    def get_edge_table(self, format=None):
        return self.__get_table('edge', format)

    def get_network_table(self, format=None):
        return self.__get_table('network', format)

    def __get_columns(self, type=None):
        url = self.__url + 'tables/default' + type + '/columns'
        df = pd.DataFrame(requests.get(url).json())
        return df.set_index(['name'])

    def get_node_columns(self):
        """
        Get node table column information as DataFrame

        :return: Node column information ad DataFrame
        """
        return self.__get_columns('node')

    def get_edge_columns(self):
        """
        Get edge table column information as DataFrame

        :return: Edge column information ad DataFrame
        """
        return self.__get_columns('edge')

    def get_network_columns(self):
        """
        Get network table column information as DataFrame

        :return: Network column information ad DataFrame
        """
        return self.__get_columns('networks')

    def __get_column(self, type=None, column=None):
        url = self.__url + 'tables/default' + type + '/columns/' + column
        result = requests.get(url).json()
        return pd.Series(result['values'])

    def get_node_column(self, column):
        return self.__get_column('node', column=column)

    def get_edge_column(self, column):
        return self.__get_column('edge', column=column)

    def __get_value(self, type=None, id=None, column=None):
        if column is None and id is not None:
            # Extract a row in table
            url = self.__url + 'tables/default' + type + '/rows/' + str(id)
            return pd.Series(requests.get(url).json())
        elif column is not None and id is not None:
            url = self.__url + 'tables/default' + type + '/rows/' + str(id) + '/' + column
            return requests.get(url).content
        else:
            raise ValueError('ID is required.')

    def get_node_value(self, id, column=None):
        return self.__get_value(type='node', id=id, column=column)

    def get_edge_value(self, id, column=None):
        return self.__get_value(type='edge', id=id, column=column)

    def get_network_value(self, column):
        return self.__get_value(type='network', id=self.__id, column=column)

    def update_node_table(self, df=None, network_key_col='name',
                          data_key_col=None):
        return self.__update_table('node', df=df, network_key_col=network_key_col, data_key_col=data_key_col)

    def __update_table(self, type, df, network_key_col='name',
                       data_key_col=None):

        if data_key_col is None:
            # Use index
            data_key = 'index'
        else:
            data_key = data_key_col

        table = {
            'key': network_key_col,
            'dataKey': data_key
        }

        data = df.to_json(orient='records')
        table['data'] = json.loads(data)
        url = self.__url + 'tables/default' + type
        requests.put(url, json=table, headers=HEADERS)

    def __delete_column(self, type, column):
        url = self.__url + 'tables/default' + type + '/columns/' + column
        requests.delete(url)

    def delete_node_table_column(self, column):
        self.__delete_column('node', column=column)

    def delete_edge_table_column(self, column):
        self.__delete_column('edge', column=column)

    def delete_network_table_column(self, column):
        self.__delete_column('network', column=column)

    def __create_column(self, type, name, data_type, immutable, list):
        url = self.__url + 'tables/default' + type + '/columns'
        new_column = {
            'name': name,
            'type': data_type,
            'immutable': immutable,
            'list': list
        }
        requests.post(url, data=json.dumps(new_column), headers=HEADERS)

    def create_node_column(self, name, data_type='String', is_immutable=False, is_list=False):
        self.__create_column('node', name=name, data_type=data_type, immutable=is_immutable, list=is_list)

    def create_edge_column(self, name, data_type='String', is_immutable=False, is_list=False):
        self.__create_column('edge', name=name, data_type=data_type, immutable=is_immutable, list=is_list)

    def create_network_column(self, name, data_type='String', is_immutable=False, is_list=False):
        self.__create_column('network', name=name, data_type=data_type, immutable=is_immutable, list=is_list)


    # Utility functions
    def get_neighbours(self, node_id):
        url = self.__url + 'nodes/' + str(node_id) + '/neighbors'
        return requests.get(url).json()

    def get_adjacent_edges(self, node_id):
        url = self.__url + 'nodes/' + str(node_id) + '/adjEdges'
        return requests.get(url).json()


    # Views
    def get_views(self):
        """
        Get views as a list of SUIDs

        :return:
        """
        url = self.__url + 'views'
        return requests.get(url).json()

    def get_png(self):
        url = self.__url + 'views/first.png'
        return requests.get(url).content

    def get_svg(self):
        url = self.__url + 'views/first.svg'
        return requests.get(url).content

    def get_pdf(self):
        url = self.__url + 'views/first.pdf'
        return requests.get(url).content

    def get_first_view(self, format='json'):
        """
        Get a first view model as dict
        :return:
        """
        url = self.__url + 'views/first'
        return requests.get(url).json()

    def get_view(self, view_id, format='json'):
        if format is 'json':
            url = self.__url + 'views/' + str(view_id)
            return requests.get(url).json()
        elif format is 'view':
            return self.__get_view_object(view_id)
        else:
            return None

    def __get_view_object(self, view_id):
        """
        Create a new CyNetworkView object for the given ID.

        :param view_id:
        :return:
        """
        view = CyNetworkView(self, view_id)
        return view

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__id == other.__id
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
