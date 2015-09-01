# -*- coding: utf-8 -*-
import json

import pandas as pd
import requests

from ..util import util_networkx as nx_util
from ..util import dataframe as df_util

from . import BASE_URL, HEADERS

BASE_URL_NETWORK = BASE_URL + 'networks'


class BaseView(object):

    def __init__(self, network_view=None, view=None, obj_type=None):
        if network_view is None:
            raise ValueError('Network view is required.')

        if view is None:
            raise ValueError('View is required.')
        else:
            model_id = network_view.get_model_id()
            view_id = network_view.get_id()
            object_id = view['SUID']
            self.url = BASE_URL_NETWORK + '/' + str(model_id) + \
                         '/views/' + str(view_id) +\
                         '/' + obj_type + '/' + str(object_id)
            self.view = self.__create(view['view'])
            self.__id = object_id

    def __create(self, view):
        view_map = {}

        for pair in view:
            key = pair['visualProperty']
            value = pair['value']
            view_map[key] = value

        return view_map

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
        print('----------- set called')
        requests.put(self.url, data=json.dumps(new_value), headers=HEADERS)

    def get_value(self, visual_property):
        print('----------- get called')
        res = requests.get(self.url + '/' + visual_property)
        return res.json()['value']