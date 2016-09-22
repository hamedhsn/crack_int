# ''' URLify'''


def replace_space(inp_st):
    orig_st_len = len(inp_st)

    # count number of zeros
    num_spc = 0
    for i in inp_st:
        if i == ' ':
            num_spc +=1

    # array of characters
    inp_st = list('{}{}'.format(inp_st, num_spc*2*' '))

    last_ind = len(inp_st)
    for i in reversed(range(orig_st_len)):
        if inp_st[i] == ' ':
            inp_st[last_ind-1] = '0'
            inp_st[last_ind-2] = '2'
            inp_st[last_ind-3] = '%'
            last_ind -= 3
        else:
            inp_st[last_ind-1] = inp_st[i]
            last_ind -= 1

    return ''.join(inp_st)

if __name__ == '__main__':
    print(replace_space('this  is a test '))




