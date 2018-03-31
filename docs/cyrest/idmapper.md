## ***cyclient.idmapper.map_column***

**`cyclient.idmapper.map_column(self, only_use_one=None, source_column=None, species=None, target_selection= None, verbose=False)`**

Uses the BridgeDB service to look up analogous identifiers from a wide
selection of other databases

* **`only_use_one (string, optional)`** When multiple identifiers can be
mapped from a single term, this forces a singular result
* **`source_column (string)`** Specifies the column nmae where the
source identifiers are located = ['']
* **`source_selection (string)`** Specifies the database describing
the existing identifiers = ['']
* **`species (string, optional)`** The combined common or latin name of
the species to which the identifiers apply = ['Human (Homo sapiens)',
'Mouse (Mus musculus)', 'Rat (Rattus norvegicus)', 'Frog (Xenopus tropicalis)',
'Zebra fish (Danio rerio)', 'Fruit fly (Drosophila melanogaster)',
'Mosquito (Anopheles gambiae)', 'Arabidopsis thaliana (Arabidopsis thaliana)',
'Yeast (Saccharomyces cerevisiae)', 'E. coli (Escherichia coli)',
'Tuberculosis (Mycobacterium tuberculosis)', 'Worm (Caenorhabditis elegans)']
* **`target_selection (string)`** Specifies the database identifiers to be looked up = ['']
* **`verbose`** print more

* **`returns`** eg. { "new column": "SGD " }

___

