import logging

from ch2.linkedlist import LinkedList


# using two pointer
def find_kth(linked_list, k):
    """ using two moving pointer in linked list - complexity O(N)

    :param linked_list: input linked list
    :param k: integer k
    :return: kth item from end of linked list
    """
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


# using recursive solution
def kth_rec(llist_node, k):
    if llist_node is None:
        return 0

    indx = kth_rec(llist_node.next, k) + 1

    if indx == k:
        print('Kth item from the end of linked list is : {}'.format(llist_node.data))

    return indx


def find_kth_recursive(llist, k):
    """

    :param llist:
    :param k:
    """
    kth_rec(llist.head, k)

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append_few([1, 5, 2, 3, 4, 1, 2, 5, 6, 5, 1])
    linked_list.print_all()

    k = find_kth(linked_list, 7)
    print('\nKth item from the end of linked list is : {}'.format(k))

    find_kth_recursive(linked_list, 7)