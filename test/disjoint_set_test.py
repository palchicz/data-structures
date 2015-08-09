import unittest

from nose.tools import istest

from data_structures.disjoint_set import DisjointSet


class DisjointSetTest(unittest.TestCase):


    def setUp(self):
        self.ds = DisjointSet()

    @istest
    def can_add_elements(self):
        self.ds.add(1)
        self.assertEquals(1, len(self.ds))
        self.ds.add('a')
        self.assertEquals(2, len(self.ds))

    @istest
    def can_add_mant_elements(self):
        self.ds.add_many([1, 2, 3])
        self.assertEquals(3, len(self.ds))
        self.ds.add_many(letter for letter in 'abc')
        self.assertEquals(6, len(self.ds))
