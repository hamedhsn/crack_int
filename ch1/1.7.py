''' Rotate Matrix '''


# complexity is O(n^2) - space complexity is 2n^2
def rotate_matrix(a, n):
    if len(a) != n*n:
        print('matrix is not n*n')
        exit()

    b = [0 for i in range(n*n)]
    sit_pos = n-1
    gap = 0
    for i in range(n*n):
        if i % n == 0 and i != 0:
            sit_pos -= 1
            gap = 0

        b[sit_pos+gap] = a[i]
        gap += n

    return ''.join(b)

if __name__ == '__main__':
    print(rotate_matrix('abcdefghijklmnop', 4))
    print(rotate_matrix('abcdefghi', 3))
