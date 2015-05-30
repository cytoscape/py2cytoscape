# -*- coding: utf-8 -*-

import enum
import requests
import json

from . import HEADERS, SUID_LIST


class StyleClient(object):

    def __init__(self, url):
        self.__url = url + 'styles'

    def create(self, name=None):
        if name is None:
            raise ValueError('Name is required.')

        style = {
            'title': name,
            'defaults': [],
            'mappings': []
        }
        requests.post(self.__url, data=json.dumps(style), headers=HEADERS)

    def create_discrete_mapping(self, column=None, visual_property=None, mapping=None):
        pass

    def create_continuous_mapping(self):
        pass

    def create_passthrough_mapping(self):
        pass

    def update_defaults(self):
        pass


