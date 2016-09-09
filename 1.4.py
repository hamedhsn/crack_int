''' Palindrome Permutation '''


# O(n) solution
def is_palindrome_perm_1(inp_str):
    # remove whitespace
    inp_str = str.strip(inp_str)

    if len(inp_str) < 2:
        return False

    ascii_list = [0 for i in range(128)]

    for c in inp_str:
        ascii_list[ord(c)] += 1

    found_diff_lett = False

    for c_num in ascii_list:
        if not is_even(c_num):
            if found_diff_lett:
                return False
            else:
                found_diff_lett = True

    return True


def is_even(num):
    if num % 2:
        return False
    else:
        return True

if __name__ == '__main__':
    print(is_palindrome_perm_1('cacaw '))
