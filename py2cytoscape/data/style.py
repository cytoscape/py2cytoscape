from . import BASE_URL, HEADERS
import requests
import json
import pandas as pd


class Style(object):
    def __init__(self, name):
        # Validate required argument
        if name is None:
            raise ValueError("Style name is required.")
        else:
            self.__name = name

        self.__url = BASE_URL + 'styles/' + str(name) + '/'

    def get_name(self):
        """
        Get immutable name of this Visual Style.

        :return: Style name as string
        """
        return self.__name

    def __get_new_mapping(self, mapping_type, column=None, col_type='String',
                          vp=None):
        if column is None or vp is None:
            raise ValueError('both column name and visual property are required.')

        new_maping = {
            'mappingType': mapping_type,
            'mappingColumn': column,
            'mappingColumnType': col_type,
            'visualProperty': vp
        }

        return new_maping

    def create_discrete_mapping(self, column=None, col_type='String',
                                vp=None, mappings=None):
        self.__call_create_mapping(
            self.__get_discrete(column=column, col_type=col_type, vp=vp,
                                mappings=mappings))

    def create_continuous_mapping(self, column=None, col_type='String',
                                  vp=None, points=None):
        self.__call_create_mapping(
            self.__get_continuous(column=column, col_type=col_type, vp=vp,
                                  points=points))

    def create_passthrough_mapping(self, column=None, col_type='String',
                                   vp=None):
        self.__call_create_mapping(
            self.__get_passthrough(column=column, col_type=col_type, vp=vp))

    def __call_create_mapping(self, mapping):
        url = self.__url + 'mappings'
        requests.post(url, data=json.dumps([mapping]), headers=HEADERS)

    def __get_passthrough(self, column=None, col_type='String', vp=None):
        return self.__get_new_mapping('passthrough', column=column,
                                      col_type=col_type, vp=vp)

    def __get_discrete(self, column=None, col_type='String', vp=None,
                       mappings=None):
        new_mapping = self.__get_new_mapping('discrete', column=column,
                                             col_type=col_type, vp=vp)
        if mappings is None:
            raise ValueError('key-value pair object (mappings) is required.')
        body = [{'key': key, 'value': mappings[key]} for key in mappings.keys()]
        new_mapping['map'] = body
        return new_mapping

    def __get_continuous(self, column=None, col_type='String', vp=None,
                         points=None):
        if points is None:
            raise ValueError('key-value pair object (mappings) is required.')
        new_mapping = self.__get_new_mapping('continuous', column=column,
                                             col_type=col_type, vp=vp)
        new_mapping['points'] = points
        return new_mapping

    def get_mapping(self, vp=None):
        if vp is None:
            raise ValueError('Visual Property ID is required.')

        url = self.__url + 'mappings/' + vp
        return requests.get(url).json()

    def get_mappings(self):
        url = self.__url + 'mappings'
        return requests.get(url).json()

    def get_default(self, vp=None):
        if vp is None:
            raise ValueError('Visual Property ID is required.')

        url = self.__url + 'defaults/' + vp
        key_value_pair = requests.get(url).content
        print(key_value_pair)
        key2 = requests.get(url).json()
        key_value_pair = key2
        return pd.Series({key_value_pair['visualProperty']: key_value_pair[
            'value']})

    def get_defaults(self):
        url = self.__url + 'defaults'
        result = requests.get(url).json()['defaults']
        vals = {entry['visualProperty']: entry['value'] for entry in result}
        return pd.Series(vals)

    def update_defaults(self, prop_value_dict):
        """
        Updates the value of one or more visual properties.

        :param prop_value_dict: Dictionary containing, for each visual property,
            the new value to use.
        """

        body = []
        for key in prop_value_dict:
            entry = {
                'visualProperty': key,
                'value': prop_value_dict[key]
            }
            body.append(entry)

        url = self.__url + 'defaults'
        requests.put(url, data=json.dumps(body), headers=HEADERS)

    # Delete Methods

    def delete_mapping(self, vp=None):
        if vp is None:
            return

        url = self.__url + 'mappings/' + vp
        requests.delete(url)

    def delete_mappings(self):
        url = self.__url + 'mappings'
        requests.delete(url)


class StyleUtil(object):
    def create_point(value, lesser, equal, greater):
        return [
            {
                'value': str(value),
                'lesser': lesser,
                'equal': equal,
                'greater': greater
            }
        ]

    def create_2_color_gradient(min=0, max=10, colors=('red', 'green')):
        point_1 = StyleUtil.create_point(min, colors[0], colors[0], colors[0])
        point_2 = StyleUtil.create_point(max, colors[1], colors[1], colors[1])
        return point_1 + point_2

    def create_3_color_gradient(min=-5, mid=0, max=5, colors=('blue', 'white', 'red')):
        # can be updated to use StyleUtil.create_point like in create_point
        points = [
            {
                'value': str(min),
                'lesser': colors[0],
                'equal': colors[0],
                'greater': colors[0],
            },
            {
                'value': str(mid),
                'lesser': colors[1],
                'equal': colors[1],
                'greater': colors[1],
            },
            {
                'value': str(max),
                'lesser': colors[2],
                'equal': colors[2],
                'greater': colors[2]
            }
        ]

        return points

    def create_slope(min=0, max=10, values=(1, 10)):
        point_1 = StyleUtil.create_point(min, values[0], values[0], values[0])
        point_2 = StyleUtil.create_point(max, values[1], values[1], values[1])
        return point_1 + point_2
