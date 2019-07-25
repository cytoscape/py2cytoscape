# -*- coding: utf-8 -*-
from py2cytoscape.data.base_view import BaseView

import requests
import json

from . import HEADERS

import warnings
warnings.warn('\n\n\n**** data.node_view will be deprecated in the next py2cytoscape release. ****\n\n\n')


class NodeView(BaseView):

    # Utility Methods to access node position
    def get_x(self):
        return self.get_value('NODE_X_LOCATION')

    def get_y(self):
        return self.get_value('NODE_Y_LOCATION')

    def set_x(self, x):
        self.set_value('NODE_X_LOCATION', x)




