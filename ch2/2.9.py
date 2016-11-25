from ch2.linkedlist import LinkedList


def find_loop_node(ll):
    fast = ll.head
    slow = ll.head

    while True:
        if fast.next is None or fast is None:
            return None
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            break

    slow = ll.head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def create_looped_ll():
    ll1 = LinkedList()
    ll1.create([1, 2, 3, 4, 5, 6, 7, 8])

    for n in ll1.traverse():
        pass

    n.next = ll1.head

    ll2 = LinkedList()
    ll2.create([-1, -2, -3])

    for n in ll2.traverse():
        pass

    n.next = ll1.head

    return ll2


def print_result(node):
    if node:
        print('starting node of the loop is: {}'.format(node.data))
    else:
        print('They is no loop in this linked list')

if __name__ == '__main__':
    # ##### test the logic works for a looped case
    ll = create_looped_ll()

    node = find_loop_node(ll)
    print_result(node)

    # ##### test if it does not work for non looped
    ll1 = LinkedList()
    ll1.create([-1, -2, -3])

    node = find_loop_node(ll1)
    print_result(node)

