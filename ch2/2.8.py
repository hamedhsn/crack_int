from ch2.linkedlist import LinkedList


def loop_detection_hashmap(l1):
    """ using a dictionary to store and check if node already exists
    time complexity is O(N) - Space complexity is O(N)

    :param l1:
    :return:
    """
    node_dict = dict()
    for item in l1.traverse():
        if node_dict.get(item):
            return item.data
        else:
            node_dict[item] = True

    print('There is no loop in this linked list')


def loop_detection_slow_fast_runner(ll1):
    """find first node of loop using slow and fast runner
    time complexity is O(N) - Space is O(1)

    :param ll1:
    :return:
    """
    slow = ll1.head
    fast = ll1.head

    while True:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    slow = ll1.head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.data

if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.create([1, 2, 3, 4, 5, 6, 7, 8])
    print(loop_detection_hashmap(ll1))

    for n in ll1.traverse():
        pass

    n.next = ll1.head.next.next

    print('\nStart of the loop in this linked list is : {}'.format(loop_detection_hashmap(ll1)))

    print('\nStart of the loop in this linked list is : {}'.format(loop_detection_slow_fast_runner(ll1)))