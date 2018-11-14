from .base import *

class apps(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/apps'
        self.___url=url

    def getAppList(self, verbose=None):
        """
        Returns installed Cytoscape Apps that have CyREST accessible Functions or Commands, as a list of App names.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'apps', method="H", verbose=verbose, parse_params=False)
        return response