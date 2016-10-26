from ch2.linkedlist import LinkedList


def remove_item(llist_node):
    if llist_node.next is None:
        return False
    else:
        llist_node.data = llist_node.next.data
        llist_node.next = llist_node.next.next
        return True

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append_few([1, 5, 2, 3, 4, 1, 2, 5, 6, 5, 1])
    linked_list.print_all()

    remove_item(linked_list.head.next)
    linked_list.print_all()

