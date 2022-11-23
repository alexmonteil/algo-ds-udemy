def rooty_print(matrix):
    print(rooty_printing(matrix, 0, len(matrix) - 1))

def rooty_printing(matrix, i, j):
    
    if j < i - 1:
        return
    
    elif j == i - 1:
        return "d" + str(i)
    
    else:
        r = matrix[i][j]
        return "k" + str(r) + "(" + rooty_printing(matrix, i, r - 2) + "," + rooty_printing(matrix, r, j) + ")"
    

matrix = [
    [1,1,2,2,2],
    [None,2,2,2,4],
    [None,None,3,4,5],
    [None,None,None,4,5],
    [None,None,None,None,5]
]

rooty_print(matrix)
    
    

    