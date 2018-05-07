## ***cyclient.vizmap.apply***

**`cyclient.vizmap.apply(self, styles=None, verbose=False)`**

Applies the specified style to the selected views and returns the
SUIDs of the affected views.

* **`styles (string)`** Name of Style to be applied to the selected
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
* **`verbose`** print more


___

## ***cyclient.vizmap.load_file***

**`cyclient.vizmap.load_file(self, afile=None, verbose=False)`**

Loads styles from a vizmap (XML or properties) file and returns the names of the loaded styles.

* **`afile (string)`** XML or properties file where one or more styles have been saved to.
* **`verbose`** print more


___

## ***cyclient.vizmap.export***

**`cyclient.vizmap.export(self, options=None, OutputFile=None, styles=None, verbose=False)`**

Exports the specified styles to a Cytoscape vizmap (XML) or a Cytoscape.js
(JSON) file and returns the path to the saved file.

* **`options (string, optional)`** The format of the output file. =
['Style XML (*.xml)', 'Style for cytoscape.js (*.json)']
* **`OutputFile (string)`** The path name of the file where the styles
must be saved to.
* **`styles (string, optional)`** The styles to be exported. If no styles
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
* **`verbose`** print more


___

## ***cyclient.vizmap.create_style***

**`cyclient.vizmap.create_style(self, title=None,mappings=None,verbose=VERBOSE)`**

Creates a new visual style
        
* **`title` title of the visual style
* **`defaults` a list of dictionaries for each visualProperty
* **`mappings` a list of dictionaries for each visualProperty

* **`returns` nothing
___

## ***cyclient.vizmap.update_style***

**`cyclient.vizmap.update_style(self, title=None,mappings=None,verbose=VERBOSE)`**

Updates a visual style
        
* **`title` title of the visual style
* **`defaults` a list of dictionaries for each visualProperty
* **`mappings` a list of dictionaries for each visualProperty
        
* **`returns` nothing
___

## ***cyclient.vizmap.mapVisualProperty***

Generates a dictionary for a given visual property


**`cyclient.vizmap.mapVisualProperty(self, visualProperty=None,mappingType,=None, mappingColumn= None, lower=None,center=None,upper=None, discrete=None, network="current",table="node",namespace="default",verbose=False)`**

* **`visualProperty` visualProperty
* **`mappingType` mappingType
* **`mappingColumn` mappingColumn
* **`lower` for "continuous" mappings a list of the form [value,rgb_string]
* **`center` for "continuous" mappings a list of the form [value,rgb_string]
* **`upper` for "continuous" mappings a list of the form [value,rgb_string]
* **`discrete` for discrete mappings, a list of lists of the form [ list_of_keys, list_of_values ]
* **`network (string, optional)` Specifies a network by name, or by
    SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
    value can also be used to specify the current network.
* **`namespace (string, optional)` Node, Edge, and Network objects support
    the default, local, and hidden namespaces. Root networks also support the
    shared namespace. Custom namespaces may be specified by Apps.

* **`returns` a dictionary for the respective visual property
___ 

## ***cyclient.vizmap.simple_defaults***

Simplifies defaults.

**`simple_defaults(self, defaults_dic)`**

* **`defaults_dic` a dictionary of the form { visualProperty_A:value_A, visualProperty_B:value_B, ..}

* **`returns` a list of dictionaries with each item corresponding to a given key in defaults_dic
___ 
