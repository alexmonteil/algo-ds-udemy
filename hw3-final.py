# Added additional row to the matrix to simulate Cormen's 1 indexed arrays
def rooty_print(matrix):
    print(rooty_printing(matrix, 1, len(matrix) - 1))

def rooty_printing(matrix, i, j):

    if j == i - 1:
        return "d" + str(j)
    
    else:
        r = matrix[i][j]
        return "k" + str(r) + "(" + rooty_printing(matrix, i, r - 1) + "," + rooty_printing(matrix, r + 1, j) + ")"
    

matrix = [
    [None,None,None,None,None,None],
    [None,1,1,2,2,2],
    [None,None,2,2,2,4],
    [None,None,None,3,4,5],
    [None,None,None,None,4,5],
    [None,None,None,None,None,5]
]

rooty_print(matrix)