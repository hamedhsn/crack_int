# ''' Remove Duplicates '''

from ch2.linkedlist import LinkedList


# remove duplicates using extra data structure
def remove_dups(llist):
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

if __name__ == '__main__':
    llist = LinkedList()
    llist.append_few([1, 1, 2, 3, 4, 1, 2, 5, 6, 5])
    llist.print_all()
    remove_dups(llist)
