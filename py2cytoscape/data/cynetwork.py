import json
import pandas as pd
import requests

from . import BASE_URL, HEADERS

BASE_URL_NETWORK = BASE_URL + 'networks'
JSON = 'json'


class CyNetwork(object):

    def __init__(self, suid=None):
        # Validate required argument
        if pd.isnull(suid):
            raise ValueError("SUID is missing.")
        else:
            self.__id = suid

        self.__url = BASE_URL_NETWORK + '/' + str(self.__id) + '/'

    def get_id(self):
        return self.__id

    def get_nodes(self):
        result  = requests.get(self.__url + 'nodes')
        try:
            return result.json()
        except:
            return 'ERROR!!!!!!!!!!!'


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
        return edges

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

    def set_node_value(self, id, column, value):
        pass

    def set_node_values(self, column, values_tuple):
        pass

    def update_node_table(self, df=None, network_key_col='name', data_key_col='name'):
        return self.__update_table('node', df=df, network_key_col=network_key_col, data_key_col=data_key_col)

    def __update_table(self, type, df, network_key_col='name', data_key_col='name'):
        table = {
            'key': network_key_col,
 		    'dataKey': data_key_col
        }
        data = []
        col_names = df.columns.values
        for index, row in df.iterrows():
            entry = {}
            for col in col_names:
                value = row[col]
                if pd.isnull(value):
                    continue
                else:
                    entry[col] = value
            data.append(entry)

        table['data'] = data
        requests.put(self.__url + 'tables/default' + type,
                      data=json.dumps(table), headers=HEADERS)


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

    def __data_frame_to_table(self, df):
        """
        Convert Pandas DataFrame to POSTable table

        :param df:
        :return:
        """

        cytable = {}


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__id == other.__id
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)



class CyTable(object):
    def __init__(self, suid, type):
        self.__id = suid
