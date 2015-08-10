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


    def __len__(self):
        return len(self._parents)
