from .base import *

class vizmap(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation for 'vizmap'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/vizmap'

    def apply(self, styles=None, verbose=False):
        """
        Applies the specified style to the selected views and returns the
        SUIDs of the affected views.

        :param styles (string): Name of Style to be applied to the selected
            views. = ['Directed', 'BioPAX_SIF', 'Bridging Reads Histogram:unique_0',
            'PSIMI 25 Style', 'Coverage Histogram:best&unique', 'Minimal',
            'Bridging Reads Histogram:best&unique_0', 'Coverage Histogram_0',
            'Big Labels', 'No Histogram:best&unique_0', 'Bridging Reads Histogram:best',
            'No Histogram_0', 'No Histogram:best&unique', 'Bridging Reads Histogram_0',
            'Ripple', 'Coverage Histogram:unique_0', 'Nested Network Style',
            'Coverage Histogram:best', 'Coverage Histogram:best&unique_0',
            'default black', 'No Histogram:best_0', 'No Histogram:unique',
            'No Histogram:unique_0', 'Solid', 'Bridging Reads Histogram:unique',
            'No Histogram:best', 'Coverage Histogram', 'BioPAX', 'Bridging Reads Histogram',
            'Coverage Histogram:best_0', 'Sample1', 'Universe', 'Bridging Reads Histogram:best_0',
            'Coverage Histogram:unique', 'Bridging Reads Histogram:best&unique',
            'No Histogram', 'default']
        :param verbose: print more

        """

        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["styles"],[styles])
        response=api(url=self.__url+"/apply", PARAMS=PARAMS, method="POST", verbose=verbose)
        if response:
            return response


    def export(self, options=None, OutputFile=None, styles=None, verbose=False):
        """
        Exports the specified styles to a Cytoscape vizmap (XML) or a Cytoscape.js
        (JSON) file and returns the path to the saved file.

        :param options (string, optional): The format of the output file. =
            ['Style XML (*.xml)', 'Style for cytoscape.js (*.json)']
        :param OutputFile (string): The path name of the file where the styles
            must be saved to.
        :param styles (string, optional): The styles to be exported. If no styles
            are specified, only the current one is exported. = ['Big Labels',
            'BioPAX', 'BioPAX_SIF', 'Bridging Reads Histogram', 'Bridging Reads
            Histogram_0', 'Bridging Reads Histogram:best', 'Bridging Reads Histogram:best_0',
            'Bridging Reads Histogram:best&unique', 'Bridging Reads Histogram:best&unique_0',
            'Bridging Reads Histogram:unique', 'Bridging Reads Histogram:unique_0',
            'Coverage Histogram', 'Coverage Histogram_0', 'Coverage Histogram:best',
            'Coverage Histogram:best_0', 'Coverage Histogram:best&unique',
            'Coverage Histogram:best&unique_0', 'Coverage Histogram:unique', '
            Coverage Histogram:unique_0', 'default', 'default black', 'Directed',
            'Minimal', 'Nested Network Style', 'No Histogram', 'No Histogram_0',
            'No Histogram:best', 'No Histogram:best_0', 'No Histogram:best&unique',
            'No Histogram:best&unique_0', 'No Histogram:unique', 'No Histogram:unique_0',
            'PSIMI 25 Style', 'Ripple', 'Sample1', 'Solid', 'Universe']
        :param verbose: print more

        """

        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["options","OutputFile", "styles"],[options,OutputFile,styles])
        response=api(url=self.__url+"/export", PARAMS=PARAMS, method="POST", verbose=verbose)
        if response:
            return response


    def load_file(self, afile=None, verbose=False):
        """
        Loads styles from a vizmap (XML or properties) file and returns the names of the loaded styles.

        :param afile (string): XML or properties file where one or more styles have been saved to.
        :param verbose: print more

        """

        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["afile"],[afile])
        response=api(url=self.__url+"/load file", PARAMS=PARAMS, method="POST", verbose=verbose)
        if response:
            return response
