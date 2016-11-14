import copy

from ch2.linkedlist import reverse_copy, LinkedList


def find_intersection(link_list_1, link_list_2):
    """ find the intersection node of the two linked list - time and space complexity is O(N)

    :param link_list_1: first linked list
    :param link_list_2: second linked list
    :return:
    """
    stack1 = list()
    stack2 = list()

    for n1 in link_list_1.traverse():
        stack1.append(n1)

    for n2 in link_list_2.traverse():
        stack2.append(n2)

    if n1 != n2:
        print('\nThey are not intersected')
        return None
    else:
        target_node = None
        while len(stack1) and len(stack1):
            tmp1 = stack1.pop()
            tmp2 = stack2.pop()

            if tmp1 == tmp2:
                target_node = tmp1
            else:
                return target_node

        return target_node


if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.create([1, 2, 3])

    ll2 = LinkedList()
    ll2.create([4, 5])
    for n in ll2.traverse():
        pass
    n.next = ll1.head

    ll1.print_all()
    print('is list 1')

    ll2.print_all()
    print('is list 2')
    target = find_intersection(ll1, ll2)
    print('\nCommon Node has value : {}'.format(target.data))

    # Second test
    ll3 = LinkedList()
    ll3.create([6, 7, 9])
    for n in ll3.traverse():
        pass
    n.next = ll1.head

    ll3.print_all()
    print('is list 3')

    target = find_intersection(ll3, ll2)
    print('\nCommon Node has value : {}'.format(target.data))

    # Third test
    ll4 = LinkedList()
    ll4.create([11, 12, 13])
    ll3.print_all()
    print('is list 4')
    find_intersection(ll3, ll4)


