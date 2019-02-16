from .base import *

class view(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation for 'view'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/view'

    def create(self, layout=None, network=None, verbose=False):
        """
        Creates a new view for the passed network and returns the SUID of the
            new view and the original network. If no networks are specified, it
            creates a view for the current network, if there is one.

        :param layout (string, optional): If true (default), the preferred layout
            will be applied to the new view. If false, no layout will be applied.
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        :returns: eg. 2123

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["layout","network"],[layout,network])
        response=api(url=self.__url+"/create", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def destroy(self, verbose=False):
        """
        Destroys all selected network views and returns their SUIDs. If no views
            are selected, this command does nothing.
        :param verbose: print more

        :returns: eg. [ 2155 ]
        """
        PARAMS={}
        response=api(url=self.__url+"/destroy", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def export(self, Height=None, options=None, outputFile=None, Resolution=None,\
        Units=None, Width=None, Zoom=None, view="current", verbose=False):
        """
        Exports the current view to a graphics file and returns the path to the
            saved file. PNG and JPEG formats have options for scaling, while other
            formats only have the option 'exportTextAsFont'. For the PDF format,
            exporting text as font does not work for two-byte characters such as
            Chinese or Japanese. To avoid corrupted texts in the exported PDF,
            please set false to 'exportTextAsFont' when exporting networks including
            those non-English characters.

        :param Height (string, optional): The height of the exported image. Valid
            only for bitmap formats, such as PNG and JPEG.
        :param options (string, optional): The format of the output file. =
            ['JPEG (*.jpeg, *.jpg)', 'PDF (*.pdf)', 'PNG (*.png)', 'PostScript (*.ps)',
             'SVG (*.svg)']
        :param OutputFile (string, optional): The path name of the file where
            the view must be saved to. By default, the view's title is used as
            the file name.
        :param Resolution (string, optional): The resolution of the exported
            image, in DPI. Valid only for bitmap formats, when the selected width
            and height 'units' is inches. The possible values are: 72 (default),
            100, 150, 300, 600. = ['72', '100', '150', '300', '600']
        :param Units (string, optional): The units for the 'width' and 'height'
            values. Valid only for bitmap formats, such as PNG and JPEG. The
            possible values are: pixels (default), inches. = ['pixels', 'inches']
        :param Width (string, optional): The width of the exported image. Valid
            only for bitmap formats, such as PNG and JPEG.
        :param Zoom (string, optional): The zoom value to proportionally scale
            the image. The default value is 100.0. Valid only for bitmap formats,
            such as PNG and JPEG
        :param verbose: print more

        :returns: path to the saved file
        """
        PARAMS=set_param(["Height","options","outputFile","Resolution",\
        "Units","Width","Zoom","view"],\
        [Height,options,outputFile,Resolution,Units,Width,Zoom,view ])
        response=api(url=self.__url+"/export", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def fit_content(self, verbose=False):
        """
        Zooms out the current view in order to display all of its elements.

        :param verbose: print more

        """
        PARAMS={}
        response=api(url=self.__url+"/fit content", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response 

    def fit_selected(self, verbose=False):
        """
        Changes the current view's zoom and viewport so the selected nodes and
            edges fit into the view area.

        :param verbose: print more

        """
        PARAMS={}
        response=api(url=self.__url+"/fit selected", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response
    
    def get_current(self, layout=None, network=None, verbose=False):
        """
        Returns the current view or null if there is none.

        :param verbose: print more

        :returns: current view or null if there is none
        """
        PARAMS={}
        response=api(url=self.__url+"/get_current", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def list(self, network=None, verbose=False):
        """
        Returns a list with the passed network's views or an empty list if
            there are no views. If a network is not specified, it assumes the
            current network.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        :returns: a list with the passed network's views or an empty list if there are no views

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network"],[network])
        response=api(url=self.__url+"/list", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def set_current(self, network=None, verbose=False):
        """
        Sets the current view, which can also be null.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network"],[network])
        response=api(url=self.__url+"/set current", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def update(self, network=None, verbose=False):
        """
        Sets the current view, which can also be null.

        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param verbose: print more

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network"],[network])
        response=api(url=self.__url+"/update", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response
