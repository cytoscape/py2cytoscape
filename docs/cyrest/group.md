## ***cyclient.group.rename***

**`cyclient.group.rename(self, groupName=None, network=None, newName=None, verbose=False)`**

Changes the name of the selected group or groups.

* **`groupName (string, optional)`** Specifies the name used to identify
the group.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`newName (string, optional)`** Specifies the NEW name used to
identify the group.
* **`verbose`** print more

___

## ***cyclient.group.collapse***

**`cyclient.group.collapse(self, groupList=None, network=None, verbose=False)`**

Replaces the representation of all of the nodes and edges in a group with a single node.

* **`groupList (string, optional)`** Specifies a list of groups. The
keywords all, selected, or unselected can be used to specify groups
by their selection state.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`verbose`** print more


___

## ***cyclient.group.get***

**`cyclient.group.get(self, network=None, node=None, verbose=False)`**

Get a group by providing a network and the group node identifier.

* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`node (string, optional)`** Selects a node by name, or, if the
parameter has the prefix suid:, selects a node by SUID.
* **`verbose`** print more

___

## ***cyclient.group.create***

**`cyclient.group.create(self, groupName=None, network=None, nodeList=None, verbose=False)`**

Create a group from the specified nodes.

* **`groupName (string, optional)`** Specifies the name used to identify
the group.
* **`network (string, optional)`** Specifies a network by name, or
by SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`nodeList (string, optional)`** Specifies a list of nodes. The
keywords all, selected, or unselected can be used to specify nodes
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list of
COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`verbose`** print more

:return: SUID of created group


___

## ***cyclient.group.list***

**`cyclient.group.list(self, network=None, verbose=False)`**

Lists the SUIDs of all of the groups in a network.

* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be to specify the current network.
* **`verbose`** print more

* **`returns`** eg. [ 3545 ]

___

## ***cyclient.group.remove***

**`cyclient.group.remove(self, edgeList=None, groupName=None, network=None, nodeList=None, verbose=False)`**

Remove the selected nodes and edges from their current group.

* **`edgeList (string, optional)`** Specifies a list of edges. The
keywords all, selected, or unselected can be used to specify edges
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list
of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`groupName (string, optional)`** Specifies the name used to identify
the group.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`nodeList (string, optional)`** Specifies a list of nodes. The
keywords all, selected, or unselected can be used to specify nodes
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list
of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`verbose`** print more

___

## ***cyclient.group.add***

**`cyclient.group.add(self, edgeList=None, groupName=None, network=None, nodeList=None, verbose=False)`**

Adds the specified nodes and edges to the specified group.

* **`edgeList (string, optional)`** Specifies a list of edges. The
keywords all, selected, or unselected can be used to specify edges
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list
of COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`groupName (string, optional)`** Specifies the name used to
identify the group.
* **`network (string, optional)`** Specifies a network by name, or
by SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`nodeList (string, optional)`** Specifies a list of nodes. The
keywords all, selected, or unselected can be used to specify nodes
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list of
COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`verbose`** print more


___

## ***cyclient.group.ungroup***

**`cyclient.group.ungroup(self, network=None, nodeList=None, verbose=False)`**

Ungroups one or more groups, expanding them if they are collapsed and removing the group nodes.

* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`nodeList (string, optional)`** Specifies a list of nodes. The
keywords all, selected, or unselected can be used to specify nodes
by their selection state. The pattern COLUMN:VALUE sets this parameter
to any rows that contain the specified column value; if the COLUMN
prefix is not used, the NAME column is matched by default. A list of
COLUMN:VALUE pairs of the format COLUMN1:VALUE1,COLUMN2:VALUE2,...
can be used to match multiple values.
* **`verbose`** print more

___

## ***cyclient.group.expand***

**`cyclient.group.expand(self, groupList=None, network=None, verbose=False)`**

Replaces the group node with member nodes for a set of groups.

* **`groupList (string, optional)`** Specifies a list of groups. The
keywords all, selected, or unselected can be used to specify groups
by their selection state.
* **`network (string, optional)`** Specifies a network by name, or by
SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
value can also be used to specify the current network.
* **`verbose`** print more


___

