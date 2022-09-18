import math


class MinHeap:
    def __init__(self):
        self.heap = []

    @staticmethod
    def _get_parent_index(index):
        return math.floor((index - 1) / 2)

    @staticmethod
    def _get_left_index(index):
        return index * 2 + 1

    @staticmethod
    def _get_right_index(index):
        return index * 2 + 2

    @staticmethod
    def _has_parent(index):
        return MinHeap._get_parent_index(index) >= 0

    def _has_left(self, index):
        return MinHeap._get_left_index(index) < len(self.heap)

    def _has_right(self, index):
        return MinHeap._get_right_index(index) < len(self.heap)

    def _get_parent(self, index):
        return self.heap[MinHeap._get_parent_index(index)]

    def _get_left(self, index):
        return self.heap[MinHeap._get_left_index(index)]

    def _get_right(self, index):
        return self.heap[MinHeap._get_right_index(index)]

    def _swap(self, index_1, index_2):
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]

    def _heapify_up(self):
        index = len(self.heap) - 1
        while MinHeap._has_parent(index) and self._get_parent(index) > self.heap[index]:
            self._swap(index, self._get_parent_index(index))
            index = self._get_parent_index(index)

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up()

    def _heapify_down(self):
        index = 0

        while self._has_left(index):

            smaller_children_index = MinHeap._get_left_index(index)
            if self._has_right(index) and self._get_right(index) < self._get_left(
                index
            ):
                smaller_children_index = MinHeap._get_right_index(index)

            if self.heap[index] < self.heap[smaller_children_index]:
                break

            self._swap(index, smaller_children_index)
            index = smaller_children_index

    def extractMin(self):
        if len(self.heap) == 0:
            raise IndexError()

        min = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()

        return min


min_heap = MinHeap()
min_heap.insert(1)
min_heap.insert(2)
min_heap.insert(3)
print(min_heap.heap)
min_heap.insert(0)
print(min_heap.heap)
min_heap.insert(10)
print(min_heap.heap)
min_heap.insert(7)
print(min_heap.heap)
min_heap.insert(-10)
print(min_heap.heap)
print("-----")
print(min_heap.extractMin())
print(min_heap.heap)
print(min_heap.extractMin())
print(min_heap.heap)
print(min_heap.extractMin())
print(min_heap.heap)
