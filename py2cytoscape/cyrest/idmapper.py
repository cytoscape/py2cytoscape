from .base import *

class idmapper(object):
    """
    cytoscape network interface as shown in CyREST's swagger documentation for 'idmapper'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/idmapper'

    def map_column(self, only_use_one=None, source_column=None, species=None, target_selection= None, verbose=False):
        """
        Uses the BridgeDB service to look up analogous identifiers from a wide
        selection of other databases

        :param only_use_one (string, optional): When multiple identifiers can be
            mapped from a single term, this forces a singular result
        :param source_column (string): Specifies the column nmae where the
            source identifiers are located = ['']
        :param source_selection (string): Specifies the database describing
            the existing identifiers = ['']
        :param species (string, optional): The combined common or latin name of
            the species to which the identifiers apply = ['Human (Homo sapiens)',
            'Mouse (Mus musculus)', 'Rat (Rattus norvegicus)', 'Frog (Xenopus tropicalis)',
            'Zebra fish (Danio rerio)', 'Fruit fly (Drosophila melanogaster)',
            'Mosquito (Anopheles gambiae)', 'Arabidopsis thaliana (Arabidopsis thaliana)',
            'Yeast (Saccharomyces cerevisiae)', 'E. coli (Escherichia coli)',
            'Tuberculosis (Mycobacterium tuberculosis)', 'Worm (Caenorhabditis elegans)']
        :param target_selection (string): Specifies the database identifiers to be looked up = ['']
        :param verbose: print more

        :returns: eg. { "new column": "SGD " }
        """
        PARAMS=set_param(["only_use_one","source_column","species","target_selection"],[only_use_one,source_column,species,target_selection])
        response=api(url=self.__url+"/map column", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

