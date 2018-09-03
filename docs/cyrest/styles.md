## ***cyclient.styles.getSingleVisualProperty***

**`cyclient.styles.getSingleVisualProperty(visualProperty, verbose=None)`**

Return the Visual Property specified by the `visualProperty` parameter.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`visualProperty`** ID of the Visual Property
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.styles.getDefaultValue***

**`cyclient.styles.getDefaultValue(name, vp, verbose=None)`**

Returns the default value for the Visual Property specified by the `name` and `vp` parameters.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`name`** Name of the Visual Style containing the Visual Property
* **`vp`** Name of the Visual Property
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.styles.getMappings***

**`cyclient.styles.getMappings(name, verbose=None)`**

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

* **`name`** Name of the Visual Style
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.styles.getAllDependencies***

**`cyclient.styles.getAllDependencies(name, verbose=None)`**

Returns the status of all the Visual Property Dependencies.

* **`name`** Name of the Visual Style
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.styles.getStyleCount***

**`cyclient.styles.getStyleCount(verbose=None)`**

Returns the number of Visual Styles available in the current session

* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.styles.updateDependencies***

**`cyclient.styles.updateDependencies(name, body, verbose=None)`**

Sets the value of Visual Property dependencies to the values in the message body.

* **`name`** Name of the Visual Style
* **`body`** A list of dependencies.
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.styles.deleteMapping***

**`cyclient.styles.deleteMapping(name, vpName, verbose=None)`**

Deletes the Visual Property mapping specified by the `vpName` and `name` parameters.

* **`name`** Name of the Visual Style containing the Visual Mapping
* **`vpName`** Name of the Visual Property that the Visual Mapping controls
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.styles.getDefaults***

**`cyclient.styles.getDefaults(name, verbose=None)`**

Returns a list of all the default values for the Visual Style specified by the `name` parameter.

* **`name`** Name of the Visual Style
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.styles.getVisualProperties***

**`cyclient.styles.getVisualProperties(verbose=None)`**

Get all available Visual Properties.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.styles.updateStyleName***

**`cyclient.styles.updateStyleName(name, body, verbose=None)`**

Updates the name of the Visual Style specified by the `name` parameter.

* **`name`** Original name of the Visual Style
* **`body`** A new name for the Visual Style.
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.styles.deleteStyle***

**`cyclient.styles.deleteStyle(name, verbose=None)`**

Deletes the Visual Style specified by the `name` parameter.

* **`name`** Visual Style Name
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.styles.deleteAllStyles***

**`cyclient.styles.deleteAllStyles(verbose=None)`**

Deletes all vision styles except for default style

* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.styles.updateMapping***

**`cyclient.styles.updateMapping(name, vp, body, verbose=None)`**

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

* **`name`** Name of the Visual Style containing the Visual Mapping
* **`vp`** Name of the Visual Property that the Visual Mapping controls
* **`body`** A list of new mappings.
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.styles.getStyle***

**`cyclient.styles.getStyle(name, verbose=None)`**

Visual Style in [Cytoscape.js CSS](http://js.cytoscape.org/#style) format.

* **`name`** Name of the Visual Style
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.styles.getStyleNames***

**`cyclient.styles.getStyleNames(verbose=None)`**

Returns a list of all the Visual Style names in the current session.

* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.styles.createStyle***

**`cyclient.styles.createStyle(body, verbose=None)`**

Creates a new Visual Style using the message body.
Returns the title of the new Visual Style. If the title of the Visual Style already existed in the session, a new one will be automatically generated and returned.

* **`body`** The details of the new Visual Style to be created.
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.styles.getStyleFull***

**`cyclient.styles.getStyleFull(name, verbose=None)`**

Returns the Visual Style specified by the `name` parameter.

* **`name`** Name of the Visual Style
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.styles.getMapping***

**`cyclient.styles.getMapping(name, vp, verbose=None)`**

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

* **`name`** Name of the Visual Style containing the Visual Property mapping
* **`vp`** Name of the Visual Property that the Visual Mapping controls
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.styles.updateDefaults***

**`cyclient.styles.updateDefaults(name, body, verbose=None)`**

Updates the default values for the Visual Properties in the Visual Style specified by the `name` parameter.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`name`** Name of the Visual Style
* **`body`** A list of Visual Property values to update.
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.styles.createMappings***

**`cyclient.styles.createMappings(name, body, verbose=None)`**

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

* **`name`** Name of the Visual Style
* **`body`** A list of new mappings.
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.styles.getRangeValues***

**`cyclient.styles.getRangeValues(vp, verbose=None)`**

Returns a list of all available values for the Visual Property specified by the `vp` parameter.
This method is only for Visual Properties with a Discrete Range, such as NODE_SHAPE or EDGE_LINE_TYPE.
Additional details on common Visual Properties can be found in the [Basic Visual Lexicon JavaDoc API](http://chianti.ucsd.edu/cytoscape-3.6.1/API/org/cytoscape/view/presentation/property/BasicVisualLexicon.html)

* **`vp`** ID of the Visual Property
* **`verbose`** print more

* **`returns`** 200: successful operation

___

