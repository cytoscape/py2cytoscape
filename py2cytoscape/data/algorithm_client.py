import requests

HEADERS = {'Content-Type': 'application/json'}


class LayoutClient(object):
    def __init__(self, url):
        self.__url = url + 'apply/layouts'
        self.__base_url = url

    def get_all(self):
        return requests.get(self.__url).json()

    def apply(self, name='force-directed', network=None):
        if network is None:
            raise ValueError('Target network is required')

        url = self.__url + '/' + name + '/' + str(network.get_id())
        requests.get(url)

    def bundle_edge(self, network=None):
        if network is None:
            raise ValueError('Target network is required')

        url = self.__base_url + 'apply/edgebundling/' + str(network.get_id())
        requests.get(url)

    def fit(self, network=None):
        if network is None:
            raise ValueError('Target network is required')
        url = self.__base_url + 'apply/fit/' + str(network.get_id())
        requests.get(url)

    def apply_from_presets(self, network=None, positions=None):
        if network is None:
            raise ValueError('Target network is required')

        views = network.get_views()
        view_id = views[0]

        manual_layout_url = self.__base_url +  'networks/' \
                            + str(network.get_id()) \
                            + '/views/' \
                            + str(view_id) + '/nodes'
        pos = self.__apply_preset(locations=positions)

        return requests.put(manual_layout_url, json=pos, headers=HEADERS)

    def __apply_preset(self, locations):
        position_list = []
        for location in locations:
            position = {
                'SUID': location[0],
                'view': [
                    {
                        'visualProperty': 'NODE_X_LOCATION',
                        'value': location[1]
                    },
                    {
                        'visualProperty': 'NODE_Y_LOCATION',
                        'value': location[2]
                    }
                ]
            }
            position_list.append(position)
        return position_list


class EdgeBundlingClient(object):
    def __init__(self, url):
        self.__url = url + 'apply/edgebundling'

    def apply(self, network=None):
        if network is None:
            raise ValueError('Target network is required')

        url = self.__url + '/' + str(network.get_id())
        requests.get(url)
