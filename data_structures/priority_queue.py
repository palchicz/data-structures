from collections import namedtuple
import heapq
import sys

_REMOVED = object()

class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.nodes = {}

    def __len__(self):
        return len(self.nodes)

    def push(self, element, priority=sys.maxsize):
        node = [priority, element]
        self.nodes[element] = node
        heapq.heappush(self.heap, node)

    def pop(self):
        while self.heap:
            _, element = heapq.heappop(self.heap)
            if element is not _REMOVED:
                del self.nodes[element]
                return element
        raise KeyError('pop from an empty priority queue')

    def update(self, element, priority):
        self.remove(element)
        self.push(element, priority)

    def remove(self, element):
        node = self.nodes.pop(element)
        node[1] = _REMOVED
