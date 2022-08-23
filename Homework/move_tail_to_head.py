class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node:
            elements.append(cur_node.data)
            cur_node = cur_node.next

        return elements

    def move_tail_to_head(self):
        last_node = self.head

        while last_node:
            if last_node.next is None:
                break
            last_node = last_node.next

        while self.head != last_node:
            self.append(self.head.data)
            self.head = self.head.next

    def get_last_node(self):
        last_node = self.head

        while last_node:
            if last_node.next is None:
                break
            last_node = last_node.next

        return last_node.data

    def get_first_node(self):

        pass

list1 = LinkedList()

list1.append(1)
list1.append(2)
list1.append(3)
list1.append(5)
list1.append(10)

print(list1.display())

list1.move_tail_to_head()

print(list1.display())

