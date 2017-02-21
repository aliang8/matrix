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

print("---------------------------------\n")
print("m2: \n")
m2 = [[1,2,3],[4,5,6],[7,8,9]]
print_matrix(m2)
print("m3: \n")
m3 = [[0,0,1],[0,1,1],[1,1,1]]
print_matrix(m3)
matrix_mult(m2,m3)
print_matrix(m3)




'''
# Draw
screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


draw_lines( matrix, screen, color )
display(screen)
'''
