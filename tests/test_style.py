# -*- coding: utf-8 -*-

import unittest

from py2cytoscape.data.style import Style
from py2cytoscape.data.cyrest_client import CyRestClient

import pandas as pd

STYLE_NAME = 'style1'


class StyleTests(unittest.TestCase):

    def setUp(self):
        self.client = CyRestClient()
        self.client.style.delete_all()
        styles = self.client.style.get_all()
        self.assertEqual(1, len(styles))

        self.style = self.client.style.create(STYLE_NAME)
        self.assertEqual(STYLE_NAME, self.style.get_name())

    def test_mappings(self):
        print('\n---------- Mappings tests start -----------\n')

        mappings = self.style.get_mappings()
        self.assertIsNotNone(mappings)
        self.assertEqual(list, type(mappings))
        self.assertEqual(0, len(mappings))

        print('\n---------- Mapping tests finished! -----------\n')

    def test_defaults(self):
        print('\n---------- Defaults tests start -----------\n')

        default_style = self.client.style.create('default')
        defs = default_style.get_defaults()
        print(defs)
        self.assertIsNotNone(defs)
        self.assertEqual(pd.Series, type(defs))
        self.assertEqual(103, len(defs))

        defs2 = self.style.get_defaults()
        print(defs2)
        self.assertIsNotNone(defs2)
        self.assertEqual(pd.Series, type(defs2))
        self.assertEqual(103, len(defs2))

        print('\n---------- Defaults tests finished! -----------\n')

    def test_get_defaults(self):
        print('\n---------- GET Defaults tests start -----------\n')

        default_style = self.client.style.create('def2')
        n_label = default_style.get_default('NODE_LABEL')
        n_size = default_style.get_default('NODE_SIZE')
        n_shape = default_style.get_default('NODE_SHAPE')
        e_width = default_style.get_default('EDGE_WIDTH')

        print(n_label)
        # These should be same as VP defaults.
        self.assertEqual(pd.Series, type(n_label))
        self.assertEqual('', n_label.ix['NODE_LABEL'])
        self.assertEqual(50, n_size.ix['NODE_SIZE'])
        self.assertEqual('ELLIPSE', n_shape.ix['NODE_SHAPE'])
        self.assertEqual(1, e_width.ix['EDGE_WIDTH'])

    def test_update_defaults(self):
        print('\n---------- Add Defaults tests start -----------\n')

        default_style = self.client.style.create('default')

        new_defaults = {
            # Node defaults
            'NODE_FILL_COLOR': '#eeeeff',
            'NODE_SIZE': 20,
            'NODE_BORDER_WIDTH': 0,
            'NODE_TRANSPARENCY': 120,
            'NODE_LABEL_COLOR': 'white',

            # Edge defaults
            'EDGE_WIDTH': 9,
            'EDGE_STROKE_UNSELECTED_PAINT': '#aaaaaa',
            'EDGE_LINE_TYPE': 'LONG_DASH',
            'EDGE_TRANSPARENCY': 120,

            # Network defaults
            'NETWORK_BACKGROUND_PAINT': 'black'
        }

        default_style.update_defaults(new_defaults)

        defs = default_style.get_defaults()
        self.assertEqual(20, defs.ix['NODE_SIZE'])
        self.assertEqual('#eeeeff'.upper(), defs.ix['NODE_FILL_COLOR'])
        self.assertEqual(0, defs.ix['NODE_BORDER_WIDTH'])
        self.assertEqual(120, defs.ix['NODE_TRANSPARENCY'])
        self.assertEqual('#FFFFFF', defs.ix['NODE_LABEL_COLOR'])

        self.assertEqual(9, defs.ix['EDGE_WIDTH'])
        self.assertEqual('#aaaaaa'.upper(), defs.ix['EDGE_STROKE_UNSELECTED_PAINT'])
        self.assertEqual('LONG_DASH', defs.ix['EDGE_LINE_TYPE'])
        self.assertEqual(120, defs.ix['EDGE_TRANSPARENCY'])

        # Network defaults
        self.assertEqual('#000000', defs.ix['NETWORK_BACKGROUND_PAINT'])

        print('\n---------- Defaults tests finished! -----------\n')

    def test_passthrough_mappings(self):
        print('---------- Passthrough mmapping tests -----------\n')

        self.style.create_passthrough_mapping(column='name',
                                              col_type='String', vp='NODE_LABEL')
        mappings = self.style.get_mappings()
        self.assertEqual(1, len(mappings))
        pt = self.style.get_mapping('NODE_LABEL')
        print(pt)
        self.assertEqual('passthrough', pt['mappingType'])
        self.assertEqual('NODE_LABEL', pt['visualProperty'])
        self.assertEqual('String', pt['mappingColumnType'])
        self.assertEqual('name', pt['mappingColumn'])

        self.style.delete_mapping(vp='NODE_LABEL')
        mappings = self.style.get_mappings()
        self.assertEqual(0, len(mappings))

        print('---------- Passthrough mapping tests finished! -----------\n')

    def test_discrete_mappings(self):
        print('---------- Discrete mapping tests -----------\n')

        vp = 'EDGE_LINE_TYPE'
        col = 'interaction'

        try:
            self.style.create_discrete_mapping(column=col,
                                           col_type='String',
                                           vp=vp)
        except ValueError as e:
            print(e)
        else:
            raise RuntimeError('This should not happen!!')

        mapping = {
            'pp': 'SOLID',
            'pd': 'LONG_DASH'
        }

        self.style.create_discrete_mapping(column=col,
                                               col_type='String',
                                               vp=vp, mappings=mapping)
        dm = self.style.get_mapping(vp)
        print(dm)
        self.assertEqual('discrete', dm['mappingType'])
        self.assertEqual(vp, dm['visualProperty'])
        self.assertEqual('String', dm['mappingColumnType'])
        self.assertEqual(col, dm['mappingColumn'])
        self.assertIsNotNone(dm['map'])

        dm_map = dm['map']
        for entry in dm_map:
            self.assertTrue(entry['key'] in mapping.keys())
            self.assertEqual(entry['value'], mapping[entry['key']])

        print('---------- Discrete mapping tests finished! -----------\n')
