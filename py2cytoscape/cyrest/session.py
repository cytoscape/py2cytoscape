from .base import *

class session(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation for 'session'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/session'

    def new(self, verbose=False):
        """
        Destroys the current session and creates a new, empty one.

        :param wid: Window ID
        :param verbose: print more
        """

        response=api(url=self.__url+"/new", verbose=verbose)
        return response

    
    def open(self, session_file=None,session_url=None, verbose=False):
        """
        Opens a session from a local file or URL.

        :param session_file: The path to the session file (.cys) to be loaded.
        :param session_url: A URL that provides a session file.
        :param verbose: print more
        """

        PARAMS=set_param(["file", "url"],[session_file, session_url])
        response=api(url=self.__url+"/open", PARAMS=PARAMS, verbose=verbose)
        return response

    
    def save(self, session_file, verbose=False):
        """
        Saves the current session to an existing file, which will be replaced.
        If this is a new session that has not been saved yet, use 'save as'
        instead.

        :param session_file: The path to the file where the current session
        must be saved to.
        :param verbose: print more
        """

        PARAMS={"file":session_file}

        response=api(url=self.__url+"/save", PARAMS=PARAMS, verbose=verbose)
        return response

    
    def save_as(self, session_file, verbose=False):
        """
        Saves the current session as a new file.

        :param session_file: The path to the file where the current session
        must be saved to.
        :param verbose: print more
        """

        PARAMS={"file":session_file}

        response=api(url=self.__url+"/save as", PARAMS=PARAMS, verbose=verbose)
        return response

    