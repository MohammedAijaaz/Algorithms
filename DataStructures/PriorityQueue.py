class Item:

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __str__(self):
        return "{}: {}".format(self.name, self.priority)


def prints(fn):
    def wrapper(*args):
        print("Before: ", args[0])
        result = fn(*args)
        print("After: ", args[0])
        return result
    return wrapper


class PriorityQueue:

    def __init__(self):
        self.items = []

    def leftChild(self, index):
        return index * 2 + 1

    def rightChild(self, index):
        return index * 2 + 2

    def parent(self, index):
        return (index - 1)//2

    def reorderTop(self, index):
        while index != 0 and self.items[self.parent(index)].priority > self.items[index].priority:
            self.swap(self.parent(index), index)
            index = self.parent(index)

    # @prints
    def insert(self, item):
        print("Insert: ", item)
        self.items.append(item)
        self.reorderTop(len(self.items)-1)

    @prints
    def pop(self):
        item = self.items[0]
        self.items[0] = self.items[-1]
        self.items.pop(-1)
        self.heapify(0)
        print("Pop: ", item)
        return item

    def heapify(self, index=0):
        itemIndex = index
        leftIndex = self.leftChild(index)
        rightIndex = self.rightChild(index)

        if leftIndex < len(self.items) and self.items[leftIndex].priority < self.items[itemIndex].priority:
            itemIndex = leftIndex
        if rightIndex < len(self.items) and self.items[rightIndex].priority < self.items[itemIndex].priority:
            itemIndex = rightIndex

        if index != itemIndex:
            self.swap(index, itemIndex)
            self.heapify(itemIndex)

    def swap(self, index1, index2):
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    def __str__(self):
        res = ""
        for item in self.items:
            res += str(item) + "\t"
        return res


def main():
    pq = PriorityQueue()
    pq.insert(Item("a", 10))
    pq.insert(Item("b", 15))
    pq.insert(Item("c", 30))
    pq.insert(Item("d", 40))
    pq.insert(Item("e", 50))
    pq.insert(Item("f", 100))
    pq.insert(Item("g", 40))
    pq.insert(Item("h", 1))
    pq.pop()
    pq.pop()
    pq.pop()
    pq.insert(Item("h", 2))
    pq.pop()
    pq.pop()
    pq.pop()
    pq.pop()


if __name__ == "__main__":
    main()
