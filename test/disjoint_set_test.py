import unittest

from nose.tools import istest

from data_structures.disjoint_set import DisjointSet


class DisjointSetTest(unittest.TestCase):


    def setUp(self):
        self.ds = DisjointSet()

    @istest
    def add_elements(self):
        self.ds.add(1)
        self.assertEquals(1, len(self.ds))
        self.ds.add('a')
        self.assertEquals(2, len(self.ds))

    @istest
    def add_many_elements(self):
        self.ds.add_many([1, 2, 3])
        self.assertEquals(3, len(self.ds))
        self.ds.add_many(letter for letter in 'abc')
        self.assertEquals(6, len(self.ds))

    @istest
    def island_elements_find_themselves(self):
        test_elements = [1, 2, 3]
        self.ds.add_many(test_elements)
        for element in test_elements:
            self.assertEquals(element, self.ds.find(element))

    @istest
    def union_two_elements(self):
        elements = [1, 2]
        self.ds.add_many(elements)
        self.ds.union(1, 2)
        self.assert_all_elements_unioned(elements)

    @istest
    def add_elements_after_a_union(self):
        elements = [1, 2, 3]
        self.ds.add_many(elements[:2])
        self.ds.union(1, 2)
        self.ds.add(elements[2])
        self.assertEquals(self.ds.find(1), self.ds.find(2))
        self.assertEquals(3, self.ds.find(3))
        self.assertNotEqual(self.ds.find(2), self.ds.find(3))
        self.ds.union(1, 3)
        self.assert_all_elements_unioned(elements)

    @istest
    def transitive_union(self):
        elements = [1, 2, 3]
        self.ds.add_many(elements)
        self.ds.union(1, 2)
        self.ds.union(2, 3)
        self.assert_all_elements_unioned(elements)

    @istest
    def union_order_doesnt_matter(self):
        elements = [1, 2, 3]
        self.ds.add_many(elements)
        self.ds.union(1, 2)
        self.ds.union(3, 2)
        self.assert_all_elements_unioned(elements)

    @istest
    def multistep_unions(self):
        elements = [1, 2, 3, 4, 5, 6]
        self.ds.add_many(elements)
        self.ds.union(1, 2)
        self.ds.union(3, 2)
        self.ds.union(5, 4)

        self.assertNotEqual(self.ds.find(2), self.ds.find(4))
        self.ds.union(4, 3)
        self.assertEqual(self.ds.find(2), self.ds.find(4))

        self.assertNotEqual(self.ds.find(6), self.ds.find(4))
        self.ds.union(6, 2)
        self.assert_all_elements_unioned(elements)

    @istest
    def unioning_joint_elements_has_no_effect(self):
        elements = [1, 2, 3, 4]
        self.ds.add_many(elements)
        self.ds.union(1, 2)
        self.ds.union(3, 4)
        self.ds.union(2, 3)
        self.ds.union(1, 4)
        self.assert_all_elements_unioned(elements)

    def assert_all_elements_unioned(self, elements):
        for a in elements:
            for b in elements:
                self.assertEquals(self.ds.find(a), self.ds.find(b))

