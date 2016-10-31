from ch2.linkedlist import LinkedList, Node


def sum_list_reverse(ll1, ll2):
    """ sume the two list in reverse order - summing digit by digit
    time complexity is O(N) - Space complexity is O(1)

    :param ll1:
    :param ll2:
    :return:
    """
    ll1 = ll1.head
    ll2 = ll2.head

    tot = ''
    carr = 0
    while ll1 or ll2:
        ll1 = ll1 if ll1 else Node(0)
        ll2 = ll2 if ll2 else Node(0)

        s = ll1.data + ll2.data + carr
        b = s % 10
        c = int(s / 10)

        if ll1.next is None:
            tot += str(s)
        else:
            tot += str(b)
            carr = c

        ll1 = ll1.next
        ll2 = ll2.next

    # create tot linked list
    fin_ll = LinkedList()
    fin_ll.create([a for a in tot])

    return fin_ll


def sum_list_reverse_recursive(ll1, ll2):
    """ same algorithm like sum_list_reverse but in recursive way -
    time complexity is O(N) - space complexity is O(N)

    :param ll1:
    :param ll2:
    :return:
    """
    if ll1.head is None and ll2.head is None:
        print('linked lists are empty')
        exit()

    tot = sum_rec(ll1.head, ll2.head)

    # create tot linked list
    fin_ll = LinkedList()
    fin_ll.create([a for a in tot])

    return fin_ll


def sum_rec(l1, l2, carry=0):
    l1 = l1 if l1 else Node(0)
    l2 = l2 if l2 else Node(0)

    t = l1.data + l2.data + carry
    b = t % 10
    c = int(t/10)

    if l1.next or l2.next:
        return '{}{}'.format(b, sum_rec(l1.next, l2.next, c))
    else:
        return str(t)


def sum_list_reverse_recursive_followup(ll1, ll2):
    """ using recursive solution to sum two linked list
    time complexity is O(N) - space complexity is O(N)

    :param ll1:
    :param ll2:
    :return:
    """
    len1 = ll1.length()
    len2 = ll2.length()

    if len1 > len2:
        ll2.padding_before(len1 - len2, data=0)
    else:
        ll1.padding_before(len2 - len1, data=0)

    c, tot = sum_rec_followup(ll1.head, ll2.head)
    if c:
        tot = str(c) + tot

    # create tot linked list
    fin_ll = LinkedList()
    fin_ll.create([a for a in tot])

    return fin_ll


def sum_rec_followup(l1, l2):
    l1 = l1 if l1 else Node(0)
    l2 = l2 if l2 else Node(0)

    t = l1.data + l2.data

    if all([not l1.next, not l2.next]):
        b = t % 10
        c = int(t / 10)
        return c, b

    c, res = sum_rec_followup(l1.next, l2.next)
    t = t + c
    b = t % 10
    c = int(t/10)

    return c, '{}{}'.format(b, res)

if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.create([7, 1, 6])

    ll2 = LinkedList()
    ll2.create([5, 9, 2])

    fin_ll = sum_list_reverse(ll1, ll2)
    fin_ll.print_all()

    ll3 = LinkedList()
    ll3.create([8, 5, 6, 7])
    fin_ll = sum_list_reverse_recursive(ll1, ll3)
    fin_ll.print_all()

    ll2.create([5, 9, 5, 2])
    fin_ll = sum_list_reverse_recursive_followup(ll1, ll2)
    fin_ll.print_all()
