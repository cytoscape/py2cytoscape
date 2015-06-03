import requests
from . import HEADERS, SUID_LIST


class LayoutClient(object):

    def __init__(self, url):
        self.__url = url + 'apply/layouts'

    def get_all(self):
        return requests.get(self.__url).json()

    def apply(self, name='force-directed', network=None):
        if network is None:
            raise ValueError('Target network is required')

        url = self.__url + '/' + name + '/' + str(network.get_id())
        requests.get(url)

    def create_discrete_mapping(self, column=None, visual_property=None, mapping=None):
        pass
