# ''' check permutation'''


# sort two strings and compare complexity= O(nlogn)
def str_perm_comparison_sort(str1, str2):
    if len(str1) != len(str2):
        return False
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


# use dictionary to reduce complexity to O(n)
def str_perm_comparison_dict(str1, str2):
    if len(str1) != len(str2):
        return False

    perm_dict = create_perm_dict(str1)
    print(perm_dict)
    for lett in str2:
        if perm_dict.get(lett):
            if perm_dict.get(lett) != 0:
                perm_dict[lett] -=1
            else:
                return False
        else:
            return False

    return True


def create_perm_dict(inp_str):
    perm_dic = dict()
    for let in inp_str:
        if perm_dic.get(let):
            perm_dic[let] +=1
        else:
            perm_dic[let] = 1
    return perm_dic


# use 128 array to hold number of character() - complexity O(n) and space O(1)
def str_perm_comparison_list(str1, str2):
    if len(str1) != len(str2):
        return False

    if count_chars(str1) == count_chars(str2):
        return True
    else:
        return False


def count_chars(inp_str):
    ascii_list = [0 for i in range(128)]
    for s in inp_str:
        ascii_list[ord(s)] += 1

    return ascii_list

if __name__ == '__main__':
    # print(str_perm_comparison_sort('hsn', 'nsh'))
    # print(str_perm_comparison_dict('hsnh', 'nshh'))
    print(str_perm_comparison_list('hsnfh', 'nshhf'))