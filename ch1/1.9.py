# ''' String rotation '''


# without substring(in func) - finding the point of slice
def find_rotate1(inp_str1, inp_str2):
    if len(inp_str1) != len(inp_str2) and not len(inp_str1):
        return False

    base = ''
    ext = ''
    pointer = 0

    for ind, l in enumerate(inp_str1):
        if l != inp_str2[pointer]:
            base += l
        else:
            pointer += 1
            ext += l

    if ext + base == inp_str2:
        return True
    else:
        return False


# use slicing in python - without substring(in func)
def find_rotate2(inp_str1, inp_str2):
    if len(inp_str1) != len(inp_str2) and not len(inp_str1):
        return False

    base = ''
    for ind, l in enumerate(inp_str1):
        if l != inp_str2[0]:
            base += l
        else:
            break

    ext = inp_str1[ind:]

    if ext + base != inp_str2:
        return False
    else:
        return True


# use in function - yx is always in xyxy where xy is string1 and yx is string2
def find_rotate3(inp_str1, inp_str2):
    if len(inp_str1) == len(inp_str2) and len(inp_str1):
        if inp_str2 in inp_str1+inp_str1:
            return True

    return False

if __name__ == '__main__':
    print(find_rotate3('waterbottle', 'erbottlewat'))
    print(find_rotate3('waternottle', 'erbottlewat'))
    print(find_rotate3('waterbottle', 'waterbottle'))
    print(find_rotate3('testabc', 'bctesta'))
