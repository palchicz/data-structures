class DisjointSet():


    def __init__(self):
        self._parent = {}
        self._rank = {}


    def add(self, element):
        self._parent[element] = element
        self._rank[element] = 0


    def add_many(self, elements):
        for element in elements:
            self.add(element)


    def find(self, element):
        set_identifier = element
        path = set()
        while not self._is_root(set_identifier):
            path.add(set_identifier)
            set_identifier = self._parent[set_identifier]
        for set_member in path:
           self._parent[set_member] = set_identifier
        return set_identifier


    def _is_root(self, element):
        return self._parent[element] == element


    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            pass
        elif self._rank[root_a] == self._rank[root_b]:
            self._parent[root_b] = root_a
            self._rank[root_a] += 1
        elif self._rank[root_a] > self._rank[root_b]:
            self._parent[root_b] = root_a
        else:
            self._parent[root_a] = root_b


    def __len__(self):
        return len(self._parent)
