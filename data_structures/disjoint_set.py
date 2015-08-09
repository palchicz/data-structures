class DisjointSet():

    def __init__(self):
        self._size = 0

    def add(self, element):
        self._size += 1

    def add_many(self, elements):
        for element in elements:
            self.add(element)

    def __len__(self):
        return self._size
