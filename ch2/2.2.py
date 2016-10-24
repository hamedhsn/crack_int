import logging

from ch2.linkedlist import LinkedList


def find_kth(linked_list, k):
    llist_node = None
    for no, item in enumerate(linked_list.traverse(), 1):
        if k == no:
            llist_node = item
            break

    if llist_node is None:
        logging.error('Kth item from end of link list does not exists')
        exit()

    for item in linked_list.traverse():
        if llist_node.next is None:
            return item.data

        llist_node = llist_node.next

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append_few([1, 5, 2, 3, 4, 1, 2, 5, 6, 5, 1])
    linked_list.print_all()

    k = find_kth(linked_list, 15)
    print('\n The kth item from the end of linked list is : {}'.format(k))