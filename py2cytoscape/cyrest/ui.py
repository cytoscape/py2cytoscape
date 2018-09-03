from .base import *

class ui(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/ui'


    def updatePanelStatus(body, verbose=None):
        """
        Updates the status(es) of available CytoPanels.

        :param body: A list of CytoPanels with states.
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.url+'ui/panels', method="PUT", body=body, verbose=verbose)
        return response


    def getAllPanelStatus(verbose=None):
        """
        Returns all CytoPanels and their statuses.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'ui/panels', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def getDesktop(verbose=None):
        """
        Returns the status of the Desktop

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'ui', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def getPanelStatus(panelName, verbose=None):
        """
        Returns the status of the CytoPanel specified by the `panelName` parameter.

        :param panelName: Name of the CytoPanel
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'ui/panels/'+str(panelName)+'', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def updateLodState(verbose=None):
        """
        Switch between full graphics details <---> fast rendering mode.
        
        Returns a success message.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'ui/lod', method="PUT", verbose=verbose)
        return response

