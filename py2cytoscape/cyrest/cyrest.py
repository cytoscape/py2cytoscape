from .base import *
from .commands import *
from .command import *
from .cybrowser import *
from .session import *
from .network import *
from .node import *
from .vizmap import *
from .diffusion import *
from .idmapper import *
from .edge import *
from .group import *
from .view import *
from .layout import *
from .table import *
from .cyndex2 import *
from .apply import *
from .apps import *
from .styles import *
from .ui import *
from .enrichmentmap import *
from .collections import *
from .networks import *

import json
import copy

class cyclient(object):
    """
    A CyREST client.

    :param host: CyREST host server address. default='localhost'
    :param port: CyREST port number. default=1234
    :param version: CyREST version. default='v1'

    returns: a cyclient object.
    """

    def __init__(self, host=HOST, port=PORT, version=VERSION):
        self.__url = 'http://' + host + ':' + str(port) + '/' + version + '/'
        #self.host=host
        #self.port=port
        #self.version=version
        self.commands=commands(self.__url)
        self.command=command(self.__url)
        self.cybrowser=cybrowser(self.__url)
        self.session=session(self.__url)
        self.network=network(self.__url)
        self.node=node(self.__url)
        self.vizmap=vizmap(self.__url)
        self.diffusion=diffusion(self.__url)
        self.edge=edge(self.__url)
        self.group=group(self.__url)
        self.view=view(self.__url)
        self.layout=layout(self.__url)
        self.table=table(self.__url)
        self.cyndex2=cyndex2(self.__url)
        self.apply=apply(self.__url)
        self.styles=styles(self.__url)
        self.ui=ui(self.__url)
        self.enrichmentmap=enrichmentmap(self.__url)
        self.collections=collections(self.__url)
        self.apps=apps(self.__url)
        self.networks=networks(self.__url)


    def status(self, verbose=False):
        """
        Checks the status of your CyREST server.
        """
        try:
            response=api(url=self.__url, method="GET", verbose=verbose)
        except Exception as e:
            print('Could not get status from CyREST:\n\n' + str(e))
        else:
            print('CyREST online!')

    def copy(self):
        """
        Creates a copy of the cyclient object.
        """
        return copy.deepcopy(self)

    def version(self, verbose=False):
        """
        Checks Cytoscape version
        """
        response=api(url=self.__url+"version",method="H", verbose=verbose)
        response=json.loads(response)
        for k in response.keys():
            print(k, response[k])

    def result(self, filetype="PNG", saveas=None, verbose=False):
        """
        Checks the current network. 
            
        :param filetype: file type eg.PDF, PNG, CYS, CYJS; default="PNG" 
        :param saveas: /path/to/non/tmp/file.prefix
        :param host: cytoscape host address, default=cytoscape_host
        :param port: cytoscape port, default=1234
        :returns: an image
        """
        from wand.image import Image as WImage
        from shutil import copyfile
        import tempfile
        from time import sleep
        import os

        sleep(1)
        u=self.__url 
        host=u.split("//")[1].split(":")[0]
        port=u.split(":")[2].split("/")[0]
        version=u.split(":")[2].split("/")[1]

        def MAKETMP():
            (fd, tmp_file) = tempfile.mkstemp()
            tmp_dir=tempfile.gettempdir()
            tmp_file=tmp_dir+"/"+tmp_file.split("/")[-1]
            return tmp_file
        
        outfile=MAKETMP()
        
        extensions={"PNG":".png","PDF":".pdf","CYS":".cys","CYJS":".cyjs"}
        ext=extensions[filetype]
        
        response=api("view","fit content",host=host,port=port, version=version, verbose=verbose)
        sleep(2)
        response=api("view", "export" , {"options":filetype,"outputFile":outfile, "view":"current"}, host=host,port=port,version=version,verbose=verbose)
        if host!='localhost':
            import paramiko
            print("Looking to ssh keys for remote access.")
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host)
            ftp_client=ssh.open_sftp()
            ftp_client.get(outfile+ext,outfile+ext)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("rm "+outfile+ext )
            
        img = WImage(filename=outfile+ext)
        if saveas:
            copyfile(outfile+ext,saveas)
        os.remove(outfile+ext)
        return img
        
