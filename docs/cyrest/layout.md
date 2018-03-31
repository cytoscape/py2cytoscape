## ***cyclient.layout.apply_preferred***

**`cyclient.layout.apply_preferred(self, network=None, verbose=False)`**

Executes the current preferred layout. Default is grid.

* **`networkSelected (string, optional)`** Specifies a network by name,
or by SUID if the prefix SUID: is used. The keyword CURRENT, or a
blank value can also be used to specify the current network.
* **`verbose`** print more


___

## ***cyclient.layout.attribute_circle***

**`cyclient.layout.attribute_circle(self, EdgeAttribute=None, network=None,     NodeAttribute=None, nodeList=None, singlePartition=None,\    spacing=None, verbose=False)`**

Execute the Attribute Circle Layout on a network.

* **`EdgeAttribute (string, optional)`** The name of the edge column
containing numeric values that will be used as weights in the layout
algorithm. Only columns containing numeric values are shown
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`NodeAttribute (string, optional)`** The name of the node column
containing numeric values that will be used as weights in the layout
algorithm. Only columns containing numeric values are shown
* **`nodeList (string, optional)`** Specifies a list of nodes. The
keywords all, selected, or unselected can be used to specify nodes
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list of
COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`singlePartition (string, optional)`** Don't partition graph before
layout, only boolean values allowed: true or false
* **`spacing (string, optional)`** Circle size, in numeric value
* **`verbose`** print more


___

## ***cyclient.layout.attributes_layout***

**`cyclient.layout.attributes_layout(self, EdgeAttribute=None, maxwidth=None, minrad=None,     network=None, NodeAttribute=None,nodeList=None, radmult=None, \    spacingx=None, spacingy=None, verbose=False)`**

Execute the Stacked Node Layout on a network.

* **`EdgeAttribute (string, optional)`** The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`network (string, optional)`** Specifies a network by name, or by SUID
			if the prefix SUID: is used. The keyword CURRENT, or a blank value c
			an also be used to specify the current network.
* **`NodeAttribute (string, optional)`** The name of the node column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`nodeList (string, optional)`** Specifies a list of nodes. The keywords
			 all, selected, or unselected can be used to specify nodes by their
			selection state. The pattern COLUMN:VALUE sets this parameter to any
			 rows that contain the specified column value; if the COLUMN prefix
			is not used, the NAME column is matched by default. A list of COLUMN
			:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be
			used to match multiple values.
* **`x_position (string, optional)`** X start position, in numeric value
* **`y_start_position (string, optional)`** Y start position, in numeric va
			lue

___

