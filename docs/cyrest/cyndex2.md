## ***cyclient.cyndex2.saveNetworkToNdex***

**`cyclient.cyndex2.saveNetworkToNdex(suid, body, verbose=None)`**

Save a network/collection to NDEx

* **`suid`** Cytoscape Collection/Subnetwork SUID
* **`body`** Properties required to save network to NDEx.
* **`verbose`** print more

* **`returns`** 200: successful operation; 404: Network does not exist

___

## ***cyclient.cyndex2.getAppInfo***

**`cyclient.cyndex2.getAppInfo(verbose=None)`**

App version and other basic information will be provided.

* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.cyndex2.updateCurrentNetworkInNdex***

**`cyclient.cyndex2.updateCurrentNetworkInNdex(body, verbose=None)`**

Update current network's record in NDEx

* **`body`** Properties required to update a network record in NDEx.
* **`verbose`** print more

* **`returns`** 200: successful operation; 404: Network does not exist

___

## ***cyclient.cyndex2.getNetworkSummary***

**`cyclient.cyndex2.getNetworkSummary(suid, verbose=None)`**

Returns summary of collection containing the specified network.

* **`suid`** Cytoscape Collection/Subnetwork SUID
* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.cyndex2.saveCurrentNetworkToNdex***

**`cyclient.cyndex2.saveCurrentNetworkToNdex(body, verbose=None)`**

Save current network/collection to NDEx

* **`body`** Properties required to save current network to NDEx.
* **`verbose`** print more

* **`returns`** 200: successful operation; 404: Current network does not exist

___

## ***cyclient.cyndex2.updateNetworkInNdex***

**`cyclient.cyndex2.updateNetworkInNdex(suid, body, verbose=None)`**

Update an NDEx network.

* **`suid`** Cytoscape Collection/Subnetwork SUID
* **`body`** Properties required to update a network record in NDEx.
* **`verbose`** print more

* **`returns`** 200: successful operation; 404: Network does not exist

___

## ***cyclient.cyndex2.getCurrentNetworkSummary***

**`cyclient.cyndex2.getCurrentNetworkSummary(verbose=None)`**

Returns summary of collection contains current network.

* **`verbose`** print more

* **`returns`** 200: successful operation

___

## ***cyclient.cyndex2.createNetworkFromNdex***

**`cyclient.cyndex2.createNetworkFromNdex(body, verbose=None)`**

Import network(s) from NDEx.

* **`body`** Properties required to import network from NDEx.
* **`verbose`** print more

* **`returns`** 200: successful operation; 404: Network does not exist

___

