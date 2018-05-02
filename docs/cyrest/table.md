## ***cyclient.table.get_column***

**`cyclient.table.get_column(self,column=None,table=None,verbose=None)`**

Get the information about a table column.

* **`column (string, optional)`** Specifies the name of a column in the tab
			le
* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.
* **`returns`** information about a table column

___

## ***cyclient.table.create_column***

**`cyclient.table.create_column(self,columnName=None,listType=None,table=None,ntype=None,verbose=None)`**

Appends an additional column of attribute values to the current table.

* **`columnName (string, optional)`** The new column name
* **`listType (string, optional)`** Can be one of integer, long, double, or
			 string.
* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.
* **`ntype (string, optional)`** Can be one of integer, long, double, string
			, or list.

___

## ***cyclient.table.import_url***

**`cyclient.table.import_url(self,caseSensitiveNetworkCollectionKeys=None,		caseSensitiveNetworkKeys=None,dataTypeList=None,\		DataTypeTargetForNetworkCollection=None,DataTypeTargetForNetworkList=None,\		delimiters=None,delimitersForDataList=None,firstRowAsColumnNames=None,\		KeyColumnForMapping=None,KeyColumnForMappingNetworkList=None,\		keyColumnIndex=None,newTableName=None,startLoadRow=None,\		TargetNetworkCollection=None,TargetNetworkList=None,url=None,\		WhereImportTable=None,verbose=None)`**

Similar to Import Table this uses a long list of input parameters to
specify the attributes of the table, the mapping keys, and the destination
table for the input.

* **`caseSensitiveNetworkCollectionKeys (string, optional)`** Determines wh
			ether capitalization is considered in matching and sorting
* **`caseSensitiveNetworkKeys (string, optional)`** Determines whether capi
			talization is considered in matching and sorting
* **`dataTypeList (string, optional)`** List of column data types ordered b
			y column index (e.g. "string,int,long,double,boolean,intlist" or jus
			t "s,i,l,d,b,il")
* **`DataTypeTargetForNetworkCollection (string, optional)`** Select whethe
			r to import the data as Node Table Columns, Edge Table Columns, or N
			etwork Table Columns
* **`DataTypeTargetForNetworkList (string, optional)`** The data type of th
			e targets
* **`delimiters (string, optional)`** The list of delimiters that separate
			columns in the table.
* **`delimitersForDataList (string, optional)`** The delimiters between ele
			ments of list columns in the table.
* **`firstRowAsColumnNames (string, optional)`** If the first imported row
			contains column names, set this to true.
* **`KeyColumnForMapping (string, optional)`** The column in the network to
			 use as the merge key
* **`KeyColumnForMappingNetworkList (string, optional)`** The column in the
			 network to use as the merge key
* **`keyColumnIndex (string, optional)`** The column that contains the key
			values for this import. These values will be used to match with the
			key values in the network.
* **`newTableName (string, optional)`** The title of the new table
* **`startLoadRow (string, optional)`** The first row of the input table to
			 load. This allows the skipping of headers that are not part of the
			import.
* **`TargetNetworkCollection (string, optional)`** The network collection t
			o use for the table import
* **`TargetNetworkList (string, optional)`** The list of networks into whic
			h the table is imported
* **`url (string)`** The URL of the file or resource that provides the tabl
			e or network to be imported.
* **`WhereImportTable (string, optional)`** Determines what network(s) the
			imported table will be associated with (if any). A table can be impo
			rted into a Network Collection, Selected networks or to an unassigne
			d table.

___

## ***cyclient.table.list_columns***

**`cyclient.table.list_columns(self,table=None,verbose=None)`**

Returns the list of columns in the table.

* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.
* **`returns`** list of columns in the table.

___

## ***cyclient.table.rename_column***

**`cyclient.table.rename_column(self,columnName=None,newColumnName=None,table=None,verbose=None)`**

Changes the name of a specified column in the table.

* **`columnName (string)`** The name of the column that will be renamed.
* **`newColumnName (string)`** The new name of the column.
* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.

___

## ***cyclient.table.add_row***

**`cyclient.table.add_row(self,keyValue=None,table=None,verbose=None)`**

Appends an additional row of empty cells to the current table.

* **`keyValue (string, optional)`** Specifies the primary key of a value in
			 the row of a table Note that network, node, and edge tables must ha
			ve Long values as keys
* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.

___

## ***cyclient.table.list***

**`cyclient.table.list(self,includePrivate=None,namespace=None,atype=None,verbose=None)`**

Returns a list of the table SUIDs associated with the passed network parameter.

* **`includePrivate (string, optional)`** A boolean value determining wheth
			er to return private as well as public tables
* **`namespace (string, optional)`** An optional argument to contrain outpu
			t to a single namespace, or ALL
* **`atype (string, optional)`** One of ''network'', ''node'', ''edge'', ''u
			nattached'', ''all'', to constrain the type of table listed
* **`returns`** list of the table SUIDs associated with the passed network parameter.

___

## ***cyclient.table.get_value***

**`cyclient.table.get_value(self,column=None,keyValue=None,table=None,verbose=None)`**

Returns the value from a cell as specified by row and column ids.

* **`column (string, optional)`** Specifies the name of a column in the tab
			le
* **`keyValue (string, optional)`** Specifies a row of a table using the pr
			imary key as the indentifier
* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.
* **`returns`** value from a cell as specified by row and column ids


___

## ***cyclient.table.merge***

**`cyclient.table.merge(self,DataTypeTargetForNetworkCollection=None,		dataTypeTargetForNetworkList=None,mergeType=None,SourceMergeColumns=None,\		SourceMergeKey=None,SourceTable=None,TargetKeyNetworkCollection=None,\		TargetMergeKey=None,TargetNetworkCollection=None,TargetNetworkList=None,\		UnassignedTable=None,WhereMergeTable=None,verbose=None)`**

Merge tables together joining around a designated key column. Depending
on the arguments, might merge into multiple local tables.

* **`DataTypeTargetForNetworkCollection (string, optional)`** The collectio
			n of networks where the merged table will reside
* **`dataTypeTargetForNetworkList (string, optional)`** 
* **`mergeType (string, optional)`** A choice between ''Copy Columns'' and
			''Link To Columns'' that determines if replicates are created
* **`SourceMergeColumns (string, optional)`** A list of columns that will b
			e brought into the merged table
* **`SourceMergeKey (string, optional)`** The name of the columns that exis
			ts in both tables and is used to correlate rows
* **`SourceTable (string, optional)`** The name of the table used as the ba
			se data in the merge
* **`TargetKeyNetworkCollection (string, optional)`** The name of the prima
			ry column about which the merge is made
* **`TargetMergeKey (string, optional)`** 
* **`TargetNetworkCollection (string, optional)`** The group of networks th
			at will be merged into the source table
* **`TargetNetworkList (string, optional)`** The list of networks where the
			 merged table will be added
* **`UnassignedTable (string, optional)`** 
* **`WhereMergeTable (string, optional)`** The destination path of the resu
			ltant merged table. The choices are ''Network Collection'', ''Select
			ed Networks'', or ''All Unassigned Tables''.

___

## ***cyclient.table.list_rows***

**`cyclient.table.list_rows(self,rowList=None,table=None,verbose=None)`**

Returns the list of primary keys for each of the rows in the specified table.

* **`rowList (string, optional)`** Specifies a list of rows. The pattern CO
			LUMN:VALUE sets this parameter to any rows that contain the specifie
			d column value; if the COLUMN prefix is not used, the NAME column is
			 matched by default. A list of COLUMN:VALUE pairs of the format COLU
			MN1:VALUE1,COLUMN2:VALUE2,... can be used to match multiple values.
			This parameter can also be set to all to include all rows.
* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.

___

## ***cyclient.table.delete_row***

**`cyclient.table.delete_row(self,keyValue=None,table=None,verbose=None)`**

Deletes a row from a table.Requires the table name or SUID and the row key.

* **`keyValue (string)`** Specifies the primary key of a value in the row o
			f a table
* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.

___

## ***cyclient.table.import_file***

**`cyclient.table.import_file(self,caseSensitiveNetworkCollectionKeys=None,		caseSensitiveNetworkKeys=None,dataTypeList=None,\		DataTypeTargetForNetworkCollection=None,DataTypeTargetForNetworkList=None,\		delimiters=None,delimitersForDataList=None,afile=None,firstRowAsColumnNames=None,\		KeyColumnForMapping=None,KeyColumnForMappingNetworkList=None,keyColumnIndex=None,\		newTableName=None,startLoadRow=None,TargetNetworkCollection=None,\		TargetNetworkList=None,WhereImportTable=None,verbose=None)`**

This uses a long list of input parameters to specify the attributes of
the table, the mapping keys, and the destination table for the input.

* **`caseSensitiveNetworkCollectionKeys (string, optional)`** Determines wh
			ether capitalization is considered in matching and sorting
* **`caseSensitiveNetworkKeys (string, optional)`** Determines whether capi
			talization is considered in matching and sorting
* **`dataTypeList (string, optional)`** List of column data types ordered b
			y column index (e.g. "string,int,long,double,boolean,intlist" or jus
			t "s,i,l,d,b,il")
* **`DataTypeTargetForNetworkCollection (string, optional)`** Select whethe
			r to import the data as Node Table Columns, Edge Table Columns, or N
			etwork Table Columns
* **`DataTypeTargetForNetworkList (string, optional)`** The data type of th
			e targets
* **`delimiters (string, optional)`** The list of delimiters that separate
			columns in the table.
* **`delimitersForDataList (string, optional)`** The delimiters between ele
			ments of list columns in the table.
* **`afile (string)`** The path to the file that contains the table or netwo
			rk to be imported.
* **`firstRowAsColumnNames (string, optional)`** If the first imported row
			contains column names, set this to true.
* **`KeyColumnForMapping (string, optional)`** The column in the network to
			 use as the merge key
* **`KeyColumnForMappingNetworkList (string, optional)`** The column in the
			 network to use as the merge key
* **`keyColumnIndex (string, optional)`** The column that contains the key
			values for this import. These values will be used to match with the
			key values in the network.
* **`newTableName (string, optional)`** The title of the new table
* **`startLoadRow (string, optional)`** The first row of the input table to
			 load. This allows the skipping of headers that are not part of the
			import.
* **`TargetNetworkCollection (string, optional)`** The network collection t
			o use for the table import
* **`TargetNetworkList (string, optional)`** The list of networks into whic
			h the table is imported
* **`WhereImportTable (string, optional)`** Determines what network(s) the
			imported table will be associated with (if any). A table can be impo
			rted into a Network Collection, Selected networks or to an unassigne
			d table.

___

## ***cyclient.table.export***

**`cyclient.table.export(self,options=None,OutputFile=None,table=None,verbose=None)`**

Creates a file with name and writes the table there.

* **`options (string, optional)`** The format of the output file.
* **`OutputFile (string, optional)`** The path of the file to export the ta
			ble to. Note that the file will be overwritten if it exists.
* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.

___

## ***cyclient.table.create_table***

**`cyclient.table.create_table(self,keyColumn=None,keyColumnType=None,title=None,verbose=None)`**

Adds a new table to the network.

* **`keyColumn (string, optional)`** Specifies the name of a column in the
			table
* **`keyColumnType (string, optional)`** The syntactical type of the value
			used in the key
* **`title (string, optional)`** The name of the table used in the current
			network

* **`returns`** table SUID

___

## ***cyclient.table.delete_column***

**`cyclient.table.delete_column(self,column=None,table=None,verbose=None)`**

Remove a column from a table, specified by its name. Returns the name of
the column removed.

* **`column (string, optional)`** Specifies the name of a column in the tab
			le
* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.

___

## ***cyclient.table.set_title***

**`cyclient.table.set_title(self,table=None,title=None,verbose=None)`**

Changes the visible identifier of a single table.

* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.
* **`title (string, optional)`** The name of the table used in the current
			network

___

## ***cyclient.table.destroy***

**`cyclient.table.destroy(self,table=None,verbose=None)`**

Removes the specified table from the network.

* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.

___

## ***cyclient.table.get_row***

**`cyclient.table.get_row(self,keyValue=None,table=None,verbose=None)`**

Returns the values in each column of a row of a table.

* **`keyValue (string, optional)`** Specifies a row of a table using the pr
			imary key as the indentifier
* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.
* **`returns`** values in each column of a row of a table


___

## ***cyclient.table.set_values***

**`cyclient.table.set_values(self,columnName=None,rowList=None,table=None,value=None,verbose=None)`**

Set all the values in the specified list of rows with a single value.

* **`columnName (string, optional)`** Specifies the name of a column in the
			 table
* **`rowList (string, optional)`** Specifies a list of rows. The pattern CO
			LUMN:VALUE sets this parameter to any rows that contain the specifie
			d column value; if the COLUMN prefix is not used, the NAME column is
			 matched by default. A list of COLUMN:VALUE pairs of the format COLU
			MN1:VALUE1,COLUMN2:VALUE2,... can be used to match multiple values.
			This parameter can also be set to all to include all rows.
* **`table (string, optional)`** Specifies a table by table name. If the pr
			efix SUID: is used, the table corresponding the SUID will be returne
			d.
* **`value (string, optional)`** The value to set the columns in the select
			ed rows to. This should be a string value, which will be converted t
			o the appropriate column type.

___

