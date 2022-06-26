"""
The fundamental unit of a linked list is a node, which is a data entity with
at least one pointer reference. The pointer reference is directed towards the
next destination one is able to move.
"""
from typing import Any


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class SinglyLinkedList:
    def __init__(self, node: Node = None):
        self.head = node

    def append(self, value: Any = None):
        if value is None:  # does not allow NoneType value in the linked list
            return

        current_ptr = self.head
        while current_ptr.next is not None:
            current_ptr = current_ptr.next

        current_ptr.next = Node(value)

        return self.head
