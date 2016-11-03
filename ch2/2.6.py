from ch2.linkedlist import LinkedList, Node


def palindrome(ll1):
    """ find palindrome of a linked list using a recreation of first list in reverse order
    time complexity: O(N)

    :param ll1: linked list target
    :return: True if it is palindrome False otherwise
    """
    if ll1.head is None:
        print('Linked list is empty')
        return False
    ll2 = reverse_copy(ll1)

    return is_equal(ll1.head, ll2.head)


def reverse_copy(linked_list):
    ll2 = LinkedList()

    for item in linked_list.traverse():
        if item == linked_list.head:
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


# ##### Second approach ######
def palindrome_runner(linked_list):
    """ use second runner to solve the problem

    :param linked_list:
    :return:
    """
    is_mid = False
    stack = list()

    for item in linked_list.traverse():

        if is_mid is False:

            # add head and take care of linked list with one or two items
            if item == linked_list.head:
                if item.next is None:
                    return True

                elif item.next.next is None:
                    scnd = item

                else:
                    scnd = item.next.next
                    stack.append(item.data)
                    continue

            if scnd.next:
                stack.append(item.data)
                if scnd.next.next:
                    scnd = scnd.next.next
                else:
                    is_mid = True
            else:
                is_mid = True
        else:
            cmpr_dt = stack.pop()
            if item.data != cmpr_dt:
                return False

    return True

def palindrome_runner_alternative(linked_list):
    fast = linked_list.head
    slow = linked_list.head

    stack = list()

    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        fast = fast.next.next
        slow = slow.next

    # for case that the length of linked list is odd
    if fast is not None:
        slow = slow.next

    while slow is not None:
        if stack.pop() != slow.data:
            return False
        slow = slow.next

    return True

if __name__ == '__main__':
    ll1 = LinkedList()

    ll1.create([])
    print('\n Palindrome check is: {} '.format(palindrome(ll1)))

    # ll1.create([1, 2, 4, 2, 1])
    ll1.create([1, 1])
    print('\n Palindrome check is: {}'.format(palindrome(ll1)))

    print('\n Palindrome check using 2nd method is: {}'.format(palindrome_runner(ll1)))

    print('\n Palindrome check using 2nd method alternative is: {}'.format(palindrome_runner(ll1)))