import requests


class SessionClient(object):

    def __init__(self, url):
        self.__url = url + 'session'

    def delete(self):
        requests.delete(self.__url)

    def save(self, file_name=None):
        if file_name is None:
            raise ValueError('Session file name is required.')

        post_url = self.__url
        params = {'file': file_name}
        res = requests.post(post_url, params=params)
        return res

    def open(self, file_name=None):
        if file_name is None:
            raise ValueError('Session file name is required.')

        get_url = self.__url
        params = {'file': file_name}
        res = requests.get(get_url, params=params)
        return res
