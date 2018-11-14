from .base import *

class session(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation for 'session'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/session'
        self.___url=url

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

    def createSessionFile(self, file, verbose=None):
        """
        Saves the current session to a file. If successful, the session file location will be returned.

        :param file: Session file location as an absolute path
        :param verbose: print more

        :returns: 200: successful operation
        """

        PARAMS=set_param(['file'],[file])
        response=api(url=self.___url+'session', PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def deleteSession(self, verbose=None):
        """
        This deletes the current session and initializes a new one. A message is returned to indicate the success of the deletion.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'session', method="DELETE", verbose=verbose)
        return response


    def getSessionFromFile(self, file, verbose=None):
        """
        Loads a session from a local file and returns the session file name

        :param file: Session file location as an absolute path
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'session', PARAMS={'file':file}, method="GET", verbose=verbose, parse_params=False)
        return response


    def getSessionName(self, verbose=None):
        """
        Returns the file name for the current Cytoscape session.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.___url+'session/name', method="GET", verbose=verbose, parse_params=False)
        return response

    def runGarbageCollection(self, verbose=None):
        """
        Manually call Java's System.gc() to free up unused memory. This process happens automatically, but may be useful to call explicitly for testing or evaluation purposes.

        :param verbose: print more

        :returns: 204: Successful Garbage Collection
        """

        response=api(url=self.___url+'gc', method="GET", verbose=verbose, parse_params=False)
        return response