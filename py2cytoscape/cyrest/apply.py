from .base import *

class apply(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation for 'layout'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/apply'
        self.___url=url


    def applyLayout(self, algorithmName, networkId, column, verbose=None):
        """
        Applies the Layout specified by the `algorithmName` parameter to the Network specified by the `networkId` parameter. If the Layout is has an option to use a Column, it can be specified by the `column` parameter.

        :param algorithmName: Name of layout algorithm
        :param networkId: SUID of the Network
        :param column: Name of the Column to be used by the Layout -- Not required, can be None
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'apply/layouts/'+str(algorithmName)+'/'+str(networkId)+'', PARAMS={'column':column}, method="GET", verbose=verbose, parse_params=False)
        return response


    def fitContent(self, networkId, verbose=None):
        """
        Fit the first available Network View for the Network specified by the `networkId` parameter to the current window.

        :param networkId: SUID of the Network
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'apply/fit/'+str(networkId)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def getStyleNames(self, verbose=None):
        """
        Returns a list of all Visual Style names. Style names may not be unique.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'apply/styles', method="H", verbose=verbose, parse_params=False)
        return response


    def copyCurrentLayout(self, sourceViewSUID, targetViewSUID, body, verbose=None):
        """
        Copy one network view layout onto another, setting the node location and view scale to match. This makes visually comparing networks simple.

        :param sourceViewSUID: Source network view SUID (or "current")
        :param targetViewSUID: Target network view SUID (or "current")
        :param body: Clone the specified network view layout onto another network view -- Not required, can be None
        :param verbose: print more

        :returns: 200: successful operation; 404: Network View does not exist
        """

        response=api(url=self.___url+'apply/layouts/copycat/'+str(sourceViewSUID)+'/'+str(targetViewSUID)+'', method="PUT", body=body, verbose=verbose)
        return response


    def bundleEdge(self, networkId, verbose=None):
        """
        Apply edge bundling to the Network specified by the `networkId` parameter. Edge bundling is executed with default parameters; at present, optional parameters are not supported.

        :param networkId: SUID of the Network
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'apply/edgebundling/'+str(networkId)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def applyStyle(self, styleName, networkId, verbose=None):
        """
        Applies the Visual Style specified by the `styleName` parameter to the network specified by the `networkId` parameter.

        :param styleName: Name of the Visual Style
        :param networkId: SUID of the Network
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'apply/styles/'+str(styleName)+'/'+str(networkId)+'', method="GET", verbose=verbose, parse_params=False)
        return response


    def updateLayoutParameters(self, algorithmName, body, verbose=None):
        """
        Updates the Layout parameters for the Layout algorithm specified by the `algorithmName` parameter.

        :param algorithmName: Name of the layout algorithm
        :param body: A list of Layout Parameters with Values.
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.___url+'apply/layouts/'+str(algorithmName)+'/parameters', method="PUT", body=body, verbose=verbose)
        return response


    def getLayoutParameters(self, algorithmName, verbose=None):
        """
        Returns all editable parameters for the Layout algorithm specified by the `algorithmName` parameter.

        :param algorithmName: Name of the Layout algorithm
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'apply/layouts/'+str(algorithmName)+'/parameters', method="H", verbose=verbose, parse_params=False)
        return response
        

    def getLayout(self, algorithmName, verbose=None):
        """
        Returns all the details, including names, parameters, and compatible column types for the Layout algorithm specified by the `algorithmName` parameter.

        :param algorithmName: Name of the Layout algorithm
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'apply/layouts/'+str(algorithmName)+'', method="H", verbose=verbose, parse_params=False)
        return response


    def layoutList(self, verbose=None):
        """
        Returns all available layouts as a list of layout names.
        
        <h3>Important Note</h3>
        
        This <strong>does not include yFiles layout algorithms</strong>, due to license issues.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'apply/layouts', method="H", verbose=verbose, parse_params=False)
        return response


    def getCompatibleColumnDataTypes(self, algorithmName, verbose=None):
        """
        Returns a list of all compatible column data types for the Layout algorithm specified by the `algorithmName` parameter.

        :param algorithmName: Name of layout algorithm
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'apply/layouts/'+str(algorithmName)+'/columntypes', method="H", verbose=verbose, parse_params=False)
        return response

