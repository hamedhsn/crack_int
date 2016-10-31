# Linked list implementation
class LinkedList:
    def __init__(self, data=None):
        if data:
            self.head = Node(data)
        else:
            self.head = data

    def append(self, d):
        if not self.head:
            self.head = Node(d)
            return

        end = Node(d)
        h = self.head

        while h.next:
            h = h.next
        h.next = end

    def append_few(self, list_d):
        for d in list_d:
            self.append(d)

    def delete(self, d):
        h = self.head

        if h.data == d:
            self.head = h.next
            return

        while h.next:
            if h.next.data == d:
                h.next = h.next.next
                return

            h = h.next

        print('\nno such item deleted')

    def print_all(self):
        print('\nList of the items:')

        h = self.head

        if not h:
            print('\nlinked list is empty')
            return

        print('{}'.format(h.data))
        while h.next:
            print(h.next.data)
            h = h.next

    def traverse(self):
        h = self.head
        while True:
            if h.next:
                yield h
                h = h.next
            else:
                yield h
                return

    def create(self, list_items):
        if len(list_items) == 0:
            print('list is empty')
            return

        nn = Node(list_items[0])
        end = nn

        for item in list_items[1:]:
            end.next = Node(item)
            end = end.next

        self.head = nn

    def length(self):
        if self.head is None:
            return 0

        for num, a in enumerate(self.traverse(), 1):
            pass

        return num

    def padding_after(self, num, data=None):
        if num <= 0 :
            print('padding number is 0')

        for item in self.traverse():
            pass

        while num > 0:
            nn = Node(data)
            item.next = nn
            item = item.next

            num -= 1

    def padding_before(self, num, data=None):
        if num <= 0 :
            print('padding number is 0')

        new_head = Node(data)
        end = new_head

        while num-1 > 0:
            end.next = Node(data)
            end = end.next

            num -= 1

        end.next = self.head

        self.head = new_head

    def insert_before(self, data):
        new_head = Node(data)

        new_head.next = self.head

        self.head = new_head

class Node:
    def __init__(self, d=None):
        self.next = None
        self.data = d

    def print(self):
        print('\n{}'.format(self.data))


if __name__ == '__main__':
    link_list = LinkedList()
    link_list.append(2)
    link_list.append(4)
    link_list.append(4)
    link_list.append_few([3, 1, 5])
    link_list.print_all()

    link_list.delete(1)
    link_list.print_all()

    link_list.delete(4)
    link_list.print_all()

    link_list.delete(44)
    link_list.print_all()

    link_list.delete(5)
    link_list.print_all()

    for no, i in enumerate(link_list.traverse(), 1):
        print('No {}: {}'.format(no, i.data))

    link_list = LinkedList()
    link_list.create([])
    link_list.print_all()

    link_list.create([])
    print('\nlength of list: {}'.format(link_list.length()))

    link_list.create([1, 2, 3])
    print('\nlength of list: {}'.format(link_list.length()))

    link_list.padding_after(3, data=0)
    link_list.print_all()

    link_list.padding_before(3, 0)
    link_list.print_all()

    link_list.insert_before(5)
    link_list.print_all()
