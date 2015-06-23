
import requests

class SessionClient(object):

    def __init__(self, url):
        self.__url = url + 'session'

    def delete(self):
        requests.delete(self.__url)

    def save(self, file_name=None):
        pass

    def load(self, file_name=None):
        pass