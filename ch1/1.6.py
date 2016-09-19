''' String compression'''


# complexity O(n)
def str_compression_check_1(inp_str):
    rep_cnt = 0
    rep_str = list()

    len_inp_str = len(inp_str)
    inp_str += '$'
    for i in range(len_inp_str):
        rep_cnt += 1
        if i == len_inp_str or inp_str[i] != inp_str[i+1]:
            rep_str.append(inp_str[i])
            rep_str.append(str(rep_cnt))
            rep_cnt = 0

    return ''.join(rep_str) if len(rep_str) < len_inp_str else inp_str[:-1]


# complexity O(n) - sub optimal as it count the repeats beforehand
def str_compression_check_2(inp_str):
    rep_cnt = 0
    rep_str = list()

    len_inp_str = len(inp_str)
    inp_str += '$'

    if not is_compressed(inp_str, len_inp_str):
        return inp_str[:-1]
    else:
        for i in range(len_inp_str):
            rep_cnt += 1
            if i == len_inp_str or inp_str[i] != inp_str[i + 1]:
                rep_str.append(inp_str[i])
                rep_str.append(str(rep_cnt))
                rep_cnt = 0

        return ''.join(rep_str)


def is_compressed(inp_str, len_inp_str):
    tot_len = 0
    rep_cnt = 0
    for i in range(len_inp_str):
        rep_cnt += 1
        if i == len_inp_str or inp_str[i] != inp_str[i + 1]:
            tot_len += 2
            rep_cnt = 0

    return True if tot_len < len_inp_str else False

if __name__ == '__main__':
    inpts = ['tesths', 'wwwwgww', 'www', 'we', 'testw', 'r']
    for inp in inpts:
        print('{}: {}'.format(inp, str_compression_check_2(inp)))
