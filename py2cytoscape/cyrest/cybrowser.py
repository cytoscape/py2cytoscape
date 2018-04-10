from .base import *

class cybrowser(object):
    """
    cytoscape cybrowser interface as shown in CyREST's swagger documentation for 'cybrowser'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/cybrowser'

    def dialog(self=None, wid=None, text=None, title=None, url=None, debug=False, verbose=False):
        """
        Launch and HTML browser in a separate window.

        :param wid: Window ID
        :param text: HTML text
        :param title: Window Title
        :param url: URL
        :param debug: Show debug tools. boolean
        :param verbose: print more
        """

        PARAMS=set_param(["id","text","title","url","debug"],[wid,text,title,url,debug])
        response=api(url=self.__url+"/dialog?",PARAMS=PARAMS, method="GET", verbose=verbose)
        return response

    def hide(self, wid, verbose=False):
        """
        Hide and HTML browser in the Results Panel.

        :param wid: Window ID
        :param verbose: print more
        """

        PARAMS={"id":wid}

        response=api(url=self.__url+"/hide?",PARAMS=PARAMS, method="GET", verbose=verbose)
        return response

    def show(self, wid=None, text=None, title=None, url=None, verbose=False):
        """
        Launch an HTML browser in the Results Panel.

        :param wid: Window ID
        :param text: HTML text
        :param title: Window Title
        :param url: URL
        :param verbose: print more
        """

        PARAMS={}
        for p,v in zip(["id","text","title","url"],[wid,text,title,url]):
            if v:
                PARAMS[p]=v

        response=api(url=self.__url+"/show?",PARAMS=PARAMS, method="GET", verbose=verbose)
        return response
 
    def version(self, verbose=False):
        """
        Display the CyBrowser version.

        :param verbose: print more
        """
        response=api(url=self.__url+"/version",method="HTML", verbose=verbose)
        return response

    