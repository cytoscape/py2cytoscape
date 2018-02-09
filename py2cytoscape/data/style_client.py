# -*- coding: utf-8 -*-

import requests
import json

from . import HEADERS, SUID_LIST
from .style import Style


class StyleClient(object):

    def __init__(self, url):
        self.__url = url + 'styles'
        self.__url_apply = url + 'apply/styles/'

        self.vps = VisualProperties(url)

    def create(self, name=None, original_style=None):
        if name is None:
            raise ValueError('Name is required.')

        existing_styles = requests.get(self.__url).json()

        if name in existing_styles:
            return Style(name)
            
        if original_style is None:
            style = {
                'title': name,
                'defaults': [],
                'mappings': []
            }
        else:
            style = original_style
            style['title'] = name
            
        new_style_name = requests.post(self.__url, data=json.dumps(style), headers=HEADERS).json()['title']
        return Style(name=new_style_name)

    def get_all(self):
        """
        Get list of all available styles.

        :return: List of style names
        """
        return requests.get(self.__url).json()

    def get(self, name, data_format='cy3'):
        if name is None:
            raise ValueError('Style name is required.')

        url = self.__url + '/' + name
        if data_format == 'cytoscapejs':
            url = url + '.json'
            return requests.get(url).json()[0]
        else:
            return requests.get(url).json()

    def apply(self, style, network=None):
        if network is None:
            raise ValueError('Target network is required')

        url = self.__url_apply + style.get_name() + '/' + str(network.get_id())
        requests.get(url)

    def delete(self, style):
        requests.delete(self.__url + '/' + style.get_name())

    def delete_all(self):
        requests.delete(self.__url)


class VisualProperties(object):

    def __init__(self, url):
        self.__url = url + 'styles/visualproperties'
        self.__convert_to_dict()

    def __convert_to_dict(self):
        vps = requests.get(self.__url).json()
        vp_dict = {}
        node_vps = []
        edge_vps = []
        network_vps = []

        for vp in vps:
            id = vp['visualProperty']
            name = vp['name']
            target_type = vp['targetDataType']
            if target_type == 'CyNode':
                node_vps.append(id)
            elif target_type == 'CyEdge':
                edge_vps.append(id)
            elif target_type == 'CyNetwork':
                network_vps.append(id)

            vp_dict[id] = name

        self.__vps = vp_dict
        self.__node_vp = tuple(node_vps)
        self.__edge_vp = tuple(edge_vps)
        self.__network_vp = tuple(network_vps)

    def get_all(self):
        return self.__vps

    def get_node_visual_props(self):
        return self.__node_vp

    def get_edge_visual_props(self):
        return self.__edge_vp

    def get_network_visual_props(self):
        return self.__network_vp




