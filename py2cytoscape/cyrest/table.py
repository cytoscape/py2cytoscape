from .base import *
import pandas as pd
import sys

class table(object):
    """
    cytoscape session interface as shown in CyREST's swagger documentation for 'table'.

    :param url: an url of the type 'http://' + host + ':' + str(port) + '/' + version + '/'.
    """

    def __init__(self, url):
        self.__url = url + 'commands/table'
        
    def add_row(self,keyValue=None,table=None,verbose=None):
        """
        Appends an additional row of empty cells to the current table.

        :param keyValue (string, optional): Specifies the primary key of a value in
                the row of a table Note that network, node, and edge tables must ha
            ve Long values as keys
        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        """
        PARAMS=set_param(['keyValue','table'],[keyValue,table])
        response=api(url=self.__url+"/add row", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def create_column(self,columnName=None,listType=None,table=None,ntype=None,verbose=None):
        """
        Appends an additional column of attribute values to the current table.

        :param columnName (string, optional): The new column name
        :param listType (string, optional): Can be one of integer, long, double, or
                string.
        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        :param ntype (string, optional): Can be one of integer, long, double, string
            , or list.
        """
        PARAMS=set_param(['columnName','listType','table','type'],[columnName,\
        listType,table,ntype])
        response=api(url=self.__url+"/create column", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    
    def create_table(self,keyColumn=None,keyColumnType=None,title=None,verbose=None):
        """
        Adds a new table to the network.

        :param keyColumn (string, optional): Specifies the name of a column in the
            table
        :param keyColumnType (string, optional): The syntactical type of the value
            used in the key
        :param title (string, optional): The name of the table used in the current
            network

        :returns: table SUID
        """
        PARAMS=set_param(['keyColumn','keyColumnType','title'],[keyColumn,\
        keyColumnType,title])
        response=api(url=self.__url+"/create table", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def delete_column(self,column=None,table=None,verbose=None):
        """
        Remove a column from a table, specified by its name. Returns the name of
        the column removed.

        :param column (string, optional): Specifies the name of a column in the tab
            le
        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        """
        PARAMS=set_param(['column','table'],[column,table])
        response=api(url=self.__url+"/delete column", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    
    def delete_row(self,keyValue=None,table=None,verbose=None):
        """
        Deletes a row from a table.Requires the table name or SUID and the row key.

        :param keyValue (string): Specifies the primary key of a value in the row o
            f a table
        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        """
        PARAMS=set_param(['keyValue','table'],[keyValue,table])
        response=api(url=self.__url+"/delete row", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    
    def destroy(self,table=None,verbose=None):
        """
        Removes the specified table from the network.

        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        """
        PARAMS=set_param(['table'],[table])
        response=api(url=self.__url+"/destroy", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def export(self,options=None,OutputFile=None,table=None,verbose=None):
        """
        Creates a file with name and writes the table there.

        :param options (string, optional): The format of the output file.
        :param OutputFile (string, optional): The path of the file to export the ta
            ble to. Note that the file will be overwritten if it exists.
        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        """
        PARAMS=set_param(['options','OutputFile','table'],[options,OutputFile,table])
        response=api(url=self.__url+"/export", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def get_column(self,column=None,table=None,verbose=None):
        """
        Get the information about a table column.

        :param column (string, optional): Specifies the name of a column in the tab
            le
        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        :returns: information about a table column
        """
        PARAMS=set_param(['column','table'],[column,table])
        response=api(url=self.__url+"/get column", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def get_row(self,keyValue=None,table=None,verbose=None):
        """
        Returns the values in each column of a row of a table.

        :param keyValue (string, optional): Specifies a row of a table using the pr
            imary key as the indentifier
        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        :returns: values in each column of a row of a table

        """
        PARAMS = set_param(['keyValue','table'],[keyValue,table])
        response=api(url=self.__url+"/get row", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def get_value(self,column=None,keyValue=None,table=None,verbose=None):
        """
        Returns the value from a cell as specified by row and column ids.

        :param column (string, optional): Specifies the name of a column in the tab
            le
        :param keyValue (string, optional): Specifies a row of a table using the pr
            imary key as the indentifier
        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        :returns: value from a cell as specified by row and column ids

        """
        PARAMS=set_param(['column','keyValue','table'],[column,keyValue,table])
        response=api(url=self.__url+"/get value", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def import_file(self,caseSensitiveNetworkCollectionKeys=None,\
        caseSensitiveNetworkKeys=None,dataTypeList=None,\
        DataTypeTargetForNetworkCollection=None,DataTypeTargetForNetworkList=None,\
        delimiters=None,delimitersForDataList=None,afile=None,firstRowAsColumnNames=None,\
        KeyColumnForMapping=None,KeyColumnForMappingNetworkList=None,keyColumnIndex=None,\
        newTableName=None,startLoadRow=None,TargetNetworkCollection=None,\
        TargetNetworkList=None,WhereImportTable=None,verbose=None):
        """
        This uses a long list of input parameters to specify the attributes of
        the table, the mapping keys, and the destination table for the input.

        :param caseSensitiveNetworkCollectionKeys (string, optional): Determines wh
            ether capitalization is considered in matching and sorting
        :param caseSensitiveNetworkKeys (string, optional): Determines whether capi
            talization is considered in matching and sorting
        :param dataTypeList (string, optional): List of column data types ordered b
            y column index (e.g. "string,int,long,double,boolean,intlist" or jus
            t "s,i,l,d,b,il")
        :param DataTypeTargetForNetworkCollection (string, optional): Select whethe
            r to import the data as Node Table Columns, Edge Table Columns, or N
            etwork Table Columns
        :param DataTypeTargetForNetworkList (string, optional): The data type of th
            e targets
        :param delimiters (string, optional): The list of delimiters that separate
            columns in the table.
        :param delimitersForDataList (string, optional): The delimiters between ele
            ments of list columns in the table.
        :param afile (string): The path to the file that contains the table or netwo
            rk to be imported.
        :param firstRowAsColumnNames (string, optional): If the first imported row
            contains column names, set this to true.
        :param KeyColumnForMapping (string, optional): The column in the network to
                use as the merge key
        :param KeyColumnForMappingNetworkList (string, optional): The column in the
                network to use as the merge key
        :param keyColumnIndex (string, optional): The column that contains the key
            values for this import. These values will be used to match with the
            key values in the network.
        :param newTableName (string, optional): The title of the new table
        :param startLoadRow (string, optional): The first row of the input table to
                load. This allows the skipping of headers that are not part of the
            import.
        :param TargetNetworkCollection (string, optional): The network collection t
            o use for the table import
        :param TargetNetworkList (string, optional): The list of networks into whic
            h the table is imported
        :param WhereImportTable (string, optional): Determines what network(s) the
            imported table will be associated with (if any). A table can be impo
            rted into a Network Collection, Selected networks or to an unassigne
            d table.
        """
        PARAMS=set_param(['caseSensitiveNetworkCollectionKeys',\
        'caseSensitiveNetworkKeys','dataTypeList',\
        'DataTypeTargetForNetworkCollection','DataTypeTargetForNetworkList',\
        'delimiters','delimitersForDataList','file','firstRowAsColumnNames',\
        'KeyColumnForMapping','KeyColumnForMappingNetworkList','keyColumnIndex',\
        'newTableName','startLoadRow','TargetNetworkCollection','TargetNetworkList',\
        'WhereImportTable'],[caseSensitiveNetworkCollectionKeys,\
        caseSensitiveNetworkKeys,dataTypeList,DataTypeTargetForNetworkCollection,\
        DataTypeTargetForNetworkList,delimiters,delimitersForDataList,afile,\
        firstRowAsColumnNames,KeyColumnForMapping,KeyColumnForMappingNetworkList,\
        keyColumnIndex,newTableName,startLoadRow,TargetNetworkCollection,\
        TargetNetworkList,WhereImportTable])
        response=api(url=self.__url+"/import file", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def import_url(self,caseSensitiveNetworkCollectionKeys=None,\
        caseSensitiveNetworkKeys=None,dataTypeList=None,\
        DataTypeTargetForNetworkCollection=None,DataTypeTargetForNetworkList=None,\
        delimiters=None,delimitersForDataList=None,firstRowAsColumnNames=None,\
        KeyColumnForMapping=None,KeyColumnForMappingNetworkList=None,\
        keyColumnIndex=None,newTableName=None,startLoadRow=None,\
        TargetNetworkCollection=None,TargetNetworkList=None,url=None,\
        WhereImportTable=None,verbose=None):
        """
        Similar to Import Table this uses a long list of input parameters to
        specify the attributes of the table, the mapping keys, and the destination
        table for the input.

        :param caseSensitiveNetworkCollectionKeys (string, optional): Determines wh
            ether capitalization is considered in matching and sorting
        :param caseSensitiveNetworkKeys (string, optional): Determines whether capi
            talization is considered in matching and sorting
        :param dataTypeList (string, optional): List of column data types ordered b
            y column index (e.g. "string,int,long,double,boolean,intlist" or jus
            t "s,i,l,d,b,il")
        :param DataTypeTargetForNetworkCollection (string, optional): Select whethe
            r to import the data as Node Table Columns, Edge Table Columns, or N
            etwork Table Columns
        :param DataTypeTargetForNetworkList (string, optional): The data type of th
            e targets
        :param delimiters (string, optional): The list of delimiters that separate
            columns in the table.
        :param delimitersForDataList (string, optional): The delimiters between ele
            ments of list columns in the table.
        :param firstRowAsColumnNames (string, optional): If the first imported row
            contains column names, set this to true.
        :param KeyColumnForMapping (string, optional): The column in the network to
                use as the merge key
        :param KeyColumnForMappingNetworkList (string, optional): The column in the
                network to use as the merge key
        :param keyColumnIndex (string, optional): The column that contains the key
            values for this import. These values will be used to match with the
            key values in the network.
        :param newTableName (string, optional): The title of the new table
        :param startLoadRow (string, optional): The first row of the input table to
                load. This allows the skipping of headers that are not part of the
            import.
        :param TargetNetworkCollection (string, optional): The network collection t
            o use for the table import
        :param TargetNetworkList (string, optional): The list of networks into whic
            h the table is imported
        :param url (string): The URL of the file or resource that provides the tabl
            e or network to be imported.
        :param WhereImportTable (string, optional): Determines what network(s) the
            imported table will be associated with (if any). A table can be impo
            rted into a Network Collection, Selected networks or to an unassigne
            d table.
        """
        PARAMS=set_param(['caseSensitiveNetworkCollectionKeys',\
        'caseSensitiveNetworkKeys','dataTypeList','DataTypeTargetForNetworkCollection',\
        'DataTypeTargetForNetworkList','delimiters','delimitersForDataList',\
        'firstRowAsColumnNames','KeyColumnForMapping','KeyColumnForMappingNetworkList',\
        'keyColumnIndex','newTableName','startLoadRow','TargetNetworkCollection',\
        'TargetNetworkList','url','WhereImportTable'],[caseSensitiveNetworkCollectionKeys,\
        caseSensitiveNetworkKeys,dataTypeList,DataTypeTargetForNetworkCollection,\
        DataTypeTargetForNetworkList,delimiters,delimitersForDataList,\
        firstRowAsColumnNames,KeyColumnForMapping,KeyColumnForMappingNetworkList,\
        keyColumnIndex,newTableName,startLoadRow,TargetNetworkCollection,\
        TargetNetworkList,url,WhereImportTable])
        response=api(url=self.__url+"/import url", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def list_tables(self,includePrivate=None,namespace=None,atype=None,verbose=None):
        """
        Returns a list of the table SUIDs associated with the passed network parameter.

        :param includePrivate (string, optional): A boolean value determining wheth
            er to return private as well as public tables
        :param namespace (string, optional): An optional argument to contrain outpu
            t to a single namespace, or ALL
        :param atype (string, optional): One of ''network'', ''node'', ''edge'', ''u
            nattached'', ''all'', to constrain the type of table listed
        :returns: list of the table SUIDs associated with the passed network parameter.
        """
        PARAMS=set_param(['includePrivate','namespace','type'],\
        [includePrivate,namespace,atype])
        response=api(url=self.__url+"/list", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def list_columns(self,table=None,verbose=None):
        """
        Returns the list of columns in the table.

        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        :returns: list of columns in the table.
        """
        PARAMS=set_param(['table'],[table])
        response=api(url=self.__url+"/list columns", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    def list_rows(self,rowList=None,table=None,verbose=None):
        """
        Returns the list of primary keys for each of the rows in the specified table.

        :param rowList (string, optional): Specifies a list of rows. The pattern CO
            LUMN:VALUE sets this parameter to any rows that contain the specifie
            d column value; if the COLUMN prefix is not used, the NAME column is
                matched by default. A list of COLUMN:VALUE pairs of the format COLU
            MN1:VALUE1,COLUMN2:VALUE2,... can be used to match multiple values.
            This parameter can also be set to all to include all rows.
        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        """
        PARAMS=set_param(['rowList','table'],[rowList,table])
        response=api(url=self.__url+"/list rows", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    
    def merge(self,DataTypeTargetForNetworkCollection=None,\
        dataTypeTargetForNetworkList=None,mergeType=None,SourceMergeColumns=None,\
        SourceMergeKey=None,SourceTable=None,TargetKeyNetworkCollection=None,\
        TargetMergeKey=None,TargetNetworkCollection=None,TargetNetworkList=None,\
        UnassignedTable=None,WhereMergeTable=None,verbose=None):
        """
        Merge tables together joining around a designated key column. Depending
        on the arguments, might merge into multiple local tables.

        :param DataTypeTargetForNetworkCollection (string, optional): The collectio
            n of networks where the merged table will reside
        :param dataTypeTargetForNetworkList (string, optional):
        :param mergeType (string, optional): A choice between ''Copy Columns'' and
            ''Link To Columns'' that determines if replicates are created
        :param SourceMergeColumns (string, optional): A list of columns that will b
            e brought into the merged table
        :param SourceMergeKey (string, optional): The name of the columns that exis
            ts in both tables and is used to correlate rows
        :param SourceTable (string, optional): The name of the table used as the ba
            se data in the merge
        :param TargetKeyNetworkCollection (string, optional): The name of the prima
            ry column about which the merge is made
        :param TargetMergeKey (string, optional):
        :param TargetNetworkCollection (string, optional): The group of networks th
            at will be merged into the source table
        :param TargetNetworkList (string, optional): The list of networks where the
                merged table will be added
        :param UnassignedTable (string, optional):
        :param WhereMergeTable (string, optional): The destination path of the resu
            ltant merged table. The choices are ''Network Collection'', ''Select
            ed Networks'', or ''All Unassigned Tables''.
        """
        PARAMS=set_param(['DataTypeTargetForNetworkCollection','dataTypeTargetForNetworkList','mergeType','SourceMergeColumns','SourceMergeKey','SourceTable','TargetKeyNetworkCollection','TargetMergeKey','TargetNetworkCollection','TargetNetworkList','UnassignedTable','WhereMergeTable'],\
        [DataTypeTargetForNetworkCollection,dataTypeTargetForNetworkList,mergeType,SourceMergeColumns,SourceMergeKey,SourceTable,TargetKeyNetworkCollection,TargetMergeKey,TargetNetworkCollection,TargetNetworkList,UnassignedTable,WhereMergeTable])
        response=api(url=self.__url+"/merge", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response



    def rename_column(self,columnName=None,newColumnName=None,table=None,verbose=None):
        """
        Changes the name of a specified column in the table.

        :param columnName (string): The name of the column that will be renamed.
        :param newColumnName (string): The new name of the column.
        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        """
        PARAMS=set_param(['columnName','newColumnName','table'],[columnName,newColumnName,table])
        response=api(url=self.__url+"/rename column", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    
    def set_title(self,table=None,title=None,verbose=None):
        """
        Changes the visible identifier of a single table.

        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        :param title (string, optional): The name of the table used in the current
            network
        """
        PARAMS=set_param(['table','title'],[table,title])
        response=api(url=self.__url+"/set title", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response


    
    def set_values(self,columnName=None,rowList=None,table=None,value=None,verbose=None):
        """
        Set all the values in the specified list of rows with a single value.

        :param columnName (string, optional): Specifies the name of a column in the
                table
        :param rowList (string, optional): Specifies a list of rows. The pattern CO
            LUMN:VALUE sets this parameter to any rows that contain the specifie
            d column value; if the COLUMN prefix is not used, the NAME column is
                matched by default. A list of COLUMN:VALUE pairs of the format COLU
            MN1:VALUE1,COLUMN2:VALUE2,... can be used to match multiple values.
            This parameter can also be set to all to include all rows.
        :param table (string, optional): Specifies a table by table name. If the pr
            efix SUID: is used, the table corresponding the SUID will be returne
            d.
        :param value (string, optional): The value to set the columns in the select
            ed rows to. This should be a string value, which will be converted t
            o the appropriate column type.
        """
        PARAMS=set_param(['columnName','rowList','table','value'],[columnName,rowList,table,value])
        response=api(url=self.__url+"/set values", PARAMS=PARAMS, method="POST", verbose=verbose)
        return response

    def getTable(self, columns=None, table=None, network = "current", namespace='default', verbose=VERBOSE):
        """
        Gets tables from cytoscape.

        :param table: table to retrieve eg. node
        :param columns: columns to retrieve in list format
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param namespace (string, optional): Node, Edge, and Network objects support
            the default, local, and hidden namespaces. Root networks also support the
            shared namespace. Custom namespaces may be specified by Apps.

        :returns: a pandas dataframe
        """

        u=self.__url 
        host=u.split("//")[1].split(":")[0]
        port=u.split(":")[2].split("/")[0]
        version=u.split(":")[2].split("/")[1]

        if type(network) != int:
            network=check_network(self,network,verbose=verbose)
            PARAMS=set_param(["columnList","namespace","network"],["SUID",namespace,network])
            network=api(namespace="network", command="get attribute",PARAMS=PARAMS, host=host,port=str(port),version=version)
            network=network[0]["SUID"]

        df=pd.DataFrame()
        def target(column):
            URL="http://"+str(host)+":"+str(port)+"/v1/networks/"+str(network)+"/tables/"+namespace+table+"/columns/"+column
            if verbose:
                print("'"+URL+"'")
                sys.stdout.flush()
            response = urllib2.urlopen(URL)
            response = response.read()
            colA=json.loads(response)

            col=pd.DataFrame()    
            colHeader=colA["name"]
            colValues=colA["values"]
            col[colHeader]=colValues
            return col

        ncols=["name"]
        for c in columns:
            ncols.append(c.replace(" ","%20") )
        for c in ncols:
            try:
                col=target(c)
                df=pd.concat([df,col],axis=1)
            except:
                print("Could not find "+c)
                sys.stdout.flush()

        df.index=df["name"].tolist()
        df=df.drop(["name"],axis=1)
        return df

    def loadTableData(self, df, df_key='index',table="node", table_key_column = "name", \
        network="current",namespace="default",verbose=False):
        """
        Loads tables into cytoscape.

        :param df: a pandas dataframe to load
        :param df_key: key column in df, default="index"
        :param table: target table, default="node"
        :param table_key_column: table key column, default="name"
        :param network (string, optional): Specifies a network by name, or by
            SUID if the prefix SUID: is used. The keyword CURRENT, or a blank
            value can also be used to specify the current network.
        :param namespace (string, optional): Node, Edge, and Network objects support
            the default, local, and hidden namespaces. Root networks also support the
            shared namespace. Custom namespaces may be specified by Apps.
        :param verbose: print more information

        :returns: output of put request
        """

        u=self.__url 
        host=u.split("//")[1].split(":")[0]
        port=u.split(":")[2].split("/")[0]
        version=u.split(":")[2].split("/")[1]

        if type(network) != int:
            network=check_network(self,network,verbose=verbose)
            
            PARAMS=set_param(["columnList","namespace","network"],["SUID",namespace,network])
            networkID=api(namespace="network", command="get attribute",PARAMS=PARAMS, host=host,port=str(port),version=version)
            
            PARAMS=set_param(["columnList","namespace","network"],["name",namespace,network])
            networkname=api(namespace="network", command="get attribute",PARAMS=PARAMS, host=host,port=str(port),version=version)
                    
            network=networkID[0]["SUID"]
            networkname=networkname[0]["name"]

        tmp=df.copy()
        if df_key!="index":
            tmp.index=tmp[df_key].tolist()
            tmp=tmp.drop([df_key],axis=1)
                
        tablen=networkname+" default node"

        data=[]

        for c in tmp.columns.tolist():
            tmpcol=tmp[[c]].dropna()
            for r in tmpcol.index.tolist():
                cell={}
                cell[str(table_key_column)]=str(r) # {"name":"p53"}
                val=tmpcol.loc[r,c]
                if type(val) != str:
                    val=float(val)
                cell[str(c)]=val
                data.append(cell)


        upload={"key":table_key_column,"dataKey":table_key_column,\
                "data":data}


        URL="http://"+str(host)+":"+str(port)+"/v1/networks/"+str(network)+"/tables/"+namespace+table  
        if verbose:
            print("'"+URL+"'", upload)
            sys.stdout.flush()
        r = requests.put(url = URL, json = upload)
        if verbose:
            print(r)
        checkresponse(r)
        res=r.content
        return res

    def getTableCount(verbose=None):
        """
        Returns the number of global tables.

        :param verbose: print more

        :returns: 200: successful operation
        """

        response=api(url=self.url+'tables/count', method="GET", verbose=verbose, parse_params=False)
        return response
