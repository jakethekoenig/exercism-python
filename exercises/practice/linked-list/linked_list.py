class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.succeeding = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError("List is empty")
        value = self.tail.value
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.succeeding = None
        self.length -= 1
        return value

    def shift(self):
        if self.length == 0:
            raise IndexError("List is empty")
        value = self.head.value
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.succeeding
            self.head.previous = None
        self.length -= 1
        return value

    def unshift(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.succeeding = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.succeeding

    def delete(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                if current == self.head:
                    self.shift()
                elif current == self.tail:
                    self.pop()
                else:
                    current.previous.succeeding = current.succeeding
                    current.succeeding.previous = current.previous
                    self.length -= 1
                return
            current = current.succeeding
        raise ValueError("Value not found")
