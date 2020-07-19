#Single linked list

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __str__():
        return '{self.data}'

class SLL:
    def __init(self):
        self.head = None

    def print_list(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next
    
if __name__ == "__main__":
    ll = SLL()
    ll.head = Node("Mon")
    ll.head.next = Node("Tue")
    ll.head.next.next = Node("Wed")
    ll.print_list()

    
