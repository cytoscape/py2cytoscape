import pandas as pd
import json


class Table(object):
    """The Table object provides methods for Cytoscape table manipulation"""
    def __init__(self):
        self.df = None
        self.port = None

    def push(self, target_table_name):
        BASE_URL = "http://localhost:" + self.port + "/v1/"
        HEADERS = {'Content-Type': 'application/json'}
        jsontable = json.loads(self.df.to_json(orient="records"))
        print(json.dumps(jsontable, indent=4))

    def set_port(self, port):
        self.port = str(port)

def read(filepath):
    table = Table()
    table.df = pd.read_csv(filepath)

    return table
