# Linked list implementation
class Node:
    def __init__(self, d):
        self.next = None
        self.data = d

    def append_tail(self, d):
        end = Node(d)
        n = self
        while n.next:
            n = n.next
        n.next = end

    def print_all(self):
        n = self
        print('\n{}'.format(n.data))
        while n.next:
            print(n.next.data)
            n = n.next

if __name__ == '__main__':
    head = Node(1)
    head.append_tail(2)
    head.append_tail(4)
    head.append_tail(0)
    head.print_all()
