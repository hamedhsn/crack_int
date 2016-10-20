# ''' Remove Duplicates '''

from ch2.linkedlist import LinkedList
import copy


def remove_dups_using_dict(llist):
    """ Remove duplicates using extra data structure(dictionary) - complexity O(N)

    :param llist: linked list of items
    """
    dup_dict = dict()
    for h in llist.traverse():
        dup_dict[h.data] = dup_dict.get(h.data, 0) + 1

    print('\nNo of duplicates: {}'.format(dup_dict))

    for item in llist.traverse():

        # remove if it occurs more than once
        if dup_dict[item.data] > 1:
            dup_dict[item.data] -= 1

            # if node to delete is head
            if item == llist.head:
                llist.head = llist.head.next
                prev_link = item
                continue

            # for other nodes
            prev_link.next = item.next

        prev_link = item

    llist.print_all()


def remove_dups_wout_ds(llist):
    """ Remove duplicates without using two pointers - complexity O(N^2)


    :param llist: linked list of items
    """
    sec_llist = copy.deepcopy(llist)  # avoid two pointer mixing with each other using same reference
    for item in llist.traverse():
        if item.next:
            sec_llist.head = item.next

        prev_link = item
        for node in sec_llist.traverse():
            if item.data == node.data:
                prev_link.next = node.next
            else:
                prev_link = node

if __name__ == '__main__':
    llist = LinkedList()
    llist.append_few([1, 5, 2, 3, 4, 1, 2, 5, 6, 5, 1])
    llist.print_all()

    remove_dups_wout_ds(llist)
    llist.print_all()

    remove_dups_using_dict(llist)
    llist.print_all()
