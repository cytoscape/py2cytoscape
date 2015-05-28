# -*- coding: utf-8 -*-

import requests
from network_client import NetworkClient

from . import PORT, IP, VERSION


class CyRestClient(object):

    def __init__(self, ip=IP, port=PORT, version=VERSION):
        self.__url = 'http://' + ip + ':' + str(port) + '/' + version + '/'
        self.network = NetworkClient(self.__url)

    def status(self):
        try:
            response = requests.get(self.__url).json()
        except Exception as e:
            print('Could not get status from cyREST: ' + e)
        else:
            return response
