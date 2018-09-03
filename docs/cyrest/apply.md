## ***cyclient.apply.getLayoutParameters***

**`cyclient.apply.getLayoutParameters(algorithmName, verbose=None)`**

Returns all editable parameters for the Layout algorithm specified by the `algorithmName` parameter.

* **`algorithmName`** Name of the Layout algorithm
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.apply.copyCurrentLayout***

**`cyclient.apply.copyCurrentLayout(sourceViewSUID, targetViewSUID, body, verbose=None)`**

Copy one network view layout onto another, setting the node location and view scale to match. This makes visually comparing networks simple.

* **`sourceViewSUID`** Source network view SUID (or "current")
* **`targetViewSUID`** Target network view SUID (or "current")
* **`body`** Clone the specified network view layout onto another network view -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: successful operation; 404: Network View does not exist

___

## ***cyclient.apply.updateLayoutParameters***

**`cyclient.apply.updateLayoutParameters(algorithmName, body, verbose=None)`**

Updates the Layout parameters for the Layout algorithm specified by the `algorithmName` parameter.

* **`algorithmName`** Name of the layout algorithm
* **`body`** A list of Layout Parameters with Values.
* **`verbose`** print more

* **`returns`** default: successful operation

___

## ***cyclient.apply.applyStyle***

**`cyclient.apply.applyStyle(styleName, networkId, verbose=None)`**

Applies the Visual Style specified by the `styleName` parameter to the network specified by the `networkId` parameter.

* **`styleName`** Name of the Visual Style
* **`networkId`** SUID of the Network
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.apply.getCompatibleColumnDataTypes***

**`cyclient.apply.getCompatibleColumnDataTypes(algorithmName, verbose=None)`**

Returns a list of all compatible column data types for the Layout algorithm specified by the `algorithmName` parameter.

* **`algorithmName`** Name of layout algorithm
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.apply.fitContent***

**`cyclient.apply.fitContent(networkId, verbose=None)`**

Fit the first available Network View for the Network specified by the `networkId` parameter to the current window.

* **`networkId`** SUID of the Network
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.apply.getStyleNames***

**`cyclient.apply.getStyleNames(verbose=None)`**

Returns a list of all Visual Style names. Style names may not be unique.

* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.apply.bundleEdge***

**`cyclient.apply.bundleEdge(networkId, verbose=None)`**

Apply edge bundling to the Network specified by the `networkId` parameter. Edge bundling is executed with default parameters; at present, optional parameters are not supported.

* **`networkId`** SUID of the Network
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.apply.getLayout***

**`cyclient.apply.getLayout(algorithmName, verbose=None)`**

Returns all the details, including names, parameters, and compatible column types for the Layout algorithm specified by the `algorithmName` parameter.

* **`algorithmName`** Name of the Layout algorithm
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.apply.layoutList***

**`cyclient.apply.layoutList(verbose=None)`**

Returns all available layouts as a list of layout names.
<h3>Important Note</h3>
This <strong>does not include yFiles layout algorithms</strong>, due to license issues.

* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.apply.applyLayout***

**`cyclient.apply.applyLayout(algorithmName, networkId, column, verbose=None)`**

Applies the Layout specified by the `algorithmName` parameter to the Network specified by the `networkId` parameter. If the Layout is has an option to use a Column, it can be specified by the `column` parameter.

* **`algorithmName`** Name of layout algorithm
* **`networkId`** SUID of the Network
* **`column`** Name of the Column to be used by the Layout -- Not required, can be None
* **`verbose`** print more

* **`returns`** 200: successful operation

___

