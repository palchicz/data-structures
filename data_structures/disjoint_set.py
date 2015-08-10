class DisjointSet():


    def __init__(self):
        self._parent = {}


    def add(self, element):
        self._parent[element] = element


    def add_many(self, elements):
        for element in elements:
            self.add(element)


    def find(self, element):
        set_identifier = element
        while self._parent[set_identifier] != set_identifier:
            set_identifier = self._parent[set_identifier]
        return set_identifier


    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        self._parent[root_b] = root_a


    def __len__(self):
        return len(self._parent)
