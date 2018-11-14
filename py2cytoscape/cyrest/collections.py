from .base import *

class collections(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/collections'
        self.___url=url


    def getCollectionCount(self, verbose=None):
        """
        Returns a count of all root networks.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'collections/count', method="H", verbose=verbose, parse_params=False)
        return response