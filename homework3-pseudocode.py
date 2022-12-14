# Pseudocode version written in python syntax but does not run due to Cormen's one-based array indexing while python has zero-based array indexing.
def rooty_print(matrix):
    print(rooty_printing(matrix, 1, len(matrix)))

def rooty_printing(matrix, i, j):
    
    if j == i - 1:
        return "d" + str(j)
    
    else:
        r = matrix[i][j]
        return "k" + str(r) + "(" + rooty_printing(matrix, i, r - 1) + "," + rooty_printing(matrix, r + 1, j) + ")"
    

matrix = [
    [1,1,2,2,2],
    [None,2,2,2,4],
    [None,None,3,4,5],
    [None,None,None,4,5],
    [None,None,None,None,5]
]

rooty_print(matrix)
    
    

    