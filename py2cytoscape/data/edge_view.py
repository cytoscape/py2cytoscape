# -*- coding: utf-8 -*-
from py2cytoscape.data.base_view import BaseView
from . import BASE_URL

BASE_URL_NETWORK = BASE_URL + 'networks'

import warnings
warnings.warn('\n\n\n**** data.edge_view will be deprecated in the next py2cytoscape release. ****\n\n\n')

class EdgeView(BaseView):

    # Utility Methods to access node position
    def get_width(self):
        return self.__view['NODE_X_LOCATION']

    def get_color(self):
        return self.__view['NODE_Y_LOCATION']
