## ***cyclient.layout.kamada_kawai***

**`cyclient.layout.kamada_kawai(self,defaultEdgeWeight=None,EdgeAttribute=None,		m_anticollisionSpringStrength=None,m_averageIterationsPerNode=None,\		m_disconnectedNodeDistanceSpringRestLength=None,\		m_disconnectedNodeDistanceSpringStrength=None,m_layoutPass=None,\		m_nodeDistanceRestLengthConstant=None,m_nodeDistanceStrengthConstant=None,\		maxWeightCutoff=None,minWeightCutoff=None,network=None,NodeAttribute=None,\		nodeList=None,randomize=None,singlePartition=None,Type=None,unweighted=None,\		verbose=None)`**

Execute the Edge-weighted Spring Embedded Layout on a network.

* **`defaultEdgeWeight (string, optional)`** The default edge weight to con
			sider, default is 0.5
* **`EdgeAttribute (string, optional)`** The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`m_anticollisionSpringStrength (string, optional)`** Strength to apply
			to avoid collisions, in numeric value
* **`m_averageIterationsPerNode (string, optional)`** Average number of ite
			ratations for each node, in numeric value
* **`m_disconnectedNodeDistanceSpringRestLength (string, optional)`** Rest
			length of a 'disconnected' spring, in numeric value
* **`m_disconnectedNodeDistanceSpringStrength (string, optional)`** Strengt
			h of a 'disconnected' spring, in numeric value
* **`m_layoutPass (string, optional)`** Number of layout passes, in numeric
			 value
* **`m_nodeDistanceRestLengthConstant (string, optional)`** Spring rest len
			gth, in numeric value
* **`m_nodeDistanceStrengthConstant (string, optional)`** Spring strength,
			in numeric value
* **`maxWeightCutoff (string, optional)`** The maximum edge weight to consi
			der, default to the Double.MAX value
* **`minWeightCutoff (string, optional)`** The minimum edge weight to consi
			der, numeric values, default is 0
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
* **`randomize (string, optional)`** Randomize graph before layout; boolean
			 values only, true or false; defaults to true
* **`singlePartition (string, optional)`** Don't partition graph before lay
			out; boolean values only, true or false; defaults to false
* **`Type (string, optional)`** How to interpret weight values; must be one
			 of Heuristic, -Log(value), 1 - normalized value and normalized valu
			e. Defaults to Heuristic = ['Heuristic', '-Log(value)', '1 - normali
			zed value', 'normalized value']
* **`unweighted (string, optional)`** Use unweighted edges; boolean values
			only, true or false; defaults to false

___

## ***cyclient.layout.apply_preferred***

**`cyclient.layout.apply_preferred(self, network=None, verbose=False)`**

Executes the current preferred layout. Default is grid.

* **`networkSelected (string, optional)`** Specifies a network by name,
or by SUID if the prefix SUID: is used. The keyword CURRENT, or a
blank value can also be used to specify the current network.
* **`verbose`** print more


___

## ***cyclient.layout.copycat***

**`cyclient.layout.copycat(self,gridUnmapped=None,selectUnmapped=None,sourceColumn=None,    	sourceNetwork=None,targetColumn=None,targetNetwork=None,verbose=None)`**

Sets the coordinates for each node in the target network to the coordinates
of a matching node in the source network.
Optional parameters such as gridUnmapped and selectUnmapped determine
the behavior of target network nodes that could not be matched.

* **`gridUnmapped (string, optional)`** If this is set to true, any nodes i
			n the target network that could not be matched to a node in the sour
			ce network will be laid out in a grid
* **`selectUnmapped (string, optional)`** If this is set to true, any nodes
			 in the target network that could not be matched to a node in the so
			urce network will be selected in the target network
* **`sourceColumn (string)`** The name of column in the node table used to
			match nodes
* **`sourceNetwork (string)`** The name of network to get node coordinates
			from
* **`targetColumn (string)`** The name of column in the node table used to
			match nodes
* **`targetNetwork (string)`** The name of the network to apply coordinates
			 to.

___

