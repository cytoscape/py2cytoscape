from .base import *

class vizmap(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation for 'vizmap'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/vizmap'

    def apply(self, styles=None, verbose=False):
        """
        Applies the specified style to the selected views and returns the
        SUIDs of the affected views.

        :param styles (string): Name of Style to be applied to the selected
            views. = ['Directed', 'BioPAX_SIF', 'Bridging Reads Histogram:unique_0',
            'PSIMI 25 Style', 'Coverage Histogram:best&unique', 'Minimal',
            'Bridging Reads Histogram:best&unique_0', 'Coverage Histogram_0',
            'Big Labels', 'No Histogram:best&unique_0', 'Bridging Reads Histogram:best',
            'No Histogram_0', 'No Histogram:best&unique', 'Bridging Reads Histogram_0',
            'Ripple', 'Coverage Histogram:unique_0', 'Nested Network Style',
            'Coverage Histogram:best', 'Coverage Histogram:best&unique_0',
            'default black', 'No Histogram:best_0', 'No Histogram:unique',
            'No Histogram:unique_0', 'Solid', 'Bridging Reads Histogram:unique',
            'No Histogram:best', 'Coverage Histogram', 'BioPAX', 'Bridging Reads Histogram',
            'Coverage Histogram:best_0', 'Sample1', 'Universe', 'Bridging Reads Histogram:best_0',
            'Coverage Histogram:unique', 'Bridging Reads Histogram:best&unique',
            'No Histogram', 'default']
        :param verbose: print more
        :returns: SUIDs of the affected views

        """

        PARAMS=set_param(["styles"],[styles])
        response=api(url=self.__url+"/apply", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def export(self, options=None, OutputFile=None, styles=None, verbose=False):
        """
        Exports the specified styles to a Cytoscape vizmap (XML) or a Cytoscape.js
        (JSON) file and returns the path to the saved file.

        :param options (string, optional): The format of the output file. =
            ['Style XML (*.xml)', 'Style for cytoscape.js (*.json)']
        :param OutputFile (string): The path name of the file where the styles
            must be saved to.
        :param styles (string, optional): The styles to be exported. If no styles
            are specified, only the current one is exported. = ['Big Labels',
            'BioPAX', 'BioPAX_SIF', 'Bridging Reads Histogram', 'Bridging Reads
            Histogram_0', 'Bridging Reads Histogram:best', 'Bridging Reads Histogram:best_0',
            'Bridging Reads Histogram:best&unique', 'Bridging Reads Histogram:best&unique_0',
            'Bridging Reads Histogram:unique', 'Bridging Reads Histogram:unique_0',
            'Coverage Histogram', 'Coverage Histogram_0', 'Coverage Histogram:best',
            'Coverage Histogram:best_0', 'Coverage Histogram:best&unique',
            'Coverage Histogram:best&unique_0', 'Coverage Histogram:unique', '
            Coverage Histogram:unique_0', 'default', 'default black', 'Directed',
            'Minimal', 'Nested Network Style', 'No Histogram', 'No Histogram_0',
            'No Histogram:best', 'No Histogram:best_0', 'No Histogram:best&unique',
            'No Histogram:best&unique_0', 'No Histogram:unique', 'No Histogram:unique_0',
            'PSIMI 25 Style', 'Ripple', 'Sample1', 'Solid', 'Universe']
        :param verbose: print more

        """

        PARAMS=set_param(["options","OutputFile", "styles"],[options,OutputFile,styles])
        response=api(url=self.__url+"/export", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def load_file(self, style_xml, verbose=False):
        """
        Loads styles from a vizmap (XML or properties) file and returns the names of the loaded styles.

        :param afile (string): XML or properties file where one or more styles have been saved to.
        :param verbose: print more

        """
        PARAMS=set_param(["file"], [style_xml])
        response=api(url=self.__url+"/load file", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def create_style(self,title=None,defaults=None,mappings=None,verbose=VERBOSE):
        """
        Creates a new visual style

        :param title: title of the visual style
        :param defaults: a list of dictionaries for each visualProperty
        :param mappings: a list of dictionaries for each visualProperty
        :param host: cytoscape host address, default=cytoscape_host
        :param port: cytoscape port, default=1234

        :returns: nothing
        """
        u=self.__url
        host=u.split("//")[1].split(":")[0]
        port=u.split(":")[2].split("/")[0]
        version=u.split(":")[2].split("/")[1]

        if defaults:
            defaults_=[]
            for d in defaults:
                if d:
                    defaults_.append(d)
            defaults=defaults_

        if mappings:
            mappings_=[]
            for m in mappings:
                if m:
                    mappings_.append(m)
            mappings=mappings_

        try:
            update_style(title=title,defaults=defaults,mappings=mappings,host=host,port=port)
            print("Existing style was updated.")
            sys.stdout.flush()
        except:
            print("Creating new style.")
            sys.stdout.flush()
            URL="http://"+str(host)+":"+str(port)+"/v1/styles"
            PARAMS={"title":title,\
                "defaults":defaults,\
                "mappings":mappings}
            r = requests.post(url = URL, json = PARAMS)
            checkresponse(r)

    def update_style(self, title=None,defaults=None,mappings=None, verbose=False):
        """
        Updates a visual style

        :param title: title of the visual style
        :param defaults: a list of dictionaries for each visualProperty
        :param mappings: a list of dictionaries for each visualProperty

        :returns: nothing
        """
        u=self.__url
        host=u.split("//")[1].split(":")[0]
        port=u.split(":")[2].split("/")[0]
        version=u.split(":")[2].split("/")[1]

        if defaults:
            defaults_=[]
            for d in defaults:
                if d:
                    defaults_.append(d)
            defaults=defaults_

        if mappings:
            mappings_=[]
            for m in mappings:
                if m:
                    mappings_.append(m)
            mappings=mappings_

        URL="http://"+str(host)+":"+str(port)+"/v1/styles/"+str(title)
        if verbose:
            print(URL)
            sys.stdout.flush()

        response = requests.get(URL).json()

        olddefaults=response["defaults"]
        oldmappings=response["mappings"]

        if mappings:
            mappings_visual_properties=[ m["visualProperty"] for m in mappings ]
            newmappings=[ m for m in oldmappings if m["visualProperty"] not in mappings_visual_properties ]
            for m in mappings:
                newmappings.append(m)
        else:
            newmappings=oldmappings

        if defaults:
            defaults_visual_properties=[ m["visualProperty"] for m in defaults ]
            newdefaults=[ m for m in olddefaults if m["visualProperty"] not in defaults_visual_properties ]
            for m in defaults:
                newdefaults.append(m)
        else:
            newdefaults=olddefaults

        r=requests.delete(URL)
        checkresponse(r)

        URL="http://"+str(host)+":"+str(port)+"/v1/styles"
        PARAMS={"title":title,\
            "defaults":newdefaults,\
            "mappings":newmappings}
        r = requests.post(url = URL, json = PARAMS)
        checkresponse(r)

    def mapVisualProperty(self, visualProperty=None,mappingType=None, mappingColumn=None,
                        lower=None,center=None,upper=None,\
                        discrete=None,\
                        network="current",table="node",\
                        namespace="default",verbose=False):
        """"
        Generates a dictionary for a given visual property

        :param visualProperty: visualProperty
        :param mappingType: mappingType
        :param mappingColumn: mappingColumn
        :param lower: for "continuous" mappings a list of the form [value,rgb_string]
        :param center: for "continuous" mappings a list of the form [value,rgb_string]
        :param upper: for "continuous" mappings a list of the form [value,rgb_string]
        :param discrete: for discrete mappings, a list of lists of the form [ list_of_keys, list_of_values ]
		:param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param namespace (string, optional): Node, Edge, and Network objects support
            the default, local, and hidden namespaces. Root networks also support the
            shared namespace. Custom namespaces may be specified by Apps.
        :returns: a dictionary for the respective visual property
        """
        u=self.__url
        host=u.split("//")[1].split(":")[0]
        port=u.split(":")[2].split("/")[0]
        version=u.split(":")[2].split("/")[1]

        if type(network) != int:
            network=check_network(self,network,verbose=verbose)
            PARAMS=set_param(["columnList","namespace","network"],["SUID",namespace,network])
            networkID=api(namespace="network", command="get attribute",PARAMS=PARAMS, host=host,port=str(port),version=version)
            PARAMS=set_param(["columnList","namespace","network"],["name",namespace,network])
            networkname=api(namespace="network", command="get attribute",PARAMS=PARAMS, host=host,port=str(port),version=version)
            network=networkID[0]["SUID"]
            networkname=networkname[0]["name"]

        URL="http://"+str(host)+":"+str(port)+"/v1/networks/"+str(network)+"/tables/"+namespace+table+"/columns/"
        if verbose:
            print(URL)
            sys.stdout.flush()
        response = requests.get(URL).json()

        mappingColumnType=None
        for r in response:
            if r["name"]==mappingColumn:
                mappingColumnType=r["type"]
                break
        if not mappingColumnType:
            print("For mappingType: "+mappingType+" it was not possible to find a  mappingColumnType.")
            sys.stdout.flush()

        PARAMS={"mappingType" : mappingType,\
                "mappingColumn" : mappingColumn,
                "mappingColumnType" : mappingColumnType,
                "visualProperty" : visualProperty}
        if mappingType == "continuous":
            PARAMS["points"]=[{"value" : lower[0],\
                            "lesser" : lower[1],\
                            "equal" : lower[1],\
                            "greater" : lower[1]},\
                            {"value" : center[0],
                            "lesser" : center[1],
                            "equal" : center[1],
                            "greater" : center[1] },\
                            {"value" : upper[0],\
                            "lesser" : upper[1],\
                            "equal" : upper[1],\
                            "greater" : upper[1]}]

        if discrete:
            PARAMS["map"]=[]
            for k,v in zip(discrete[0],discrete[1]):
                PARAMS["map"].append({ "key":k,"value":v})

        if not mappingColumnType:
            res=None
        else:
            res=PARAMS

        return res

    def simple_defaults(self, defaults_dic):
        """
        Simplifies defaults.

        :param defaults_dic: a dictionary of the form { visualProperty_A:value_A, visualProperty_B:value_B, ..}

        :returns: a list of dictionaries with each item corresponding to a given key in defaults_dic
        """

        defaults=[]
        for d in defaults_dic.keys():
            dic={}
            dic["visualProperty"]=d
            dic["value"]=defaults_dic[d]
            defaults.append(dic)
        return defaults
