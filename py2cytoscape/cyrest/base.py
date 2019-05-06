import sys
import requests
import urllib.request as urllib2		
import json


from json import JSONDecodeError

HOST = 'localhost'
IP=HOST # temporary
PORT = 1234
VERSION = 'v1'
BASE_URL = 'http://' + HOST + ':' + str(PORT) + '/' + VERSION + '/'
HEADERS = {'Content-Type': 'application/json'}
VERBOSE=False


SUID_LIST = 'suid'

BASE_URL_NETWORK = BASE_URL + 'networks'

def set_param(parameters,values):
    PARAMS={}
    for p,v in zip(parameters,values):
        if v:
            PARAMS[p]=v
    return PARAMS

def check_network(cyrest_network,network=None,verbose=False):
    if network is None:
        try:
            network_name=cyrest_network.network_name
        except AttributeError:
            network_name='CURRENT'
    else:
        network_name=network
    if verbose:
        print("Working on '%s' network." %str(network_name) )
    return network_name

def checkresponse(r,verbose=False):
    status=r.status_code
    if 200 <= status < 300:
        if verbose:
            print("response status "+status)
            sys.stdout.flush()
        res=None
    else:
        print(r, r.status_code)
        sys.stdout.flush()
        res="error::"+str(r.status_code)
    return res

def handle_status_codes(x,verbose=False):
    if type(x) == str:
        if "error::" in x:
            res=int(x.lstrip("error::"))
        else:
            res=None
    else:
        res=None

    if res or verbose:
        if res:
            res=res
        else:
            res=x
    else:
        res=None

    if not res:
        if x:
            res=x

    return res


def api(namespace=None, command="", PARAMS={}, body=None, host=HOST, port=str(PORT), version=VERSION, method="POST", verbose=VERBOSE, url=None, parse_params=True):
    """
    General function for interacting with Cytoscape API.

    :param namespace: namespace where the request should be executed. eg. "string"
    :param commnand: command to execute. eg. "protein query"
    :param PARAMs: a dictionary with the parameters. Check your swagger normaly running on
    http://localhost:1234/v1/swaggerUI/swagger-ui/index.html?url=http://localhost:1234/v1/commands/swagger.json
    :param host: cytoscape host address, default=cytoscape_host
    :param port: cytoscape port, default=1234
    :param version: API version
    :param method: type of http call, ie. "POST" or "GET" or "HELP".
    :param verbose: print more information

    :returns: For "POST" the data in the content's response. For "GET" None.

    eg.
    cytoscape("string","pubmed query",{"pubmed":"p53 p21","limit":"50"})
    """

    if url:
        baseurl=url
    else:
        if namespace:
            baseurl="http://"+str(host)+":"+str(port)+"/"+str(version)+"/commands/"+str(namespace)+"/"+str(command)
        else:
            baseurl="http://"+str(host)+":"+str(port)+"/"+str(version)+"/commands"

    if (method == "GET") or (method == "G"):
        URL=baseurl
        if verbose:
            print("'"+URL+"'")
            sys.stdout.flush()
        r = requests.get(url = URL, params=PARAMS)
        verbose_=checkresponse(r, verbose=verbose)
        if (verbose) or (verbose_):
            print("'"+URL+"'")
            sys.stdout.flush()

        if verbose_:
            res=verbose_
        else:
            res=r

    if (method == "DELETE"):
        URL=baseurl
        if verbose:
            print("'"+URL+"'")
            sys.stdout.flush()
        r = requests.delete(url = URL)
        verbose_=checkresponse(r, verbose=verbose)
        if (verbose) or (verbose_):
            print("'"+URL+"'")
            sys.stdout.flush()
        res=r.json()
        if len(res["errors"]) > 0:
            raise ValueError(res["errors"][0])

    elif (method == "POST") or (method == "P"):
        if verbose:
            print("'"+baseurl+"'")
            sys.stdout.flush()
        r = requests.post(url = baseurl, json = PARAMS)
        verbose_=checkresponse(r, verbose=verbose)
        if (verbose) or (verbose_):
            verbose=True
            print(r.content)
            sys.stdout.flush()

        res=r.json()
        if "errors" in res.keys():
            if len(res["errors"]) > 0:
                raise ValueError(res["errors"][0])
        if not verbose:
            if "data" in res.keys():
                res=res["data"]
        else:
            res=verbose_

    elif (method == "PUT"):
        if verbose:
            print("'"+baseurl+"'")
            sys.stdout.flush()
        r = requests.put(url = baseurl, json = body)

        verbose_=checkresponse(r, verbose=verbose)
        if (verbose) or (verbose_):
            verbose=True
            print(r.content)
            sys.stdout.flush()

        try:
            res=r.json()
            if "errors" in res.keys():
                if len(res["errors"]) > 0:
                    raise ValueError(res["errors"][0])
        except JSONDecodeError:
            if not r.text:
                res = {}
            else:
                raise

    elif (method=="HTML") or (method == "H") or (method=="HELP"):
        URL = baseurl
        if verbose:
            print("'"+URL+"'")
            sys.stdout.flush()
        response = requests.get(URL, params=PARAMS)

        res = response.text.split("\n")
        def clean(x):
            r=x.split("</p>")[0].split(">")[-1]
            return r
        res="\n".join([ clean(x) for x in res ])

    res=handle_status_codes(res,verbose=verbose)

    return res
