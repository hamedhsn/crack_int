# ''' is Unique'''


# using list with size 128 assume string contains ASCII code - O(n)
def detect_nonunique_str_1(st):
    if len(st) > 128:
        return False

    arr_cnt = [0 for i in range(128)]

    for s in st:
        arr_cnt[ord(s)] += 1

    # Pythonic way of checking
    # if len(list(filter(lambda s: s > 1, [1, 2, 0]))):
    #     return True
    # else:
    #     return False

    for a in arr_cnt:
        if a > 1:
            return False

    return True


# using hash O(n)
def detect_nonunique_str_2(st):
    letters = dict()
    for s in st:
        if letters.get(s):
            return 'Not unique'
        else:
            letters[s] = True
    return 'String is unique'


# using sort o(nlogn)
def detect_nonunique_str_3(st):
    sorted_st = sorted(st)
    for i in range(len(sorted_st)-1):
        if sorted_st[i] == sorted_st[i+1]:
            return 'Not unique'
    return 'String is unique'

if __name__ == '__main__':
    for a in ['hameda', 'hamed', 'h', '']:
        # print('{} : {}'.format(a, detect_nonunique_str_2(a)))
        # print('{} : {}'.format(a, detect_nonunique_str_3(a)))
        print('{} : {}'.format(a, detect_nonunique_str_1(a)))

