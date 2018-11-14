from .base import *

class cyndex2(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/cyndex2'
        self.___url=url


    def updateNetworkInNdex(self, suid, body, verbose=None):
        """
        Update an NDEx network.

        :param suid: Cytoscape Collection/Subnetwork SUID
        :param body: Properties required to update a network record in NDEx.
        :param verbose: print more

        :returns: 200: successful operation; 404: Network does not exist
        """

        surl=self.___url
        sv=surl.split('/')[-1]
        surl=surl.rstrip(sv+'/')
        response=api(url=surl+'/cyndex2/'+sv+'/networks/'+str(suid)+'', method="PUT", body=body, verbose=verbose)
        return response


    def saveNetworkToNdex(self, suid, body, verbose=None):
        """
        Save a network/collection to NDEx

        :param suid: Cytoscape Collection/Subnetwork SUID
        :param body: Properties required to save network to NDEx.
        :param verbose: print more

        :returns: 200: successful operation; 404: Network does not exist
        """

        surl=self.___url
        sv=surl.split('/')[-1]
        surl=surl.rstrip(sv+'/')
        PARAMS=set_param(['suid','body'],[suid,body])
        response=api(url=surl+'/cyndex2/'+sv+'/networks/'+str(suid)+'', PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def getNetworkSummary(self, suid, verbose=None):
        """
        Returns summary of collection containing the specified network.

        :param suid: Cytoscape Collection/Subnetwork SUID
        :param verbose: print more

        :returns: 200: successful operation
        """

        surl=self.___url
        sv=surl.split('/')[-1]
        surl=surl.rstrip(sv+'/')
        response=api(url=surl+'/cyndex2/'+sv+'/networks/'+str(suid)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def getAppInfo(self, verbose=None):
        """
        App version and other basic information will be provided.

        :param verbose: print more

        :returns: 200: successful operation
        """

        surl=self.___url
        sv=surl.split('/')[-1]
        surl=surl.rstrip(sv+'/')
        response=api(url=surl+'/cyndex2/v1', method="GET", verbose=verbose, parse_params=False)
        return response


    def updateCurrentNetworkInNdex(self, body, verbose=None):
        """
        Update current network's record in NDEx

        :param body: Properties required to update a network record in NDEx.
        :param verbose: print more

        :returns: 200: successful operation; 404: Network does not exist
        """

        surl=self.___url
        sv=surl.split('/')[-1]
        surl=surl.rstrip(sv+'/')
        response=api(url=surl+'/cyndex2/'+sv+'/networks/current', method="PUT", body=body, verbose=verbose)
        return response


    def saveCurrentNetworkToNdex(self, body, verbose=None):
        """
        Save current network/collection to NDEx

        :param body: Properties required to save current network to NDEx.
        :param verbose: print more

        :returns: 200: successful operation; 404: Current network does not exist
        """

        surl=self.___url
        sv=surl.split('/')[-1]
        surl=surl.rstrip(sv+'/')
        PARAMS=set_param(['body'],[body])
        response=api(url=surl+'/cyndex2/'+sv+'/networks/current', PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def getCurrentNetworkSummary(self, verbose=None):
        """
        Returns summary of collection contains current network.

        :param verbose: print more

        :returns: 200: successful operation
        """

        surl=self.___url
        sv=surl.split('/')[-1]
        surl=surl.rstrip(sv+'/')
        response=api(url=surl+'/cyndex2/'+sv+'/networks/current', method="GET", verbose=verbose, parse_params=False)
        return response


    def createNetworkFromNdex(self, body, verbose=None):
        """
        Import network(s) from NDEx.

        :param body: Properties required to import network from NDEx.
        :param verbose: print more

        :returns: 200: successful operation; 404: Network does not exist
        """

        surl=self.___url
        sv=surl.split('/')[-1]
        surl=surl.rstrip(sv+'/')
        PARAMS=set_param(['body'],[body])
        response=api(url=surl+'/cyndex2/'+sv+'/networks', PARAMS=PARAMS, method="POST", verbose=verbose)
        return response