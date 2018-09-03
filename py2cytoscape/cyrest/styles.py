from .base import *

class styles(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/styles'


    def updateDefaults(name, body, verbose=None):
        """
        Updates the default values for the Visual Properties in the Visual Style specified by the `name` parameter.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param name: Name of the Visual Style
        :param body: A list of Visual Property values to update.
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'/defaults', method="PUT", body=body, verbose=verbose)
        return response


    def getDefaults(name, verbose=None):
        """
        Returns a list of all the default values for the Visual Style specified by the `name` parameter.

        :param name: Name of the Visual Style
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'/defaults', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def getSingleVisualProperty(visualProperty, verbose=None):
        """
        Return the Visual Property specified by the `visualProperty` parameter.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param visualProperty: ID of the Visual Property
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'styles/visualproperties/'+str(visualProperty)+'', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def createStyle(body, verbose=None):
        """
        Creates a new Visual Style using the message body.
        
        Returns the title of the new Visual Style. If the title of the Visual Style already existed in the session, a new one will be automatically generated and returned.

        :param body: The details of the new Visual Style to be created.
        :param verbose: print more

        :returns: 200: successful operation
        """

        PARAMS=set_param(['body'],[body])
        response=api(url=self.url+'styles', PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def deleteAllStyles(verbose=None):
        """
        Deletes all vision styles except for default style

        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.url+'styles', method="DELETE", verbose=verbose)
        return response


    def getStyleNames(verbose=None):
        """
        Returns a list of all the Visual Style names in the current session.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'styles', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def updateDependencies(name, body, verbose=None):
        """
        Sets the value of Visual Property dependencies to the values in the message body.

        :param name: Name of the Visual Style
        :param body: A list of dependencies.
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'/dependencies', method="PUT", body=body, verbose=verbose)
        return response


    def getAllDependencies(name, verbose=None):
        """
        Returns the status of all the Visual Property Dependencies.

        :param name: Name of the Visual Style
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'/dependencies', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def getStyle(name, verbose=None):
        """
        Visual Style in [Cytoscape.js CSS](http://js.cytoscape.org/#style) format.

        :param name: Name of the Visual Style
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'.json', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def getStyleCount(verbose=None):
        """
        Returns the number of Visual Styles available in the current session

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'styles/count', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def deleteMapping(name, vpName, verbose=None):
        """
        Deletes the Visual Property mapping specified by the `vpName` and `name` parameters.

        :param name: Name of the Visual Style containing the Visual Mapping
        :param vpName: Name of the Visual Property that the Visual Mapping controls
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'/mappings/'+str(vpName)+'', method="DELETE", verbose=verbose)
        return response


    def getRangeValues(vp, verbose=None):
        """
        Returns a list of all available values for the Visual Property specified by the `vp` parameter.
        
        This method is only for Visual Properties with a Discrete Range, such as NODE_SHAPE or EDGE_LINE_TYPE.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param vp: ID of the Visual Property
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'styles/visualproperties/'+str(vp)+'/values', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def updateStyleName(name, body, verbose=None):
        """
        Updates the name of the Visual Style specified by the `name` parameter.

        :param name: Original name of the Visual Style
        :param body: A new name for the Visual Style.
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'', method="PUT", body=body, verbose=verbose)
        return response


    def deleteStyle(name, verbose=None):
        """
        Deletes the Visual Style specified by the `name` parameter.

        :param name: Visual Style Name
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'', method="DELETE", verbose=verbose)
        return response


    def getStyleFull(name, verbose=None):
        """
        Returns the Visual Style specified by the `name` parameter.

        :param name: Name of the Visual Style
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def createMappings(name, body, verbose=None):
        """
        Create a new Visual Mapping function and add it to the Visual Style specified by the `name` parameter. Existing mappings in the Visual Style will be overidden by the new mappings created.
        
        The types of mapping available in Cytoscape are explained in depth [here](http://manual.cytoscape.org/en/stable/Styles.html#how-mappings-work). An example of the data format for each is included below. For additional details, such as what Visual Properties supported by each Mapping, click on the relevant JavaDoc API link.
        
        #### Discrete Mapping
        [JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/vizmap/mappings/DiscreteMapping.html)
        ```
        { "mappingType": "discrete",
        "mappingColumn": "interaction",
            "mappingColumnType": "String",
            "visualProperty": "EDGE_WIDTH", 
            "map": [
            { "key" : "pd",
                "value" : "20"
            },
            { "key" : "pp",
                "value" : "1.5"
            }
            ]
        }```
        #### Continuous Mapping
        [JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/vizmap/mappings/ContinuousMapping.html)
        ```
        { "mappingType": "continuous",
        "mappingColumn": "Degree",
        "mappingColumnType": "Integer",
        "visualProperty": "NODE_SIZE",
        "points": [
            { "value" : 1,
                "lesser" : "20",
                "equal" : "20",
                "greater" : "20"
            },
                { "value" : 20,
                "lesser" : "120",
                "equal" : "120",
                "greater" : "220"      }
            ]
        }```
        #### Passthrough Mapping
        [JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/vizmap/mappings/PassthroughMapping.html)
        ```
        { "mappingType": "passthrough",
        "mappingColumn": "name",
        "mappingColumnType": "String",
        "visualProperty": "EDGE_LABEL" 
        }```
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param name: Name of the Visual Style
        :param body: A list of new mappings.
        :param verbose: print more

        :returns: default: successful operation
        """

        PARAMS=set_param(['name','body'],[name,body])
        response=api(url=self.url+'styles/'+str(name)+'/mappings', PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def getMappings(name, verbose=None):
        """
        Returns a list of all Visual Mappings used in the Visual Style specified by the `name` parameter.
        
        The types of mapping available in Cytoscape are explained in depth [here](http://manual.cytoscape.org/en/stable/Styles.html#how-mappings-work). An example of the data format for each is included below. For additional details, such as what Visual Properties supported by each Mapping, click on the relevant JavaDoc API link.
        
        #### Discrete Mapping
        [JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/vizmap/mappings/DiscreteMapping.html)
        ```
        { "mappingType": "discrete",
        "mappingColumn": "interaction",
            "mappingColumnType": "String",
            "visualProperty": "EDGE_WIDTH", 
            "map": [
            { "key" : "pd",
                "value" : "20"
            },
            { "key" : "pp",
                "value" : "1.5"
            }
            ]
        }```
        #### Continuous Mapping
        [JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/vizmap/mappings/ContinuousMapping.html)
        ```
        { "mappingType": "continuous",
        "mappingColumn": "Degree",
        "mappingColumnType": "Integer",
        "visualProperty": "NODE_SIZE",
        "points": [
            { "value" : 1,
                "lesser" : "20",
                "equal" : "20",
                "greater" : "20"
            },
                { "value" : 20,
                "lesser" : "120",
                "equal" : "120",
                "greater" : "220"      }
            ]
        }```
        #### Passthrough Mapping
        [JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/vizmap/mappings/PassthroughMapping.html)
        ```
        { "mappingType": "passthrough",
        "mappingColumn": "name",
        "mappingColumnType": "String",
        "visualProperty": "EDGE_LABEL" 
        }```
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param name: Name of the Visual Style
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'/mappings', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def getVisualProperties(verbose=None):
        """
        Get all available Visual Properties.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'styles/visualproperties', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def updateMapping(name, vp, body, verbose=None):
        """
        Update the visual mapping specified by the `name` and `vp` parameters.
        
        The types of mapping available in Cytoscape are explained in depth [here](http://manual.cytoscape.org/en/stable/Styles.html#how-mappings-work). An example of the data format for each is included below. For additional details, such as what Visual Properties supported by each Mapping, click on the relevant JavaDoc API link.
        
        #### Discrete Mapping
        [JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/vizmap/mappings/DiscreteMapping.html)
        ```
        { "mappingType": "discrete",
        "mappingColumn": "interaction",
            "mappingColumnType": "String",
            "visualProperty": "EDGE_WIDTH", 
            "map": [
            { "key" : "pd",
                "value" : "20"
            },
            { "key" : "pp",
                "value" : "1.5"
            }
            ]
        }```
        #### Continuous Mapping
        [JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/vizmap/mappings/ContinuousMapping.html)
        ```
        { "mappingType": "continuous",
        "mappingColumn": "Degree",
        "mappingColumnType": "Integer",
        "visualProperty": "NODE_SIZE",
        "points": [
            { "value" : 1,
                "lesser" : "20",
                "equal" : "20",
                "greater" : "20"
            },
                { "value" : 20,
                "lesser" : "120",
                "equal" : "120",
                "greater" : "220"      }
            ]
        }```
        #### Passthrough Mapping
        [JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/vizmap/mappings/PassthroughMapping.html)
        ```
        { "mappingType": "passthrough",
        "mappingColumn": "name",
        "mappingColumnType": "String",
        "visualProperty": "EDGE_LABEL" 
        }```
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param name: Name of the Visual Style containing the Visual Mapping
        :param vp: Name of the Visual Property that the Visual Mapping controls
        :param body: A list of new mappings.
        :param verbose: print more

        :returns: default: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'/mappings/'+str(vp)+'', method="PUT", body=body, verbose=verbose)
        return response


    def getMapping(name, vp, verbose=None):
        """
        Returns the Visual Mapping assigned to the Visual Property specified by the `name` and `vp` parameters.
        
        The types of mapping available in Cytoscape are explained in depth [here](http://manual.cytoscape.org/en/stable/Styles.html#how-mappings-work). An example of the data format for each is included below. For additional details, such as what Visual Properties supported by each Mapping, click on the relevant JavaDoc API link.
        
        #### Discrete Mapping
        [JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/vizmap/mappings/DiscreteMapping.html)
        ```
        { "mappingType": "discrete",
        "mappingColumn": "interaction",
            "mappingColumnType": "String",
            "visualProperty": "EDGE_WIDTH", 
            "map": [
            { "key" : "pd",
                "value" : "20"
            },
            { "key" : "pp",
                "value" : "1.5"
            }
            ]
        }```
        #### Continuous Mapping
        [JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/vizmap/mappings/ContinuousMapping.html)
        ```
        { "mappingType": "continuous",
        "mappingColumn": "Degree",
        "mappingColumnType": "Integer",
        "visualProperty": "NODE_SIZE",
        "points": [
            { "value" : 1,
                "lesser" : "20",
                "equal" : "20",
                "greater" : "20"
            },
                { "value" : 20,
                "lesser" : "120",
                "equal" : "120",
                "greater" : "220"      }
            ]
        }```
        #### Passthrough Mapping
        [JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/vizmap/mappings/PassthroughMapping.html)
        ```
        { "mappingType": "passthrough",
        "mappingColumn": "name",
        "mappingColumnType": "String",
        "visualProperty": "EDGE_LABEL" 
        }```
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param name: Name of the Visual Style containing the Visual Property mapping
        :param vp: Name of the Visual Property that the Visual Mapping controls
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'/mappings/'+str(vp)+'', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    def getDefaultValue(name, vp, verbose=None):
        """
        Returns the default value for the Visual Property specified by the `name` and `vp` parameters.
        
        Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

        :param name: Name of the Visual Style containing the Visual Property
        :param vp: Name of the Visual Property
        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'styles/'+str(name)+'/defaults/'+str(vp)+'', PARAMS=None, method="GET", verbose=verbose, parse_params=False)
        return response


    