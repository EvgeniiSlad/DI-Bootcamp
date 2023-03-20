
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def append(self, data):
        node = Node(data, None)
        if self.head == None:
            self.head = node
        else:
            currentItem = self.head
            while currentItem.next != None:
                currentItem = currentItem.next

            currentItem.next = node

            
    def print(self):
        currentItem = self.head
        while currentItem != None:
            print(currentItem.data)
            currentItem = currentItem.next



list = LinkedList()

list.append('hadas')
list.append('Yossi')
list.append('Dalu')
list.append('Evgenii')
list.print()

head = {'data': 'hadas', 'next': {'data': 'Yossi', 'next': {'data': 'Dalu', 'next': {'data': 'Evgenii', 'next': None}}}}