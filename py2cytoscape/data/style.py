from . import BASE_URL, HEADERS
import requests
import json


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

    def __get_new_mapping(self, mapping_type, column=None, dataType='String', vp=None):
        if column is None or vp is None:
            raise ValueError('both column name and visual property are required.')

        new_maping = {
            'mappingType': mapping_type,
            'mappingColumn': column,
            'mappingColumnType': dataType,
            'visualProperty': vp
        }

        return new_maping

    def create_discrete_mapping(self, column=None, dataType='String', vp=None, mappings=None):
        self.__call_create_mapping(
            self.__get_discrete(column=column, dataType=dataType, vp=vp, mappings=mappings))

    def create_continuous_mapping(self, column=None, dataType='String', vp=None, points=None):
        self.__call_create_mapping(
            self.__get_continuous(column=column, dataType=dataType, vp=vp, points=points))

    def create_passthrough_mapping(self, column=None, dataType='String', vp=None):
        self.__call_create_mapping(
            self.__get_passthrough(column=column, dataType=dataType, vp=vp))

    def __call_create_mapping(self, mapping):
        url = self.__url + 'mappings'
        requests.post(url, data=json.dumps([mapping]), headers=HEADERS)

    def __get_passthrough(self, column=None, dataType='String', vp=None):
        return self.__get_new_mapping('passthrough', column=column, dataType=dataType, vp=vp)

    def __get_discrete(self, column=None, dataType='String', vp=None, mappings=None):
        new_mapping = self.__get_new_mapping('discrete', column=column, dataType=dataType, vp=vp)
        if mappings is None:
            raise ValueError('key-value pair object (mappings) is required.')
        body = [{'key': key, 'value': mappings[key]} for key in mappings.keys()]
        new_mapping['map'] = body
        return new_mapping

    def __get_continuous(self, column=None, dataType='String', vp=None, points=None):
        if points is None:
            raise ValueError('key-value pair object (mappings) is required.')
        new_mapping = self.__get_new_mapping('continuous', column=column, dataType=dataType, vp=vp)
        new_mapping['points'] = points
        return new_mapping

    def get_default(self, vp=None):
        pass

    def get_defaults(self):
        pass

    def update_defaults(self, key_value_pair):
        body = []
        for key in key_value_pair:
            entry = {
                'visualProperty': key,
                'value': key_value_pair[key]
            }
            body.append(entry)

        url = self.__url + 'defaults'
        requests.put(url, data=json.dumps(body), headers=HEADERS)

