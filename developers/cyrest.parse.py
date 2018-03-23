#!/usr/bin/env python

"""
Usage:

./cyrest.parse.py cyparse.txt force-directed-cl
"""

import sys


fin=sys.argv[1]

args=[]
with open(fin, "r") as f:
    for line in f:
        a=line.split(" ")[0]
        args.append(a)
if "network" in args:
    net=True
else:
    net=False

text=""
for a in args:
    text=text+a+"=None,"
texta=text.rstrip(',')

text="["
for a in args:
    text=text+"'"+a+"',"
text=text.rstrip(",")
text=text+"],["
for a in args:
    text=text+a+","
text=text.rstrip(",")
textb=text+"]"


text=[]
with open(fin, "r") as f:
    for line in f:
        l=line.rstrip("\n")
        l=l.rstrip(",")
        chunks, chunk_size = len(l), 68
        l=[ l[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
        l="\n\t\t\t".join(l)
        l="\t\t:param "+l
        text.append(l)
textc="\n".join(text)

fname=sys.argv[3]
nfname=fname.replace(" ","_")
nfname=nfname.replace("-","_")
header='\tdef '+nfname+'(self,'+texta+',verbose=None):'
textd=header+'\n\t\t"""\n'+textc+'\n\t\t"""'

if net:
    text="\n\t\tnetwork=check_network(self,network,verbose=verbose)"
else:
    text=""
textf=text+'\n\t\tPARAMS=set_param('+textb+')\n\t\tresponse=api(url=self.__url+"/'+fname+'", PARAMS=PARAMS, method="POST", verbose=verbose)'

print textd+textf

with open("/Users/jboucas/py2cytoscape/py2cytoscape/cyrest/"+sys.argv[2], "a") as fout:
    fout.write("\n\n"+textd+textf)
