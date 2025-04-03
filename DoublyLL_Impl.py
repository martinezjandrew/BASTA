class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None

    def traverseForward(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def insertAtEnd(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = new_node
            new_node.prev = curr

    def insertAtBeginning(self, data):
        new_node = self.Node(data)

        new_node.next = self.head
        if new_node.next:
            new_node.next.prev = new_node

        self.head = new_node

    def insertAt(self, index, data):
        new_node = self.Node(data)

        if index == 0:
            self.insertAtBeginning(data)

        curr = self.head

        position = 0

        while curr is not None and position + 1 != index:
            position = position + 1
            curr = curr.next

        if curr is not None:
            new_node.prev = curr
            new_node.next = curr.next
            curr.next = new_node
            if new_node.next:
                new_node.next.prev = new_node

    def replaceAt(self, index, data):
        return "NOT READY YET"
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
        if self.head.next is None:
            self.head = None
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        if curr.prev:
            curr.prev.next = None

    def removeAt(self, index):
        if self.head is None:
            return

        curr = self.head
        position = 0

        if index == 0:
            self.removeAtBeginning()
            return

        while curr is not None and position < index - 1:
            position += 1
            curr = curr.next

        if curr is None:
            return

        if curr.prev:
            curr.prev.next = curr.next

        if curr.next:
            curr.next.prev = curr.prev
