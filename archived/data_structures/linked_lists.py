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

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = Node(value)

        return self.head

    def prepend(self, value: Any = None):
        if value is None:  # does not allow NoneType value in the linked list
            return

        new_head = Node(value)
        new_head.next = self.head

        return new_head

    def insert_after(self, value: Any = None, prev_node: Node = None):
        # :value param only works when linked list has unique values,
        # else it inserts after the first occurrence of :value
        if value is None and prev_node is None:
            return

        new_node = Node(value)

        if value:
            current_node = self.head
            found = False

            while current_node.next is not None:
                if current_node.data == value:
                    found = True
                    break

            if not found:
                return

            prev_node = current_node

        new_node.next = prev_node.next
        prev_node.next = new_node

        return self.head
