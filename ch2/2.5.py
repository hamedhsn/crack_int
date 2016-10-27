from ch2.linkedlist import LinkedList, Node


def sum_list_reverse(ll1, ll2):
    ll1 = ll1.head
    ll2 = ll2.head

    tot = ''
    carr = 0
    while ll1:
        s = str(ll1.data + ll2.data + carr)

        if ll1.next is None:
            tot += s
        else:
            tot += s[1]
            carr = int(s[0])

        ll1 = ll1.next
        ll2 = ll2.next

    # create tot linked list
    nn = Node(tot[0])
    end = nn

    for ch in tot[1:]:
        end.next = Node(int(ch))
        end = end.next

    fin_ll = LinkedList()
    fin_ll.head = nn

    return fin_ll

if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.append_few([7, 1, 6])

    ll2 = LinkedList()
    ll2.append_few([5, 9, 2])

    fin_ll = sum_list_reverse(ll1, ll2)
    fin_ll.print_all()
