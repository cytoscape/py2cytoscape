from .base import *

class enrichmentmap(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/enrichmentmap'
        self.___url=url


    def getModelData(self, network, verbose=None):
        """
        

        :param network: Network name or SUID
        :param verbose: print more

        :returns: 200: successful operation
        """

        surl=self.___url
        sv=surl.split('/')[-1]
        surl=surl.rstrip(sv+'/')
        response=api(url=surl+'/enrichmentmap/model/'+str(network)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def getExpressionDataForNetwork(self, network, verbose=None):
        """
        

        :param network: Network name or SUID
        :param verbose: print more

        :returns: 200: successful operation
        """

        surl=self.___url
        sv=surl.split('/')[-1]
        surl=surl.rstrip(sv+'/')
        response=api(url=surl+'/enrichmentmap/expressions/'+str(network)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def getExpressionDataForNode(self, network, node, verbose=None):
        """
        

        :param network: Network name or SUID
        :param node: Node SUID
        :param verbose: print more

        :returns: 200: successful operation
        """

        surl=self.___url
        sv=surl.split('/')[-1]
        surl=surl.rstrip(sv+'/')
        response=api(url=surl+'/enrichmentmap/expressions/'+str(network)+'/'+str(node)+'', method="GET", verbose=verbose, parse_params=False)
        return response