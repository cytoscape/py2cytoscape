from .base import *

class command(object):
    """
    cytoscape command as shown in CyREST's swagger documentation for 'Command'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/command'

    def echo(self, variableName, verbose=False):
        """
        The echo command will display the value of the variable specified by the
        variableName argument, or all variables if variableName is not provided.

        :param variableName: The name of the variable or '*' to display the value of all variables.
        :param verbose: print more
        """
        PARAMS={"variableName":variableName}
        response=api(url=self.__url+"/echo", PARAMS=PARAMS, verbose=verbose)
        return response

    def open_dialog(self, verbose=False):
        """
        The command line dialog provides a field to enter commands and view
        results. It also provides the help command to display namespaces,
        commands, and arguments.

        :param verbose: print more
        """
        response=api(url=self.__url+"/open dialog", verbose=verbose)
        return response


    def pause(self, message=None, verbose=False):
        """
        The pause command displays a dialog with the text provided in the
        message argument and waits for the user to click OK

        :param message: a message to display. default=None
        :param verbose: print more
        """

        PARAMS=set_param(["message"],[message])
        response=api(url=self.__url+"/pause", PARAMS=PARAMS, verbose=verbose)
        return response

    
    def quit(self,verbose=False):
        """
        This command causes Cytoscape to exit. It is typically used at the end
        of a script file.

        :param verbose: print more
        """
        response=api(url=self.__url+"/quit", verbose=verbose)
        return response

    def run(self,script_file,args=None,verbose=False):
        """
        The run command will execute a command script from the file pointed to
        by the file argument, which should contain Cytoscape commands, one per
        line. Arguments to the script are provided by the args argument.

        :param script_file: file to run
        :param args: enter the script arguments as key:value pairs separated by
                        commas. eg. "arg1:value1,arg2:value2"
        :param verbose: print more
        """

        PARAMS=set_param(["file","args"],[script_file,args])
        response=api(url=self.__url+"/run", PARAMS=PARAMS, verbose=verbose)
        return response

    def sleep(self,duration,verbose=False):
        """
        The sleep command will pause processing for a period of time as specified
        by duration seconds. It is typically used as part of a command script.

        :param duration: enter the time in seconds to sleep
        :param verbose: print more
        """
        PARAMS={"duration":str(duration)}
        response=api(url=self.__url+"/sleep", PARAMS=PARAMS, verbose=verbose)
        return response

    