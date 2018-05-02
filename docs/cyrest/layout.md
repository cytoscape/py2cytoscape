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

## ***cyclient.layout.fruchterman_rheingold***

**`cyclient.layout.fruchterman_rheingold(self,attraction_multiplier=None,conflict_avoidance=None,		defaultEdgeWeight=None,EdgeAttribute=None,gravity_multiplier=None,\		layout3D=None,max_distance_factor=None,maxWeightCutoff=None,minWeightCutoff=None,\		network=None,nIterations=None,NodeAttribute=None,nodeList=None,randomize=None,\		repulsion_multiplier=None,singlePartition=None,spread_factor=None,\		temperature=None,Type=None,update_iterations=None,verbose=None)`**

Execute the Edge-weighted Force directed (BioLayout) on a network

* **`attraction_multiplier (string, optional)`** Divisor to calculate the a
			ttraction force, in numeric value
* **`conflict_avoidance (string, optional)`** Constant force applied to avo
			id conflicts, in numeric value
* **`defaultEdgeWeight (string, optional)`** The default edge weight to con
			sider, default is 0.5
* **`EdgeAttribute (string, optional)`** The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`gravity_multiplier (string, optional)`** Multiplier to calculate the g
			ravity force, in numeric value
* **`layout3D (string, optional)`** Layout nodes in 3D; boolean values only
			, true or false; defaults to true
* **`max_distance_factor (string, optional)`** Percent of graph used for no
			de repulsion calculations, in numeric value
* **`maxWeightCutoff (string, optional)`** The maximum edge weight to consi
			der, default to the Double.MAX value
* **`minWeightCutoff (string, optional)`** The minimum edge weight to consi
			der, numeric values, default is 0
* **`network (string, optional)`** Specifies a network by name, or by SUID
			if the prefix SUID: is used. The keyword CURRENT, or a blank value c
			an also be used to specify the current network.
* **`nIterations (string, optional)`** Number of iterations, in numeric val
			ue
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
* **`repulsion_multiplier (string, optional)`** Multiplier to calculate the
			 repulsion force, in numeric value
* **`singlePartition (string, optional)`** Don't partition graph before lay
			out; boolean values only, true or false; defaults to false
* **`spread_factor (string, optional)`** Amount of extra room for layout, i
			n numeric value
* **`temperature (string, optional)`** Initial temperature, in numeric valu
			e
* **`Type (string, optional)`** How to interpret weight values; must be one
			 of Heuristic, -Log(value), 1 - normalized value and normalized valu
			e. Defaults to Heuristic = ['Heuristic', '-Log(value)', '1 - normali
			zed value', 'normalized value']
* **`update_iterations (string, optional)`** Number of iterations before up
			dating display, in numeric value (0: update only at end)

___

## ***cyclient.layout.genemania_force_directed***

**`cyclient.layout.genemania_force_directed(self,curveSteepness=None,defaultEdgeWeight=None,		defaultSpringCoefficient=None,defaultSpringLength=None,EdgeAttribute=None,\		ignoreHiddenElements=None,isDeterministic=None,maxNodeMass=None,\		maxWeightCutoff=None,midpointEdges=None,minNodeMass=None,minWeightCutoff=None,\		network=None,NodeAttribute=None,nodeList=None,numIterations=None,\		singlePartition=None,Type=None,verbose=None)`**

Execute the GeneMANIA Force Directed Layout on a network.

* **`curveSteepness (string, optional)`** 
* **`defaultEdgeWeight (string, optional)`** The default edge weight to con
			sider, default is 0.5
* **`defaultSpringCoefficient (string, optional)`** 
* **`defaultSpringLength (string, optional)`** 
* **`EdgeAttribute (string, optional)`** The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`ignoreHiddenElements (string, optional)`** 
* **`isDeterministic (string, optional)`** 
* **`maxNodeMass (string, optional)`** 
* **`maxWeightCutoff (string, optional)`** The maximum edge weight to consi
			der, default to the Double.MAX value
* **`midpointEdges (string, optional)`** 
* **`minNodeMass (string, optional)`** 
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
* **`numIterations (string, optional)`** 
* **`singlePartition (string, optional)`** 
* **`Type (string, optional)`** How to interpret weight values; must be one
			 of Heuristic, -Log(value), 1 - normalized value and normalized valu
			e. Defaults to Heuristic = ['Heuristic', '-Log(value)', '1 - normali
			zed value', 'normalized value']

___

## ***cyclient.layout.get_preferred***

**`cyclient.layout.get_preferred(self,network=None,verbose=None)`**

Returns the name of the current preferred layout or empty string if not
set. Default is grid.

* **`network (string, optional)`** Gets the name of the current preferred l
			ayout

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

## ***cyclient.layout.isom***

**`cyclient.layout.isom(self,coolingFactor=None,EdgeAttribute=None,initialAdaptation=None,		maxEpoch=None,minAdaptation=None,minRadius=None,network=None,NodeAttribute=None,\		nodeList=None,radius=None,radiusConstantTime=None,singlePartition=None,\		sizeFactor=None,verbose=None)`**

Execute the Inverted Self-Organizing Map Layout on a network.

* **`coolingFactor (string, optional)`** Cooling factor, in numeric value
* **`EdgeAttribute (string, optional)`** The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`initialAdaptation (string, optional)`** Initial adaptation, in numeric
			 value
* **`maxEpoch (string, optional)`** Number of iterations, in numeric value
* **`minAdaptation (string, optional)`** Minimum adaptation value, in numer
			ic value
* **`minRadius (string, optional)`** Minimum radius, in numeric value
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
* **`radius (string, optional)`** Radius, in numeric value
* **`radiusConstantTime (string, optional)`** Radius constant, in numeric v
			alue
* **`singlePartition (string, optional)`** Don't partition graph before lay
			out; boolean values only, true or false; defaults to false
* **`sizeFactor (string, optional)`** Size factor, in numeric value

___

## ***cyclient.layout.cose***

**`cyclient.layout.cose(self,compoundGravityRange=None,compoundGravityStrength=None,		EdgeAttribute=None,gravityRange=None,gravityStrength=None,idealEdgeLength=None,\		incremental=None,LayoutQuality=None,network=None,NodeAttribute=None,\		nodeList=None,repulsionStrength=None,smartEdgeLengthCalc=None,\		smartRepulsionRangeCalc=None,springStrength=None,verbose=None)`**

Execute the Compound Spring Embedder (CoSE) on a network

* **`compoundGravityRange (string, optional)`** Compound gravity range (0-1
			00)
* **`compoundGravityStrength (string, optional)`** Compound gravity strengt
			h (0-100)
* **`EdgeAttribute (string, optional)`** The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`gravityRange (string, optional)`** Gravity range (0-100)
* **`gravityStrength (string, optional)`** Gravity strength (0-100)
* **`idealEdgeLength (string, optional)`** Ideal edge length, any positive
			integer
* **`incremental (string, optional)`** Incremental; whether the algorithm w
			ill be applied incrementally; boolean values only, true or false; de
			faults to false
* **`LayoutQuality (string, optional)`** Layout quality; allowed values are
			 Proof, Default and Draft = ['Proof', 'Default', 'Draft']
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
* **`repulsionStrength (string, optional)`** Repulsion strength (0-100)
* **`smartEdgeLengthCalc (string, optional)`** Use smart edge length calcul
			ation; boolean values only, true or false; defaults to true
* **`smartRepulsionRangeCalc (string, optional)`** Use smart repulsion rang
			e calculation; boolean values only, true or false; defaults to true
* **`springStrength (string, optional)`** Spring strength (0-100)

___

## ***cyclient.layout.set_preferred***

**`cyclient.layout.set_preferred(self,preferredLayout=None,verbose=None)`**

Sets the preferred layout. Takes a specific name as defined in the API
Default is grid.

* **`preferredLayout (string, optional)`** Layout to use as preferred, for
			allowed names see Layout API

___

## ***cyclient.layout.stacked_node_layout***

**`cyclient.layout.stacked_node_layout(self,EdgeAttribute=None,network=None,NodeAttribute=None,		nodeList=None,x_position=None,y_start_position=None,verbose=None)`**

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

## ***cyclient.layout.force_directed***

**`cyclient.layout.force_directed(self,defaultEdgeWeight=None,defaultNodeMass=None,		defaultSpringCoefficient=None,defaultSpringLength=None,EdgeAttribute=None,\		isDeterministic=None,maxWeightCutoff=None,minWeightCutoff=None,network=None,\		NodeAttribute=None,nodeList=None,numIterations=None,singlePartition=None,\		Type=None,verbose=None)`**

Execute the Prefuse Force Directed Layout on a network

* **`defaultEdgeWeight (string, optional)`** The default edge weight to con
			sider, default is 0.5
* **`defaultNodeMass (string, optional)`** Default Node Mass, in numeric va
			lue
* **`defaultSpringCoefficient (string, optional)`** Default Spring Coeffici
			ent, in numeric value
* **`defaultSpringLength (string, optional)`** Default Spring Length, in nu
			meric value
* **`EdgeAttribute (string, optional)`** The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`isDeterministic (string, optional)`** Force deterministic layouts (slo
			wer); boolean values only, true or false; defaults to false
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
* **`numIterations (string, optional)`** Number of Iterations, in numeric v
			alue
* **`singlePartition (string, optional)`** Don't partition graph before lay
			out; boolean values only, true or false; defaults to false
* **`Type (string, optional)`** How to interpret weight values; must be one
			 of Heuristic, -Log(value), 1 - normalized value and normalized valu
			e. Defaults to Heuristic = ['Heuristic', '-Log(value)', '1 - normali
			zed value', 'normalized value']

___

## ***cyclient.layout.hierarchical***

**`cyclient.layout.hierarchical(self,bandGap=None,componentSpacing=None,EdgeAttribute=None,		leftEdge=None,network=None,NodeAttribute=None,nodeHorizontalSpacing=None,\		nodeList=None,nodeVerticalSpacing=None,rightMargin=None,topEdge=None,\		verbose=None)`**

Execute the Hierarchical Layout on a network.

* **`bandGap (string, optional)`** Band gap, in numeric value
* **`componentSpacing (string, optional)`** Component spacing, in numeric v
			alue
* **`EdgeAttribute (string, optional)`** The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`leftEdge (string, optional)`** Left edge margin, in numeric value
* **`network (string, optional)`** Specifies a network by name, or by SUID
			if the prefix SUID: is used. The keyword CURRENT, or a blank value c
			an also be used to specify the current network.
* **`NodeAttribute (string, optional)`** The name of the node column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`nodeHorizontalSpacing (string, optional)`** Horizontal spacing between
			 nodes, in numeric value
* **`nodeList (string, optional)`** Specifies a list of nodes. The keywords
			 all, selected, or unselected can be used to specify nodes by their
			selection state. The pattern COLUMN:VALUE sets this parameter to any
			 rows that contain the specified column value; if the COLUMN prefix
			is not used, the NAME column is matched by default. A list of COLUMN
			:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be
			used to match multiple values.
* **`nodeVerticalSpacing (string, optional)`** Vertical spacing between nod
			es, in numeric value
* **`rightMargin (string, optional)`** Right edge margin, in numeric value
* **`topEdge (string, optional)`** Top edge margin, in numeric value

___

## ***cyclient.layout.grid***

**`cyclient.layout.grid(self,EdgeAttribute=None,network=None,NodeAttribute=None,		nodeHorizontalSpacing=None,nodeList=None,nodeVerticalSpacing=None,verbose=None)`**

Execute the Grid Layout on a network.

* **`EdgeAttribute (string, optional)`** The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`network (string, optional)`** Specifies a network by name, or by SUID
			if the prefix SUID: is used. The keyword CURRENT, or a blank value c
			an also be used to specify the current network.
* **`NodeAttribute (string, optional)`** The name of the node column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`nodeHorizontalSpacing (string, optional)`** Horizontal spacing between
			 nodes, in numeric value
* **`nodeList (string, optional)`** Specifies a list of nodes. The keywords
			 all, selected, or unselected can be used to specify nodes by their
			selection state. The pattern COLUMN:VALUE sets this parameter to any
			 rows that contain the specified column value; if the COLUMN prefix
			is not used, the NAME column is matched by default. A list of COLUMN
			:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be
			used to match multiple values.
* **`nodeVerticalSpacing (string, optional)`** Vertical spacing between nod
			es, in numeric value

___

## ***cyclient.layout.attributes_layout***

**`cyclient.layout.attributes_layout(self, EdgeAttribute=None, maxwidth=None, minrad=None,     network=None, NodeAttribute=None,nodeList=None, radmult=None, \    spacingx=None, spacingy=None, verbose=False)`**

Execute the Group Attributes Layout on a network

* **`EdgeAttribute (string, optional)`** The name of the edge column
containing numeric values that will be used as weights in the layout
algorithm. Only columns containing numeric values are shown
* **`maxwidth (string, optional)`** Maximum width of a row, in numeric value
* **`minrad (string, optional)`** Minimum width of a partition, in
numeric value
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
prefix is not used, the NAME column is matched by default. A list
of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`radmult (string, optional)`** Minimum width of a partition, in
numeric value
* **`spacingx (string, optional)`** Horizontal spacing between two
partitions in a row, in numeric value
* **`spacingy (string, optional)`** Vertical spacing between the largest
partitions of two rows, in numeric value
* **`verbose`** print more


___

## ***cyclient.layout.degree_circle***

**`cyclient.layout.degree_circle(self,EdgeAttribute=None,network=None,NodeAttribute=None,    	nodeList=None,singlePartition=None,verbose=None)`**

Execute the Degree Sorted Circle Layout on a network.

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
* **`singlePartition (string, optional)`** Don't partition graph before lay
			out; boolean values only, true or false; defaults to false

___

## ***cyclient.layout.force_directed_cl***

**`cyclient.layout.force_directed_cl(self,defaultEdgeWeight=None,defaultNodeMass=None,		defaultSpringCoefficient=None,defaultSpringLength=None,EdgeAttribute=None,\		fromScratch=None,isDeterministic=None,maxWeightCutoff=None,minWeightCutoff=None,\		network=None,NodeAttribute=None,nodeList=None,numIterations=None,\		numIterationsEdgeRepulsive=None,singlePartition=None,Type=None,verbose=None)`**

Execute the Prefuse Force Directed OpenCL Layout on a network.

* **`defaultEdgeWeight (string, optional)`** The default edge weight to con
			sider, default is 0.5
* **`defaultNodeMass (string, optional)`** 
* **`defaultSpringCoefficient (string, optional)`** 
* **`defaultSpringLength (string, optional)`** 
* **`EdgeAttribute (string, optional)`** The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`fromScratch (string, optional)`** 
* **`isDeterministic (string, optional)`** 
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
* **`numIterations (string, optional)`** 
* **`numIterationsEdgeRepulsive (string, optional)`** 
* **`singlePartition (string, optional)`** 
* **`Type (string, optional)`** How to interpret weight values; must be one
			 of Heuristic, -Log(value), 1 - normalized value and normalized valu
			e. Defaults to Heuristic = ['Heuristic', '-Log(value)', '1 - normali
			zed value', 'normalized value']

___

## ***cyclient.layout.circular***

**`cyclient.layout.circular(self,EdgeAttribute=None,leftEdge=None,network=None,	NodeAttribute=None,nodeHorizontalSpacing=None,nodeList=None,\	nodeVerticalSpacing=None,rightMargin=None,singlePartition=None,topEdge=None,\    verbose=None)`**

Execute the Circular Layout on a network

* **`EdgeAttribute (string, optional)`** The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`leftEdge (string, optional)`** Left edge margin, in numeric value
* **`network (string, optional)`** Specifies a network by name, or by SUID
			if the prefix SUID: is used. The keyword CURRENT, or a blank value c
			an also be used to specify the current network.
* **`NodeAttribute (string, optional)`** The name of the node column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
* **`nodeHorizontalSpacing (string, optional)`** Horizontal spacing between
			 nodes, in numeric value
* **`nodeList (string, optional)`** Specifies a list of nodes. The keywords
			 all, selected, or unselected can be used to specify nodes by their
			selection state. The pattern COLUMN:VALUE sets this parameter to any
			 rows that contain the specified column value; if the COLUMN prefix
			is not used, the NAME column is matched by default. A list of COLUMN
			:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be
			used to match multiple values.
* **`nodeVerticalSpacing (string, optional)`** Vertical spacing between nod
			es, in numeric value
* **`rightMargin (string, optional)`** Right edge margin, in numeric value
* **`singlePartition (string, optional)`** Don't partition graph before lay
			out; only boolean values are allowed: true or false
* **`topEdge (string, optional)`** Top edge margin, in numeric value

___

