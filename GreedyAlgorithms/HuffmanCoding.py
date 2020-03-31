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

    def decode(self, root, code):

        if root.left == None and root.right == None:
            print(root.name)
            return root.name

        if code[0] == '0':
            self.decode(root.left, code[1:])
        elif code[0] == '1':
            self.decode(root.right, code[1:])

    def buildTree(self):

        # insert all unique chars first
        for k, v in self.source_frequency.items():
            item = ItemLR(k, v)
            self.pqueue.insert(item)

        while len(self.pqueue.items) > 1:
            x = self.pqueue.pop()
            y = self.pqueue.pop()
            z = ItemLR('_', x.priority + y.priority)
            z.left = x
            z.right = y
            self.root = z

            self.pqueue.insert(z)


class SortedHuffam():

    def __init__(self):
        super().__init__()

        self.source_frequencies = [ItemLR('a', 5), ItemLR('b', 9), ItemLR(
            'c', 12), ItemLR('d', 13), ItemLR('e', 16), ItemLR('f', 45)]
        self.queue1 = []
        self.queue2 = []

        self.buildTree()

    def getMinItem(self):
        if len(self.queue2) == 0:
            return self.queue1.pop(0)
        elif len(self.queue1) == 0:
            return self.queue2.pop(0)

        if self.queue1[0].priority < self.queue2[0].priority:
            return self.queue1.pop(0)
        return self.queue2.pop(0)

    def buildTree(self):

        # push all items to queue1

        for item in self.source_frequencies:
            self.queue1.append(item)

        while len(self.queue1) > 0 and len(self.queue2) >= 0:

            x = self.getMinItem()
            y = self.getMinItem()
            z = ItemLR('_', x.priority + y.priority)
            z.left = x
            z.right = y
            self.queue2.append(z)

        return self.queue2[0]


def main():

    s = "a"*5 + "b"*9 + "c"*12 + "d"*13 + "e"*16 + "f"*45
    huffman = Huffman(s)
    huffman.buildTree()
    huffman.renderTree(huffman.root, "")
    huffman.decode(huffman.root, "1101")

    sortedHuffman = SortedHuffam()
    root = sortedHuffman.buildTree()
    huffman.renderTree(root, "")


if __name__ == "__main__":
    main()
