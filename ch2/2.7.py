import copy

from ch2.linkedlist import reverse_copy, LinkedList


def find_intersection_reverse_traverse(link_list_1, link_list_2):
    """ find the intersection node of the two linked list -
     traverse both list and push elements into stack . then at the end compare if the have same end
     then start popping from stacks and compare until see the same nodes
    time and space complexity is O(N1+N2)

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

    # if the last item is not common means they are not intersected
    if n1 != n2:
        print('\nThey are not intersected')
        return None
    else:
        # traverse to find the intersection node
        target_node = None
        while len(stack1) and len(stack1):
            tmp1 = stack1.pop()
            tmp2 = stack2.pop()

            if tmp1 == tmp2:
                target_node = tmp1
            else:
                return target_node

        return target_node


# Second solution
def find_intersection_ignore_extras(link_list_1, link_list_2):
    """ find the intersection node of the two linked list -
    traverse both lists and count length then ignore the difference(length(l1) - length(l2)) from
    the beginning of longer list and then compare the elements unti see the intersection node
    time is O(N1+N2) but space complexity is O(1)

    :param link_list_1:
    :param link_list_2:
    :return:
    """
    for no1, n1 in enumerate(link_list_1.traverse()):
        pass

    for no2, n2 in enumerate(link_list_2.traverse()):
        pass

    # if the last item is not common means they are not intersected
    if n1 != n2:
        print('\nThey are not intersected')
        return None
    else:
        ll1 = link_list_1.head
        ll2 = link_list_2.head

        if no1 > no2:
            for i, node in enumerate(link_list_1.traverse(), 1):
                if i == no1 - no2:
                    ll1 = node.next
                    break
        elif no1 < no2:
            for i, node in enumerate(link_list_2.traverse(), 1):
                if i == no2 - no1:
                    ll2 = node.next
                    break

        while ll1 != ll2:
            ll1 = ll1.next
            ll2 = ll2.next

        return ll1


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
    target = find_intersection_reverse_traverse(ll1, ll2)
    print('\nCommon Node has value : {}'.format(target.data))

    # Second test
    ll3 = LinkedList()
    ll3.create([6, 7, 9])
    for n in ll3.traverse():
        pass
    n.next = ll1.head

    ll3.print_all()
    print('is list 3')

    target = find_intersection_reverse_traverse(ll3, ll2)
    print('\nCommon Node has value : {}'.format(target.data))

    # Third test
    ll4 = LinkedList()
    ll4.create([11, 12, 13])
    ll3.print_all()
    print('is list 4')
    find_intersection_reverse_traverse(ll3, ll4)

    # TEST SECOND METHOD
    target = find_intersection_ignore_extras(ll1, ll2)
    print('ll1 intersection with ll2 on data node: {}'.format(target.data))

    target = find_intersection_ignore_extras(ll1, ll3)
    print('ll1 intersection with ll3 on data node: {}'.format(target.data))

    target = find_intersection_ignore_extras(ll2, ll3)
    print('ll2 intersection with ll3 on data node: {}'.format(target.data))

    target = find_intersection_ignore_extras(ll4, ll3)
