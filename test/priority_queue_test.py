import unittest

from nose.tools import istest

from data_structures.priority_queue import PriorityQueue


class PriorityQueueTest(unittest.TestCase):

    def setUp(self):
        self.queue = PriorityQueue()

    @istest
    def starts_at_zero_size(self):
        self.assertEqual(0, len(self.queue))

    @istest
    def can_push_an_elements(self):
        self.queue.push('a')
        self.assertEqual(1, len(self.queue))

    @istest
    def can_push_multiple_elements(self):
        self.queue.push('a')
        self.queue.push('b')
        self.queue.push('c')
        self.assertEqual(3, len(self.queue))

    @istest
    def can_pop_an_element(self):
        expected_element = 'a'
        self.queue.push(expected_element)
        self.assertEqual(expected_element,  self.queue.pop())
        self.assertEqual(0, len(self.queue))

    @istest
    def can_pop_multiple_element(self):
        expected_output = set(['a', 'b', 'c'])
        for item in expected_output:
            self.queue.push(item)
        actual_output = set()
        while self.queue:
            actual_output.add(self.queue.pop())
        self.assertEqual(expected_output,  actual_output)
        self.assertEqual(0, len(self.queue))

    @istest
    def can_pop_items_in_priority_order(self):
        self.queue.push('a', 10)
        self.queue.push('b', 50)
        self.queue.push('c', 1)

        self.assertEqual('c', self.queue.pop())
        self.assertEqual('a', self.queue.pop())
        self.assertEqual('b', self.queue.pop())

    @istest
    def no_priority_defaults_to_lowest_priority(self):
        self.queue.push('a')
        self.queue.push('b', 99)
        self.assertEqual('b', self.queue.pop())
        self.assertEqual('a', self.queue.pop())

    @istest
    def remove_elements(self):
        self.queue.push('a', 9)
        self.queue.push('b', 99)
        self.queue.remove('a')
        self.assertEqual(1, len(self.queue))
        self.assertEqual('b', self.queue.pop())
        self.assertEqual(0, len(self.queue))

    @istest
    def empty_queue_throws_key_error(self):
        with self.assertRaises(KeyError):
            self.queue.pop()
        with self.assertRaises(KeyError):
            self.queue.push('a')
            self.queue.pop()
            self.queue.pop()
        with self.assertRaises(KeyError):
            self.queue.push('b')
            self.queue.remove('b')
            self.queue.pop()

    @istest
    def can_update_priority(self):
        self.queue.push('a', 99)
        self.queue.push('b', 10)
        self.assertEqual(2, len(self.queue))
        self.queue.update('a', 3)
        self.assertEqual(2, len(self.queue))
        self.assertEqual('a', self.queue.pop())
        self.assertEqual('b', self.queue.pop())
        self.assertEqual(0, len(self.queue))
