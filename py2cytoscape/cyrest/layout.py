rom .base import *

class layout(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation for 'layout'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/layout'

    def apply_preferred(self, network=None, verbose=False):
        """
        Executes the current preferred layout. Default is grid.

        :param networkSelected (string, optional): Specifies a network by name,
            or by SUID if the prefix SUID: is used. The keyword CURRENT, or a
            blank value can also be used to specify the current network.
        :param verbose: print more

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["network"],[network])
        response=api(url=self.__url+"/apply preferred", PARAMS=PARAMS, method="POST", verbose=verbose)

    def attribute_circle(self, EdgeAttribute=None, network=None, \
    NodeAttribute=None, nodeList=None, singlePartition=None,\
    spacing=None, verbose=False):
        """

        :param EdgeAttribute (string, optional): The name of the edge column
            containing numeric values that will be used as weights in the layout
            algorithm. Only columns containing numeric values are shown
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param NodeAttribute (string, optional): The name of the node column
            containing numeric values that will be used as weights in the layout
            algorithm. Only columns containing numeric values are shown
        :param nodeList (string, optional): Specifies a list of nodes. The
            keywords all, selected, or unselected can be used to specify nodes
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list of
            COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param singlePartition (string, optional): Don't partition graph before
            layout, only boolean values allowed: true or false
        :param spacing (string, optional): Circle size, in numeric value
        :param verbose: print more

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["EdgeAttribute","network","NodeAttribute","nodeList","singlePartition","spacing"],\
        [EdgeAttribute,network,NodeAttribute,nodeList,singlePartition,spacing])
        response=api(url=self.__url+"/attribute-circle", PARAMS=PARAMS, method="POST", verbose=verbose)

    def attribute_layout(self, EdgeAttribute=None, maxwidth=None, minrad=None, \
    network=None, NodeAttribute=None,nodeList=None, radmult=None, \
    spacingx=None, spacingy=None, verbose=False):
        """

        :param EdgeAttribute (string, optional): The name of the edge column
            containing numeric values that will be used as weights in the layout
                algorithm. Only columns containing numeric values are shown
        :param maxwidth (string, optional): Maximum width of a row, in numeric value
        :param minrad (string, optional): Minimum width of a partition, in
            numeric value
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param NodeAttribute (string, optional): The name of the node column
            containing numeric values that will be used as weights in the layout
            algorithm. Only columns containing numeric values are shown
        :param nodeList (string, optional): Specifies a list of nodes. The
            keywords all, selected, or unselected can be used to specify nodes
            by their selection state. The pattern COLUMN:VALUE sets this parameter
            to any rows that contain the specified column value; if the COLUMN
            prefix is not used, the NAME column is matched by default. A list
            of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
            can be used to match multiple values.
        :param radmult (string, optional): Minimum width of a partition, in
            numeric value
        :param spacingx (string, optional): Horizontal spacing between two
            partitions in a row, in numeric value
        :param spacingy (string, optional): Vertical spacing between the largest
            partitions of two rows, in numeric value
        :param verbose: print more

        """
        network=check_network(self,network,verbose=verbose)
        PARAMS=set_param(["EdgeAttribute","network","NodeAttribute","nodeList","singlePartition","spacing"],\
        [EdgeAttribute, maxwidth, \
        minrad, network, NodeAttribute,nodeList, radmult, \
        spacingx, spacingy])
        response=api(url=self.__url+"/attribute-circle", PARAMS=PARAMS, method="POST", verbose=verbose)


	def circular(self,EdgeAttribute=None,leftEdge=None,network=None,\
    NodeAttribute=None,nodeHorizontalSpacing=None,nodeList=None,\
    nodeVerticalSpacing=None,rightMargin=None,singlePartition=None,topEdge=None,\
    verbose=None):
		"""
		:param EdgeAttribute (string, optional): The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
		:param leftEdge (string, optional): Left edge margin, in numeric value
		:param network (string, optional): Specifies a network by name, or by SUID
			if the prefix SUID: is used. The keyword CURRENT, or a blank value c
			an also be used to specify the current network.
		:param NodeAttribute (string, optional): The name of the node column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
		:param nodeHorizontalSpacing (string, optional): Horizontal spacing between
			 nodes, in numeric value
		:param nodeList (string, optional): Specifies a list of nodes. The keywords
			 all, selected, or unselected can be used to specify nodes by their
			selection state. The pattern COLUMN:VALUE sets this parameter to any
			 rows that contain the specified column value; if the COLUMN prefix
			is not used, the NAME column is matched by default. A list of COLUMN
			:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be
			used to match multiple values.
		:param nodeVerticalSpacing (string, optional): Vertical spacing between nod
			es, in numeric value
		:param rightMargin (string, optional): Right edge margin, in numeric value
		:param singlePartition (string, optional): Don't partition graph before lay
			out; only boolean values are allowed: true or false
		:param topEdge (string, optional): Top edge margin, in numeric value
		"""
		network=check_network(self,network,verbose=verbose)
		PARAMS=set_param(['EdgeAttribute','leftEdge','network','NodeAttribute',\
        'nodeHorizontalSpacing','nodeList','nodeVerticalSpacing','rightMargin',\
        'singlePartition','topEdge'],[EdgeAttribute,leftEdge,network,NodeAttribute,\
        nodeHorizontalSpacing,nodeList,nodeVerticalSpacing,rightMargin,\
        singlePartition,topEdge])
		response=api(url=self.__url+"/circular", PARAMS=PARAMS, method="POST", verbose=verbose)


	def copycat(self,gridUnmapped=None,selectUnmapped=None,sourceColumn=None,\
    sourceNetwork=None,targetColumn=None,targetNetwork=None,verbose=None):
		"""
        Sets the coordinates for each node in the target network to the coordinates
        of a matching node in the source network.
        Optional parameters such as gridUnmapped and selectUnmapped determine
        the behavior of target network nodes that could not be matched.

		:param gridUnmapped (string, optional): If this is set to true, any nodes i
			n the target network that could not be matched to a node in the sour
			ce network will be laid out in a grid
		:param selectUnmapped (string, optional): If this is set to true, any nodes
			 in the target network that could not be matched to a node in the so
			urce network will be selected in the target network
		:param sourceColumn (string): The name of column in the node table used to
			match nodes
		:param sourceNetwork (string): The name of network to get node coordinates
			from
		:param targetColumn (string): The name of column in the node table used to
			match nodes
		:param targetNetwork (string): The name of the network to apply coordinates
			 to.
		"""
		PARAMS=set_param(['gridUnmapped','selectUnmapped','sourceColumn',\
        'sourceNetwork','targetColumn','targetNetwork'],[gridUnmapped,\
        selectUnmapped,sourceColumn,sourceNetwork,targetColumn,targetNetwork])
		response=api(url=self.__url+"/copycat", PARAMS=PARAMS, method="POST", verbose=verbose)


	def cose(self,compoundGravityRange=None,compoundGravityStrength=None,\
    EdgeAttribute=None,gravityRange=None,gravityStrength=None,idealEdgeLength=None,\
    incremental=None,LayoutQuality=None,network=None,NodeAttribute=None,\
    nodeList=None,repulsionStrength=None,smartEdgeLengthCalc=None,\
    smartRepulsionRangeCalc=None,springStrength=None,verbose=None):
		"""
		:param compoundGravityRange (string, optional): Compound gravity range (0-1
			00)
		:param compoundGravityStrength (string, optional): Compound gravity strengt
			h (0-100)
		:param EdgeAttribute (string, optional): The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
		:param gravityRange (string, optional): Gravity range (0-100)
		:param gravityStrength (string, optional): Gravity strength (0-100)
		:param idealEdgeLength (string, optional): Ideal edge length, any positive
			integer
		:param incremental (string, optional): Incremental; whether the algorithm w
			ill be applied incrementally; boolean values only, true or false; de
			faults to false
		:param LayoutQuality (string, optional): Layout quality; allowed values are
			 Proof, Default and Draft = ['Proof', 'Default', 'Draft']
		:param network (string, optional): Specifies a network by name, or by SUID
			if the prefix SUID: is used. The keyword CURRENT, or a blank value c
			an also be used to specify the current network.
		:param NodeAttribute (string, optional): The name of the node column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
		:param nodeList (string, optional): Specifies a list of nodes. The keywords
			 all, selected, or unselected can be used to specify nodes by their
			selection state. The pattern COLUMN:VALUE sets this parameter to any
			 rows that contain the specified column value; if the COLUMN prefix
			is not used, the NAME column is matched by default. A list of COLUMN
			:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be
			used to match multiple values.
		:param repulsionStrength (string, optional): Repulsion strength (0-100)
		:param smartEdgeLengthCalc (string, optional): Use smart edge length calcul
			ation; boolean values only, true or false; defaults to true
		:param smartRepulsionRangeCalc (string, optional): Use smart repulsion rang
			e calculation; boolean values only, true or false; defaults to true
		:param springStrength (string, optional): Spring strength (0-100)
		"""
		network=check_network(self,network,verbose=verbose)
		PARAMS=set_param(['compoundGravityRange','compoundGravityStrength',\
        'EdgeAttribute','gravityRange','gravityStrength','idealEdgeLength',\
        'incremental','LayoutQuality','network','NodeAttribute','nodeList',\
        'repulsionStrength','smartEdgeLengthCalc','smartRepulsionRangeCalc',\
        'springStrength'],[compoundGravityRange,compoundGravityStrength,EdgeAttribute,\
        gravityRange,gravityStrength,idealEdgeLength,incremental,LayoutQuality,\
        network,NodeAttribute,nodeList,repulsionStrength,smartEdgeLengthCalc,\
        smartRepulsionRangeCalc,springStrength])
		response=api(url=self.__url+"/cose", PARAMS=PARAMS, method="POST", verbose=verbose)


	def degree_circle(self,EdgeAttribute=None,network=None,NodeAttribute=None,\
    nodeList=None,singlePartition=None,verbose=None):
		"""
		:param EdgeAttribute (string, optional): The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
		:param network (string, optional): Specifies a network by name, or by SUID
			if the prefix SUID: is used. The keyword CURRENT, or a blank value c
			an also be used to specify the current network.
		:param NodeAttribute (string, optional): The name of the node column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
		:param nodeList (string, optional): Specifies a list of nodes. The keywords
			 all, selected, or unselected can be used to specify nodes by their
			selection state. The pattern COLUMN:VALUE sets this parameter to any
			 rows that contain the specified column value; if the COLUMN prefix
			is not used, the NAME column is matched by default. A list of COLUMN
			:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be
			used to match multiple values.
		:param singlePartition (string, optional): Don't partition graph before lay
			out; boolean values only, true or false; defaults to false
		"""
		network=check_network(self,network,verbose=verbose)
		PARAMS=set_param(['EdgeAttribute','network','NodeAttribute','nodeList',\
        'singlePartition'],[EdgeAttribute,network,NodeAttribute,nodeList,\
        singlePartition])
		response=api(url=self.__url+"/degree-circle", PARAMS=PARAMS, method="POST", verbose=verbose)

	def force_directed(self,defaultEdgeWeight=None,defaultNodeMass=None,defaultSpringCoefficient=None,defaultSpringLength=None,EdgeAttribute=None,isDeterministic=None,maxWeightCutoff=None,minWeightCutoff=None,network=None,NodeAttribute=None,nodeList=None,numIterations=None,singlePartition=None,Type=None,verbose=None):
		"""
		:param defaultEdgeWeight (string, optional): The default edge weight to con
			sider, default is 0.5
		:param defaultNodeMass (string, optional): Default Node Mass, in numeric va
			lue
		:param defaultSpringCoefficient (string, optional): Default Spring Coeffici
			ent, in numeric value
		:param defaultSpringLength (string, optional): Default Spring Length, in nu
			meric value
		:param EdgeAttribute (string, optional): The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
		:param isDeterministic (string, optional): Force deterministic layouts (slo
			wer); boolean values only, true or false; defaults to false
		:param maxWeightCutoff (string, optional): The maximum edge weight to consi
			der, default to the Double.MAX value
		:param minWeightCutoff (string, optional): The minimum edge weight to consi
			der, numeric values, default is 0
		:param network (string, optional): Specifies a network by name, or by SUID
			if the prefix SUID: is used. The keyword CURRENT, or a blank value c
			an also be used to specify the current network.
		:param NodeAttribute (string, optional): The name of the node column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
		:param nodeList (string, optional): Specifies a list of nodes. The keywords
			 all, selected, or unselected can be used to specify nodes by their
			selection state. The pattern COLUMN:VALUE sets this parameter to any
			 rows that contain the specified column value; if the COLUMN prefix
			is not used, the NAME column is matched by default. A list of COLUMN
			:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be
			used to match multiple values.
		:param numIterations (string, optional): Number of Iterations, in numeric v
			alue
		:param singlePartition (string, optional): Don't partition graph before lay
			out; boolean values only, true or false; defaults to false
		:param Type (string, optional): How to interpret weight values; must be one
			 of Heuristic, -Log(value), 1 - normalized value and normalized valu
			e. Defaults to Heuristic = ['Heuristic', '-Log(value)', '1 - normali
			zed value', 'normalized value']
		"""
		network=check_network(self,network,verbose=verbose)
		PARAMS=set_param(['defaultEdgeWeight','defaultNodeMass','defaultSpringCoefficient','defaultSpringLength','EdgeAttribute','isDeterministic','maxWeightCutoff','minWeightCutoff','network','NodeAttribute','nodeList','numIterations','singlePartition','Type'],[defaultEdgeWeight,defaultNodeMass,defaultSpringCoefficient,defaultSpringLength,EdgeAttribute,isDeterministic,maxWeightCutoff,minWeightCutoff,network,NodeAttribute,nodeList,numIterations,singlePartition,Type])
		response=api(url=self.__url+"/force-directed", PARAMS=PARAMS, method="POST", verbose=verbose)


	def force_directed_cl(self,defaultEdgeWeight=None,defaultNodeMass=None,defaultSpringCoefficient=None,defaultSpringLength=None,EdgeAttribute=None,fromScratch=None,isDeterministic=None,maxWeightCutoff=None,minWeightCutoff=None,network=None,NodeAttribute=None,nodeList=None,numIterations=None,numIterationsEdgeRepulsive=None,singlePartition=None,Type=None,verbose=None):
		"""
		:param defaultEdgeWeight (string, optional): The default edge weight to con
			sider, default is 0.5
		:param defaultNodeMass (string, optional):
		:param defaultSpringCoefficient (string, optional):
		:param defaultSpringLength (string, optional):
		:param EdgeAttribute (string, optional): The name of the edge column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
		:param fromScratch (string, optional):
		:param isDeterministic (string, optional):
		:param maxWeightCutoff (string, optional): The maximum edge weight to consi
			der, default to the Double.MAX value
		:param minWeightCutoff (string, optional): The minimum edge weight to consi
			der, numeric values, default is 0
		:param network (string, optional): Specifies a network by name, or by SUID
			if the prefix SUID: is used. The keyword CURRENT, or a blank value c
			an also be used to specify the current network.
		:param NodeAttribute (string, optional): The name of the node column contai
			ning numeric values that will be used as weights in the layout algor
			ithm. Only columns containing numeric values are shown
		:param nodeList (string, optional): Specifies a list of nodes. The keywords
			 all, selected, or unselected can be used to specify nodes by their
			selection state. The pattern COLUMN:VALUE sets this parameter to any
			 rows that contain the specified column value; if the COLUMN prefix
			is not used, the NAME column is matched by default. A list of COLUMN
			:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,... can be
			used to match multiple values.
		:param numIterations (string, optional):
		:param numIterationsEdgeRepulsive (string, optional):
		:param singlePartition (string, optional):
		:param Type (string, optional): How to interpret weight values; must be one
			 of Heuristic, -Log(value), 1 - normalized value and normalized valu
			e. Defaults to Heuristic = ['Heuristic', '-Log(value)', '1 - normali
			zed value', 'normalized value']
		"""
		network=check_network(self,network,verbose=verbose)
		PARAMS=set_param(['defaultEdgeWeight','defaultNodeMass','defaultSpringCoefficient','defaultSpringLength','EdgeAttribute','fromScratch','isDeterministic','maxWeightCutoff','minWeightCutoff','network','NodeAttribute','nodeList','numIterations','numIterationsEdgeRepulsive','singlePartition','Type'],[defaultEdgeWeight,defaultNodeMass,defaultSpringCoefficient,defaultSpringLength,EdgeAttribute,fromScratch,isDeterministic,maxWeightCutoff,minWeightCutoff,network,NodeAttribute,nodeList,numIterations,numIterationsEdgeRepulsive,singlePartition,Type])
		response=api(url=self.__url+"/force-directed-cl", PARAMS=PARAMS, method="POST", verbose=verbose)
