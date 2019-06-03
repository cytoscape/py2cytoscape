from json import JSONDecodeError

import requests

HOST = 'localhost'
IP = HOST  # temporary
PORT = 1234
VERSION = 'v1'
BASE_URL = 'http://' + HOST + ':' + str(PORT) + '/' + VERSION + '/'
HEADERS = {'Content-Type': 'application/json'}
VERBOSE = False


SUID_LIST = 'suid'

BASE_URL_NETWORK = BASE_URL + 'networks'


def set_param(parameters, values):
    return {p: v for p, v in zip(parameters, values) if v}


def check_network(cyrest_network, network=None, verbose=False):
    if network is None:
        try:
            network_name = cyrest_network.network_name
        except AttributeError:
            network_name = 'CURRENT'
    else:
        network_name = network
    if verbose:
        print("Working on '%s' network." % str(network_name))
    return network_name


def checkresponse(r, verbose=False):
    status = r.status_code
    if 200 <= status < 300:
        if verbose:
            print("response status " + status, flush=True)
        res = None
    else:
        print(r, r.status_code, flush=True)
        res = "error::" + str(r.status_code)
    return res


def handle_status_codes(x, verbose=False):
    if isinstance(x, str):
        if "error::" in x:
            res = int(x.lstrip("error::"))
        else:
            res = None
    else:
        res = None

    if not res and verbose:
        res = x
    else:
        res = None

    if not res and x:
        res = x

    return res


def _clean(x):
    return x.split("</p>")[0].split(">")[-1]


def api(namespace=None,
        command="",
        params=None,
        body=None,
        host=HOST,
        port=str(PORT),
        version=VERSION,
        method="POST",
        verbose=VERBOSE,
        url=None,
        **kwargs):
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

    if params is None:
        params = {}

    if url:
        baseurl = url
    else:
        if namespace:
            baseurl = "http://" + str(host) + ":" + str(port) + "/" + str(version) + \
                "/commands/" + str(namespace) + "/" + str(command)
        else:
            baseurl = "http://" + str(host) + ":" + str(port) + "/" + str(version) + "/commands"

    if method in ('G', 'GET'):
        URL = baseurl
        if verbose:
            print("'" + URL + "'", flush=True)
        r = requests.get(url=URL, params=params)
        verbose_ = checkresponse(r, verbose=verbose)
        if (verbose) or (verbose_):
            print("'" + URL + "'", flush=True)

        if verbose_:
            res = verbose_
        else:
            res = r

    if method == "DELETE":
        URL = baseurl
        if verbose:
            print("'" + URL + "'", flush=True)
        r = requests.delete(url=URL)
        verbose_ = checkresponse(r, verbose=verbose)
        if (verbose) or (verbose_):
            print("'" + URL + "'", flush=True)
        res = r.json()
        if len(res["errors"]) > 0:
            raise ValueError(res["errors"][0])

    elif method in ('P', 'POST'):
        if verbose:
            print("'" + baseurl + "'", flush=True)
        r = requests.post(url=baseurl, json=params)
        verbose_ = checkresponse(r, verbose=verbose)
        if (verbose) or (verbose_):
            verbose = True
            print(r.content, flush=True)

        res = r.json()
        if "errors" in res.keys():
            if len(res["errors"]) > 0:
                raise ValueError(res["errors"][0])
        if not verbose:
            if "data" in res.keys():
                res = res["data"]
        else:
            res = verbose_

    elif (method == "PUT"):
        if verbose:
            print("'" + baseurl + "'", flush=True)
        r = requests.put(url=baseurl, json=body)

        verbose_ = checkresponse(r, verbose=verbose)
        if (verbose) or (verbose_):
            verbose = True
            print(r.content, flush=True)

        try:
            res = r.json()
            if "errors" in res.keys():
                if len(res["errors"]) > 0:
                    raise ValueError(res["errors"][0])
        except JSONDecodeError:
            if not r.text:
                res = {}
            else:
                raise

    elif method in ('H', 'HTML', 'HELP'):
        URL = baseurl
        if verbose:
            print("'" + URL + "'", flush=True)
        response = requests.get(URL, params=params)

        res = response.text.split("\n")

        res = "\n".join(map(_clean, res))

    res = handle_status_codes(res, verbose=verbose)

    return res
