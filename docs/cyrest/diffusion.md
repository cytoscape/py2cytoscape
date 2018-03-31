## ***cyclient.diffusion.diffuse***

**`cyclient.diffusion.diffuse(self, verbose=False)`**

Diffusion will send the selected network view and its selected nodes to
a web-based REST service to calculate network propagation. Results are
returned and represented by columns in the node table.
Columns are created for each execution of Diffusion and their names are
returned in the response.
The nodes you would like to use as input should be selected. This will
be used to generate the contents of the diffusion_input column, which
represents the query vector and corresponds to h in the diffusion equation.

* **`verbose`** print more


___

## ***cyclient.diffusion.diffuse_advanced***

**`cyclient.diffusion.diffuse_advanced(self, heatColumnName=None, time=None, verbose=False)`**

Diffusion will send the selected network view and its selected nodes to
a web-based REST service to calculate network propagation. Results are
returned and represented by columns in the node table.
Columns are created for each execution of Diffusion and their names are
returned in the response.

* **`heatColumnName (string, optional)`** A node column name intended
to override the default table column 'diffusion_input'. This represents
the query vector and corresponds to h in the diffusion equation. =
['HEKScore', 'JurkatScore', '(Use selected nodes)']
* **`time (string, optional)`** The extent of spread over the network.
This corresponds to t in the diffusion equation.
* **`verbose`** print more

___

