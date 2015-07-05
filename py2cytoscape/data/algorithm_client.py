import requests


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

    def bundle_edge(self, network=None):
        if network is None:
            raise ValueError('Target network is required')

        url = self.__url + '/edgebundling/' + str(network.get_id())
        requests.get(url)


class EdgeBundlingClient(object):

    def __init__(self, url):
        self.__url = url + 'apply/edgebundling'


    def apply(self, network=None):
        if network is None:
            raise ValueError('Target network is required')

        url = self.__url + '/' + str(network.get_id())
        requests.get(url)
