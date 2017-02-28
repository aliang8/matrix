from display import *
from draw import *

# Matrix testing
print("Testing matrix functions....\n")
m = new_matrix()
m2 = new_matrix()

# print matrix
print("m: \n")
print_matrix(m)
print("m2: \n")
print_matrix(m2)

# identity matrix
print("Identity matrix m: \n")
ident(m)
print_matrix(m)

# scalar multiplication
print("Scaling m by 3: \n")
scalar_mult(m,3)
print_matrix(m)

# matrix multiplication
print("---------------------------------\n")
print("m2: \n")
m2 = [[1,2,3],[4,5,6],[7,8,9]]
print_matrix(m2)
print("m3: \n")
m3 = [[0,0,1],[0,1,1],[1,1,1]]
print_matrix(m3)
print("m2 x m3 \n")
matrix_mult(m2,m3)
print_matrix(m3)

print("---------------------------------\n")

# Draw a diamond
screen = new_screen()
color = [135,206,250]
matrix = new_matrix()

add_edge(matrix,250,100,0,125,250,0)
add_edge(matrix,250,100,0,375,250,0)

add_edge(matrix,125,250,0,375,250,0)

add_edge(matrix,125,250,0,195,315,0)
add_edge(matrix,375,250,0,305,315,0)

add_edge(matrix,195,315,0,250,100,0)
add_edge(matrix,305,315,0,250,100,0)

add_edge(matrix,210,250,0,250,315,0)
add_edge(matrix,290,250,0,250,315,0)

add_edge(matrix,195,315,0,305,315,0)
print_matrix(matrix)


draw_lines( matrix, screen, color )
display(screen)

