from ch2.linkedlist import LinkedList, Node


def palindrome(ll1):
    """ find palindrome of a linked list
    time complexity: O(N)

    :param ll1: linked list target
    :return: True if it is palindrome False otherwise
    """
    ll2 = reverse_copy(ll1)

    return is_equal(ll1.head, ll2.head)


def reverse_copy(lined_list):
    ll2 = LinkedList()

    for item in lined_list.traverse():
        if item == lined_list.head:
            n = Node(item.data)
            continue

        tmp = Node(item.data)
        tmp.next = n
        n = tmp

    ll2.head = n

    return ll2


def is_equal(l1, l2):
    while l1 and l2:
        if l1.data != l2.data:
            return False

        l1 = l1.next
        l2 = l2.next

    return True


if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.create([1, 2, 4, 2, 1])
    print('\n Palindrome check is {}'.format(palindrome(ll1)))
