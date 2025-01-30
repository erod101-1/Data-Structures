# Forest of Trees
'''
Tree for every disjoint set
edges:
[1,2],[4,1],[2,4]
child -> parent
2 -> 1
Find Parent of Node... Union by rank (consider the height of the trees that we are unioning)
'''

class UnionFind:
    def __init__(self,n):
        self.parent = {}
        self.rank = {}
        for i in range(1,n + 1):
            self.parent[i] = i
            self.rank[i] = 0
    def find(self,n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]] # iterate to parent
            p = self.parent[p] # optimize
        return p 
    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2) 
        if p1 == p2: # same root parent return false
            return False 
        # union by rank
        if self.rank[p1] > self.rank[p2]: 
            self.parent[p2] = p1 
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True