# -*- coding: utf-8 -*-

import requests
from .network_client import NetworkClient
from .style_client import StyleClient
from .algorithm_client import LayoutClient
from .algorithm_client import EdgeBundlingClient
from .session_client import SessionClient

from . import PORT, IP, VERSION


class CyRestClient(object):

    def __init__(self, ip=IP, port=PORT, version=VERSION):
        self.__url = 'http://' + ip + ':' + str(port) + '/' + version + '/'

        self.network = NetworkClient(self.__url)
        self.style = StyleClient(self.__url)
        self.layout = LayoutClient(self.__url)
        self.edgebundling = EdgeBundlingClient(self.__url)
        self.session = SessionClient(self.__url)

    def status(self):
        try:
            response = requests.get(self.__url).json()
        except Exception as e:
            print('Could not get status from cyREST: ' + e)
        else:
            return response
