# ''' Remove Duplicates '''


# remove duplicates using extra data structure
def remove_dups(llist):
    dup_dict = dict()
    h = llist.head
    while h.next:
        dup_dict[h.data] = dup_dict.get(h.data, 0) + 1
