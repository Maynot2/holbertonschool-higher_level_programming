#!/usr/bin/python3


"""This is the documentation for 100-singly_linked_list module"""


class Node:
    """Models a node of a single linked list"""

    def __init__(self, data, next_node=None):
        """Constructor method for node instances"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for the data property"""

        return self.__data

    @data.setter
    def data(self, val):
        """Setter method for the data property"""

        if isinstance(val, int):
            self.__data = val
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """Getter method for the next_node property"""

        return self.__next_node

    @next_node.setter
    def next_node(self, val):
        """Setter method for the next_node property"""

        if isinstance(val, Node) or val is None:
            self.__next_node = val
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """Models a single linked list made of nodes"""

    def __init__(self):
        """Constructor method for list instances"""

        self.__head = None

    def sorted_insert(self, val):
        """Inserts a node into the single linked list in ascending order """
        new_node = Node(val)

        if self.__head is None:
            self.__head = new_node
        elif self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node:
                if new_node.data >= node.data:
                    if node.next_node is None:
                        node.next_node = new_node
                        break
                    if new_node.data <= node.next_node.data:
                        next_node = node.next_node
                        node.next_node = new_node
                        new_node.next_node = next_node
                node = node.next_node

    def __str__(self):
        """Define custom behaviour for print function on single linked list"""

        node = self.__head
        printable_list = ''
        while node:
            printable_list += str(node.data)
            if node.next_node is not None:
                printable_list += '\n'
            node = node.next_node
        return printable_list
