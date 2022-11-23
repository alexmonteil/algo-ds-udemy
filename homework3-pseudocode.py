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
    [2,2,2,4],
    [3,4,5],
    [4,5],
    [5]
]

rooty_print(matrix)
    
    

    