# -*- coding: utf-8 -*-

import requests
import json

from . import BASE_URL, HEADERS, SUID_LIST
from ..util import cytoscapejs as util

import pandas as pd


BASE_URL_NETWORK = BASE_URL + 'networks'
JSON = 'json'


class NetworkClient(object):

    @staticmethod
    def get_all(format=SUID_LIST):
        if format is SUID_LIST:
            result = requests.get(BASE_URL_NETWORK)
        elif format is JSON:
            result = requests.get(BASE_URL_NETWORK + '.json')
        else:
            return None

        return result.json()

    @staticmethod
    def get(id):
        return requests.get(BASE_URL_NETWORK + '/' + str(id) + '.json').json()

    @staticmethod
    def delete_all():
        requests.delete(BASE_URL_NETWORK)

    @staticmethod
    def delete(id):
        requests.delete(BASE_URL_NETWORK + '/' + str(id))

    @staticmethod
    def create(data=None):
        if data is None:
            res = requests.post(BASE_URL_NETWORK, data=json.dumps(
                util.get_empty_network()), headers=HEADERS)
        else:
            res = requests.post(BASE_URL_NETWORK, data=json.dumps(data),
                                headers=HEADERS)

        result = res.json()
        return result['networkSUID']

    @staticmethod
    def create_from_dataframe(self, df):
        pass
