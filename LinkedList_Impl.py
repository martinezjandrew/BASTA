class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    def insertAtBeginning(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAt(self, index, data):
        if index == 0:
            self.insertAtBeginning(data)

        curr = self.head
        position = 0

        while curr is not None and position + 1 != index:
            position = position + 1
            curr = curr.next

        if curr is not None:
            new_node = self.Node(data)
            new_node.next = curr.next
            curr.next = new_node

    def replaceAt(self, index, data):
        curr = self.head
        position = 0
        if position == index:
            curr.data = data
        else:
            while curr is not None and position != index:
                position = position + 1
                curr = curr.next

            if curr is not None:
                curr.data = data

    def removeAtBeginning(self):
        if self.head is None:
            return

        self.head = self.head.next

    def removeAtEnd(self):
        if self.head is None:
            return

        curr = self.head
        while curr.next is not None and curr.next.next is not None:
            curr = curr.next

        curr.next = None

    def removeAt(self, index):
        if self.head is None:
            return

        curr = self.head
        position = 0

        if index == 0:
            self.removeAtBeginning()
        else:
            while curr is not None and position < index - 1:
                position += 1
                curr = curr.next

            if curr is not None and curr.next is not None:
                curr.next = curr.next.next

    def print(self):
        node = self.head
        while node is not None and node.next is not None:
            print(node.data, end=", ")
            node = node.next

        print(node.data)