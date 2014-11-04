import pandas as pd
import json
import requests

class Table(object):
    """The Table object provides methods for Cytoscape table manipulation"""
    def __init__(self):
        self.df = None

    def push(self, port):
        BASE_URL = "http://localhost:" + str(port) + "/v1/"
        HEADERS = {'Content-Type': 'application/json'}
        jsontable = json.loads(self.df.to_json(orient="records"))
        print json.dumps(jsontable, indent=4)

def read(filepath):
    table = Table()
    table.df = pd.read_csv(filepath)

    return table
