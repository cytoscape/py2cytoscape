# -*- coding: utf-8 -*-
import json

import pandas as pd
import requests

from ..util import util_networkx as nx_util
from ..util import dataframe as df_util

from . import BASE_URL, HEADERS

BASE_URL_NETWORK = BASE_URL + 'networks'


class BaseView(object):
    """
    Base view class to directly access node/edge views.
    """

    def __init__(self, network_view=None, obj_id=None, obj_type=None):
        if network_view is None:
            raise ValueError('Network view is required.')

        if obj_id is None:
            raise ValueError('Object SUID is required.')
        else:
            model_id = network_view.get_model_id()
            view_id = network_view.get_id()
            self.url = BASE_URL_NETWORK + '/' + str(model_id) + \
                         '/views/' + str(view_id) +\
                         '/' + obj_type + '/' + str(obj_id)
            self.__id = obj_id

    # def __create(self, view):
    #     view_map = {}
    #
    #     for pair in view:
    #         key = pair['visualProperty']
    #         value = pair['value']
    #         view_map[key] = value
    #
    #     return view_map

    def get_id(self):
        """
        Get SUID of the object

        :return: SUID as integer
        """
        return self.__id

    def set_value(self, visual_property, value):
        new_value = [
            {
                'visualProperty': visual_property,
                "value": value
            }
        ]
        requests.put(self.url, data=json.dumps(new_value), headers=HEADERS)

    def set_values(self, values):
        new_values = []
        for vp in values.keys():
            new_val = {
                'visualProperty': vp,
                'value': values[vp]
            }
            new_values.append(new_val)

        requests.put(self.url, data=json.dumps(new_values), headers=HEADERS)

    def get_value(self, visual_property):
        res = requests.get(self.url + '/' + visual_property)
        return res.json()['value']

    def get_values(self):
        res = requests.get(self.url)
        print(self.url)
        results = res.json()
        values = {}
        for entry in results:
            values[entry['visualProperty']] = entry['value']
        return values