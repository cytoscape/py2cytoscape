# -*- coding: utf-8 -*-
import json
import requests

from . import BASE_URL, HEADERS

BASE_URL_NETWORK = BASE_URL + 'networks'


class BaseView(object):
    """
    Base view class to directly access node/edge view properties.
    """

    def __init__(self, network_view=None, obj_id=None, obj_type=None):
        if network_view is None:
            raise ValueError('Network view is required.')

        if obj_type is None:
            raise ValueError('Object type is required.')

        if obj_id is None:
            raise ValueError('Object SUID is required.')
        else:
            model_id = network_view.get_model_id()
            view_id = network_view.get_id()
            self.url = BASE_URL_NETWORK + '/' + str(model_id) + \
                       '/views/' + str(view_id) + \
                       '/' + obj_type + '/' + str(obj_id)
            self.__id = obj_id

    def get_id(self):
        """Get SUID of the object

        Note that this is node/edge SUID, NOT node view/edge view SUID.

        :return: SUID as integer
        """
        return self.__id

    def set_value(self, visual_property, value):
        """Set a single Visual Property Value

        :param visual_property: Visual Property ID
        :param value: New value for the VP
        :return: None
        """
        if visual_property is None or value is None:
            raise ValueError('Both VP and value are required.')

        new_value = [
            {
                'visualProperty': visual_property,
                "value": value
            }
        ]
        requests.put(self.url, data=json.dumps(new_value), headers=HEADERS)

    def set_values(self, values):
        """
        Set multiple Visual properties at once.

        :param values:
        :return:
        """
        if values is None:
            raise ValueError('Values are required.')

        new_values = []
        for vp in values.keys():
            new_val = {
                'visualProperty': vp,
                'value': values[vp]
            }
            new_values.append(new_val)

        requests.put(self.url, data=json.dumps(new_values), headers=HEADERS)

    def get_value(self, visual_property):
        """Get a value for the Visual Property

        :param visual_property:
        :return:
        """
        res = requests.get(self.url + '/' + visual_property)
        return res.json()['value']

    def get_values(self):
        """Get all visual property values for the object

        :return: dictionary of values (VP ID - value)
        """

        results = requests.get(self.url).json()
        values = {}
        for entry in results:
            values[entry['visualProperty']] = entry['value']
        return values
