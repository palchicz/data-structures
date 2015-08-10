class DisjointSet():


    def __init__(self):
        self._parents = {}


    def add(self, element):
        self._parents[element] = element


    def add_many(self, elements):
        for element in elements:
            self.add(element)


    def find(self, element):
        return self._parents[element]


    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        self._parents[root_b] = root_a

    def __len__(self):
        return len(self._parents)
