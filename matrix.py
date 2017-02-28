import math

def print_matrix( matrix ):
    res = ""
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            res += (str)(matrix[y][x]) + "\t"
        res += "\n"
    print(res)

def ident( matrix ):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if x == y:
                matrix[y][x] = 1
            else:
                matrix[y][x] = 0

def scalar_mult( matrix, s ):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            matrix[y][x] = matrix[y][x] * s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if len(m1) == len(m2[0]):
        m3 = new_matrix(len(m1), len(m2[0]))
    for r1 in range(len(m1)):
        for c2 in range(len(m2[0])):
            val = 0
            for r in range(len(m2)):
                val += m1[r1][r] * m2[r][c2]
            m3[r1][c2] = val
    for y in range(len(m2)):
        for x in range(len(m1[y])):
            m2[y][x] = m3[y][x]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
