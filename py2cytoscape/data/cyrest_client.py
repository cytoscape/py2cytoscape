# -*- coding: utf-8 -*-

import requests
from network import NetworkClient

from . import BASE_URL


class CyRestClient(object):

    def __init__(self):
        self.network = NetworkClient()

    def status(self):
        return requests.get(BASE_URL).json()
