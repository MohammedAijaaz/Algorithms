from collections import Counter
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

pq = None


def importDS():
    global pq
    import DataStructures.PriorityQueue as pq


importDS()


class ItemLR(pq.Item):

    def __init__(self, name, priority):
        super().__init__(name, priority)
        self.left = None
        self.right = None


class Huffman:

    def __init__(self, s):
        self.source_string = s
        self.source_frequency = Counter(self.source_string)
        self.source_association = {}
        self.pqueue = pq.PriorityQueue()
        self.root = None

    def renderTree(self, root, s):

        if root.left == None and root.right == None:
            print("{} : {}".format(root.name, s))
            return

        self.renderTree(root.left, s + "0")
        self.renderTree(root.right, s + "1")

    def buildTree(self):

        # insert all unique chars first
        for k, v in self.source_frequency.items():
            item = ItemLR(k, v)
            self.pqueue.insert(item)

        print(self.pqueue)
        while len(self.pqueue.items) > 1:
            x = self.pqueue.pop()
            y = self.pqueue.pop()
            z = ItemLR('_', x.priority + y.priority)
            z.left = x
            z.right = y
            self.root = z

            self.pqueue.insert(z)

        print(z)


def main():

    s = "a"*5 + "b"*9 + "c"*12 + "d"*13 + "e"*16 + "f"*45
    print(s)
    huffman = Huffman(s)
    huffman.buildTree()
    huffman.renderTree(huffman.root, "")


if __name__ == "__main__":
    main()
