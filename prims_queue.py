from math import floor


class PrimsQueue:
    """ Queue used by Prim's Algorithm
    """

    FROM_NODE = 0
    TO_NODE = 1
    VALUE = 2

    def __init__(self, heap=[]):
        """ Constructor

        :param heap: Optional array of nodes that will be made into a heap
        """
        if len(heap) == 0:
            self.heap = []
        for item in heap:
            to_node = item[self.TO_NODE]
            from_node = item[self.FROM_NODE]
            value = item[self.VALUE]
            self.push(from_node, to_node, value)

    def front(self):
        """ Returns the smallest value in the heap, so the next item in the queue

        :return: An edge that is a tuple in the form of (from, to, weight)
        """
        heap = self.heap
        if len(heap) == 0:
            return None
        item = heap[0]
        to_node = item[self.TO_NODE]
        from_node = item[self.FROM_NODE]
        value = item[self.VALUE]
        return from_node, to_node, value

    def pop(self):
        """ Takes the first element of the heap, removes it from the heap, and returns that item

        :return: The node with the lowest value
        """
        heap = self.heap
        if len(heap) < 1:
            return None

        ret_val = self.front()
        self.__delete(0)
        return ret_val

    def push(self, from_node, to_node, value):
        """ Pushes a node onto the min heap and corrects the heap

        :param from_node: The source node of an edge
        :param to_node: The destination node of an edge
        :param value: The weight of an edge
        :return: None
        """
        heap = self.heap
        heap.append([from_node, to_node, value])
        if len(heap) == 1:
            return

        index = len(heap) - 1
        while True:
            # parent of k is at (k-1)/2 [int division]
            parent_index = max(floor((index-1)/2), 0)
            parent_value = heap[parent_index][self.VALUE]

            if value < parent_value:
                self.__swap(parent_index, index)
                index = parent_index
            else:
                return

    def update(self, from_node, to_node, value):
        """ Updates a given node's priority if the given node's priority is better

        :param from_node: The source node of an edge
        :param to_node: The destination node of an edge
        :param value: The weight of an edge
        :return: None
        """
        heap = self.heap
        index = None
        for i in range(0, len(heap)):
            current_to = heap[i][self.TO_NODE]
            if current_to == to_node:
                index = i
                break
        if index is None:
            return
        elif heap[index][self.VALUE] < value:
            return
        else:
            self.__delete(index)
            self.push(from_node, to_node, value)

    def __delete(self, index):
        """ Removes an element in the heap at the given index, then corrects the heap

        :param index: The index of the node to be removed
        :return: None
        """
        heap = self.heap
        if index < len(heap) - 1:
            heap[index] = heap[len(heap) - 1]
            heap.pop()
        else:
            heap.pop()
            return

        value = heap[index][self.VALUE]
        while True:
            left_child_index = 2 * index + 1   # L child of k is 2k+1
            right_child_index = 2 * index + 2  # R child of k is 2k+2
            child_index = None
            if right_child_index < len(heap):
                right_child_value = heap[right_child_index][self.VALUE]
                left_child_value = heap[left_child_index][self.VALUE]
                child_index = right_child_index if (right_child_value < left_child_value) else left_child_index
            if child_index is None and left_child_index < len(heap):
                child_index = left_child_index

            if child_index is None or value <= heap[child_index][self.VALUE]:
                return
            else:
                self.__swap(child_index, index)
                index = child_index

    def __swap(self, index1, index2):
        """ Swaps two nodes in the heap at the given indices

        :param index1: Index of node 1
        :param index2: Index of the other node
        :return: None
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def print(self):
        """ Prints the contents of the queue with a blank line at the end

        :return: None
        """
        for index in range(0, len(self.heap)):
            print(self.heap[index])
        print()
