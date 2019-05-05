"""
在input.txt输入排序数字
"""
import sys
import os
class LinkErr(Exception): pass
class Empty(Exception): pass

datas = []

class BinHeap:
    def __init__(self, val):
        self.val = val  
        self.idx = 0
        self.fruits = []
 
    def link(self, other):
        if self.idx != other.idx:
            raise LinkErr()
        if self.val > other.val:
            raise LinkErr()
        self.fruits.append(other)
        self.idx += 1 
        return True
         
class BinHeapSet:
    def __init__(self,ini=2e300):
        self.ini = ini
        self.sets = []
        self.eles = 0
        self.min = self.ini
        self.min_idx = -1
 
    def __capFun(self):
        return 2**len(self.sets) - 1
 
    def __resFun(self):
        while self.__capFun() < self.eles:
            self.sets.append(None)
 
    def __addMe(self,new_tree):
        self.eles = self.eles + 2**new_tree.idx
        self.__resFun()
        while self.sets[new_tree.idx] is not None:
            if self.sets[new_tree.idx].val < new_tree.val:
                new_tree, self.sets[new_tree.idx] = \
                 self.sets[new_tree.idx], new_tree
            r = new_tree.idx
            new_tree.link(self.sets[r])
            self.sets[r] = None
        self.sets[new_tree.idx] = new_tree
        if new_tree.val <= self.min:
            self.min = new_tree.val
            self.min_idx = new_tree.idx
 
    def insert(self, val):
        tree = BinHeap(val)        
        self.__addMe(tree)
 
    def del_me(self):
        if not self:
            raise Empty()
        to_remove = self.sets[self.min_idx]
        self.sets[to_remove.idx] = None
        self.eles = self.eles - 2**to_remove.idx
        for child in to_remove.fruits:
            self.__addMe(child)
             
        self.min = self.ini
        for tree in self.sets:
            if tree is not None:
                if tree.val <= self.min:
                    self.min = tree.val
                    self.min_idx = tree.idx
                     
    def __nonzero__(self):
        return self.eles
     
    def __len__(self):
        return self.eles
             
     
def run_test():
    Q1 = BinHeapSet()
    for x in datas:
        Q1.insert(x)

    while Q1:
        with open("output_bhsort.txt", "a+") as fo:
            fo.write(str(Q1.min) + "\n")
            Q1.del_me()

def check():
    if 2 == len(sys.argv):
        if sys.argv[1].endswith(".txt"):
            with open(sys.argv[1], "r") as fo:
                global datas
                datas = fo.readlines()
    else:
        print("Enter <input file>")
        exit(1)

    datas = [int(x) for x in datas]

    if os.path.exists("output_bhsort.txt"):
        with open("output_bhsort.txt", "r+") as fo:
            fo.truncate()
 
if __name__ == "__main__":
    check()
    run_test()