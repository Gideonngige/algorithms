def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False 

    #check if first row needs to be zeroed
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_zero = True
            break
    
    #check of first column needs to be zeroes
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    
    #use first row and column as markers 
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    #set zeroes based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    #zero out first row  if needed
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    
    #zero out first column if needed
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))