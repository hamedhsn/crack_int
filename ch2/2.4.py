from ch2.linkedlist import LinkedList, Node
import copy


def partition(linked_list, part_val):
    right_ll = None
    left_ll = None

    for item in linked_list.traverse():
        tmp = copy.deepcopy(item)
        tmp.next = None
        if item.data >= part_val:

            if right_ll is None:
                right_ll = copy.deepcopy(tmp)
                # rr = copy.copy(item)
            else:
                tmp.next = right_ll.next
                right_ll.next = copy.deepcopy(tmp)
                # rr.next = copy.copy(item)
                # rr = rr.next

        else:
            if left_ll is None:
                left_ll = copy.deepcopy(tmp)
                # ll = copy.copy(item)
            else:
                tmp.next = left_ll.next
                left_ll.next = copy.deepcopy(tmp)

                # ll.next = copy.copy(item)
                # ll = ll.next

    while left_ll.next:
        left_en_ref = left_ll

    left_en_ref.next = right_ll

    linked_list.head = left_ll

    return linked_list

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append_few([1, 5, 2, 3, 4, 1, 2, 5, 6, 5, 1])

    linked_list = partition(linked_list, 5)
    linked_list.print_all()