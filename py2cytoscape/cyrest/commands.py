from .base import *

class commands(object):
    """
    cytoscape commands as shown in CyREST's swagger documentation for 'Commands'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands'

    def list_namespaces(self, verbose=False):
        """
        List all available command namespaces.
        """
        response=api(url=self.__url,method="HTML", verbose=verbose)
        return response

    def namespace(self, namespace, verbose=False):
        """
        List all available commands in a namespace.

        :param namespace: a namespace as listed in rest.cyclient.commands.list().
        :param verbose: print more
        """
        response=api(url=self.__url+"/"+namespace,method="HTML",verbose=verbose)
        return response

    def command(self, namespace, command, verbose=False):
        """
        List the arguments of a command.

        :param namespace: a namespace as listed in rest.cyclient.commands.list().
        :param command: a commands as listed in rest.cyclient.commands.namespace(<namespace>).
        :param verbose: print more
        """
        response=api(url=self.__url+"/"+namespace+"/"+command,method="HTML",verbose=verbose)
        return response

    