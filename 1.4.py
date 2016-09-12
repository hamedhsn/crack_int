''' Palindrome Permutation '''


# O(n) solution - use array to count each char - check at the end
# assumption is to ignore non characters
def is_palindrome_perm_1(inp_str):
    ascii_list = [0 for i in range(128)]

    for c in str.lower(inp_str):
        if ord('a') <= ord(c) <= ord('z'):
            ascii_list[ord(c)] += 1

    found_diff_lett = False

    for c_num in ascii_list:
        if not is_even(c_num):
            if found_diff_lett:
                return False
            else:
                found_diff_lett = True

    return True


# O(n) solution - use array to count each char - know result at the end
# slight improvement over is_palindrome_perm_1
# assumption is to ignore non characters
def is_palindrome_perm_2(inp_str):

    char_num = [0 for i in range(26)]

    num_odds = 0
    for c in str.lower(inp_str):
        if ord('a') <= ord(c) <= ord('z'):
            char_num[get_char_num(c)] += 1
            if not is_even(char_num[get_char_num(c)]):
                num_odds += 1
            else:
                num_odds -= 1

    print(num_odds)
    return num_odds <= 1


def get_char_num(ch):
    return ord(ch) - ord('a')


def is_even(num):
    if num % 2:
        return False
    else:
        return True

if __name__ == '__main__':
    print(is_palindrome_perm_2('cacawwt /3 RT'))
