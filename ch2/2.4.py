from ch2.linkedlist import LinkedList, Node


def partition_1(linked_list, part_val):
    """ partition by creating two linked list (one for greater and one for less than target value) and
    attaching them together
    Using append the time complexity is O(N2)

    :param linked_list:
    :param part_val:
    :return:
    """
    right_ll = LinkedList()
    left_ll = LinkedList()

    for item in linked_list.traverse():
        if item.data >= part_val:
            right_ll.append(item.data)
        else:
            left_ll.append(item.data)

    for item in left_ll.traverse():
        pass

    item.next = right_ll.head

    return left_ll


def partition_2(linked_list, part_val):
    """ partition by creating two linked list(one for greater and one for less than target value) and
    attaching them together
    creating the two linked list happens in one go so the time complexity is O(N)

    :param linked_list:
    :param part_val:
    :return:
    """
    right_ll = LinkedList()
    left_ll = LinkedList()

    for item in linked_list.traverse():
        tmp = Node(item.data)

        if item.data >= part_val:

            if right_ll.head is None:
                right_ll.head = tmp
            else:
                t = right_ll.head.next
                tmp.next = t
                right_ll.head.next = tmp

        else:
            if left_ll.head is None:
                left_ll.head = tmp
            else:
                if left_ll.head.next is None:
                    last_left_elm = tmp
                t = left_ll.head.next
                tmp.next = t
                left_ll.head.next = tmp

    last_left_elm.next = right_ll.head

    return left_ll


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append_few([9, 5, 6, 3, 4, 1, 2, 5, 6, 5, 1])

    linked_list = partition_1(linked_list, 5)
    linked_list.print_all()

    linked_list = partition_2(linked_list, 5)
    linked_list.print_all()
