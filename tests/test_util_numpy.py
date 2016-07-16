from py2cytoscape.util import util_numpy as util

import numpy as np

import unittest

class UtilNumpyTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_from_np(self):
        print('\n---------- NumPy util tests start -----------\n')

        b_mat1 = np.identity(10)
        b_mat2 = np.random.randint(2, size=(10, 10))
        b_mat3 = np.random.randn(100, 100)

        print(b_mat1)
        print(b_mat2)
        print(b_mat3)

        for x in np.nditer(b_mat3, op_flags=['readwrite']):
            val = np.random.randint(2)
            if val == 0:
                x[...] = np.nan

        print(b_mat3)

        g3_str_names = []
        g3_labels = list(range(0, 100))
        for k in g3_labels:
            g3_str_names.append('Node ' + str(k))

        print(g3_str_names)

        g1 = util.from_ndarray(b_mat1, name="Matrix 1")
        g2 = util.from_ndarray(b_mat2, name="Matrix 2")
        g3 = util.from_ndarray(b_mat3, name="Matrix 3", weighted=True,
                               labels=g3_str_names)

        self.assertEqual(10, len(g1['elements']['nodes']))
        self.assertEqual(10, len(g2['elements']['nodes']))
        self.assertEqual(100, len(g3['elements']['nodes']))
        print(g1)
        print(g2)
        print(g3['elements']['nodes'][0])
