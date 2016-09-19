''' 1.5. One way'''


# complexity is O(n)
def find_one_away_1(str1, str2):
    """ first solution

    :param str1: first input string
    :param str2: second input string
    :return:
    """
    if abs(len(str1) - len(str2)) > 1:
        return False

    if len(str1) < len(str2):
        return insert_remove_check(str1, str2)
    if len(str1) > len(str2):
        return insert_remove_check(str2, str1)
    else:
        return replace_check(str1, str2)


def insert_remove_check(st1, st2):
    """ check for any one way change in insert/remove

    :param st1: first input string
    :param st2: second input string
    :return:
    """
    for ind, ch in enumerate(st1):
        if ch != st2[ind]:
            return False

    return True


def replace_check(st1, st2):
    """ check for any one replacement change

    :param st1: first input string
    :param st2: second input string
    :return:
    """
    num_diff = -1
    for ind, ch in enumerate(st1):
        if ch != st2[ind]:
            num_diff += 1

    return not bool(num_diff)

''' --------------------------------------------------------------------------------------- '''


# complexity is O(n) - combine the three operation check into one
def find_one_away_2(str1, str2):
    """ combine the insert/remove function with replace function in previouse solution

    :param st1: first input string
    :param st2: second input string
    :return:
    """
    if abs(len(str1) - len(str2)) > 1:
        return False

    str1, str2 = (str1, str2) if len(str1) <= len(str2) else (str2, str1)

    return check_ops(str1, str2)


def check_ops(st1, st2):
    """ check for

    :param st1: shorter string
    :param st2: longer string
    :return: True if they are one operation away False otherwise
    """
    num_diff = 0
    for ind, ch in enumerate(st1):
        if ch != st2[ind]:
            num_diff += 1

    if len(st1) != len(st2) and num_diff:
        return False

    if len(st1) == len(st2) and num_diff > 1:
        return False

    return True


if __name__ == '__main__':
    inp1 = ['tesths', 'wwwwgw', 'wq', 'we', 'testw']
    inp2 = ['testhsn', 'w', 'www', 'wq', 'tertq']
    for inp in zip(inp1, inp2):
        print('First solution : {} vs {} ->  {}'.format(inp[0], inp[1], find_one_away_1(inp[0], inp[1])))
        print('First solution : {} vs {} ->  {}'.format(inp[0], inp[1], find_one_away_2(inp[0], inp[1])))
