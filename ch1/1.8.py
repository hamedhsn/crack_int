# ''' Zero matrix '''


# complexity O(no_rows, no_cols)
def replace_zeros(inp_mx, no_rows, no_cols):
    """ replace all the zeros and corresponding rows and cols

    :param inp_mx: list of elements
    :param no_rows: number of rows
    :param no_cols: number of columns
    :return:
    """
    if len(inp_mx) != no_rows*no_cols:
        print('number of elements does not match with number of row and cols provided')
        exit()

    rows, cols = find_zeros(inp_mx, no_rows)
    for ind, m in enumerate(inp_mx):
        r_no, c_no = which_row_col(ind, no_rows)
        if rows.get(r_no) or cols.get(c_no):
            inp_mx[ind] = 0

    return inp_mx


def find_zeros(inp_mx, no_rows):
    """ find all the zeros

    :param inp_mx:list of elements
    :param no_rows:
    :return:
    """
    # we can also use one array for rows and one for cols instead of two dicts
    rows = dict()
    cols = dict()
    for ind, m in enumerate(inp_mx):
        if m == 0:
            r_no, c_no = which_row_col(ind, no_rows)
            rows[r_no] = True
            cols[c_no] = True

    return rows, cols


def which_row_col(ind, no_rows):
    """ find row number and col number of given index

    :param ind:
    :param no_rows:
    :return:
    """
    r_no = int(ind / no_rows)
    c_no = ind % no_rows

    return r_no, c_no

if __name__ == '__main__':
    mx = ['a', 'b', 'c', 'd', 'e', 'f', 0, 'h', 'i', 'j', 0, 'l']
    print(replace_zeros(mx, 4, 3))
