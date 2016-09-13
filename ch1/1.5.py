''' 1.5. One way'''


# complexity is O(n)
def find_one_away_1(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    if len(str1) < len(str2):
        return insert_remove_check(str1, str2)
    if len(str1) > len(str2):
        return insert_remove_check(str2, str1)
    else:
        return replace_check(str1, str2)


def insert_remove_check(st1, st2):
    for ind, ch in enumerate(st1):
        if ch != st2[ind]:
            return False

    return True


def replace_check(st1, st2):
    num_diff = 0
    for ind, ch in enumerate(st1):
        if ch != st2[ind]:
            num_diff += 1

    return not bool(num_diff)


# complexity is O(n)
def find_one_away_2(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    if len(str1) <= len(str2):
        return check_ops(str1, str2)
    else:
        return check_ops(str2, str1)


def check_ops(st1, st2):
    num_diff = 0
    for ind, ch in enumerate(st1):
        if ch != st2[ind]:
            num_diff += 1
            return False

    return True and not bool(num_diff)

if __name__ == '__main__':
    inp1 = 'tesths'
    inp2 = 'testhsn'
    print(find_one_away_1(inp1, inp2))
    print(find_one_away_2(inp1, inp2))