a = [[0,1,1,1,0,0,0],[0,0,1,1,1,0,0],[0,0,0,1,1,1,0],[0,0,0,1,1,0,0],[0,0,1,1,0,0,0],[0,1,1,0,0,0,0],[1,1,0,0,0,0,0]]

k = [[1,0,1],[0,1,0],[1,0,1]]

def summary(k, a):
    sum = 0
    for i in range(len(k)):
        for j in range(len(k[0])):
            if a[i][j] * k[i][j] != 0:
                sum += a[i][j] * k[i][j]
    return sum

num_row = 0
num_col = 0
number = 0
sum_array = []
output = []
while(num_row != len(a)-2):
    sum_array_row = []
    while(num_col != len(a[0])-2):
        for i in range(num_row, num_row+3):
            new_row = []
            for j in range(num_col, num_col+3):
                new_row.append(a[i][j])
            output.append(new_row)    
        sum_array_row.append(summary(output, k))
        output = []
        num_col += 1
    sum_array.append(sum_array_row)
    num_row += 1
    num_col = 0
print(sum_array)
