matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

rotate_matrix = []
for i in range(len(matrix[0])):
    rotate_matrix_row = []
    for j in range(1,len(matrix)+1):
        rotate_matrix_row.append(matrix[-j][i])
    rotate_matrix.append(rotate_matrix_row)
print(rotate_matrix)
