from .base import *

class commands(object):
    """
    cytoscape commands as shown in CyREST's swagger documentation for 'Commands'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands'

    def list(self):
        """
        List all available command namespaces.
        """
        response=api(url=self.__url,method="HTML")

    def namespace(self,namespace):
        """
        List all available commands in a namespace.

        :param namespace: a namespace as listed in rest.cyclient.commands.list().
        """
        response=api(url=self.__url+"/"+namespace,method="HTML")

    def command(self, namespace, command):
        """
        Execute a command or list its arguments.

        :param namespace: a namespace as listed in rest.cyclient.commands.list().
        :param command: a commands as listed in rest.cyclient.commands.namespace(<namespace>).
        """
        response=api(url=self.__url+"/"+namespace+"/"+command,method="HTML")
