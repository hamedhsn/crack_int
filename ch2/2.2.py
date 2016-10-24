import logging

from ch2.linkedlist import LinkedList


# using two pointer
def find_kth(linked_list, k):
    """ using two moving pointer in linked list - time complexity O(N)

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
    """ using recursive approach which prints the results - time complexity is O(N)
    but space complexity is also O(N)

    :param llist: input linked list
    :param k: k integer
    """
    kth_rec(llist.head, k)


def kth_rec_2(llist_node, k):
    if llist_node is None:
        return 0, None

    indx, val = kth_rec_2(llist_node.next, k)
    indx += 1

    if indx == k:
        val = llist_node.data
        # print('Kth item from the end of linked list is : {}'.format(llist_node.data))

    return indx, val


def find_kth_recursive_2(llist, k):
    """ using recursive approach which returns value - time complexity is O(N)
    but space complexity is also O(N)

    :param llist: input linked list
    :param k: k integer
    :return: kth item from end of linked list
    """
    indx, val = kth_rec_2(llist.head, k)
    return val

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append_few([1, 5, 2, 3, 4, 1, 2, 5, 6, 5, 1])
    linked_list.print_all()

    k = 7
    # method1
    val = find_kth(linked_list, k)
    print('\nKth item from the end of linked list is : {}'.format(val))

    # method 2
    find_kth_recursive(linked_list, k)

    # method 3
    val = find_kth_recursive_2(linked_list, k)
    print('\nKth item from the end of linked list is : {}'.format(val))
