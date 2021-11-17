arr1 = [[1, 2, 3], [4, 5, 6]]
raw = len(arr1)
column = len(arr1[0])
output = []
for i in range(0, column):
    output_raw = []
    for j in range(0, raw):
        output_raw.append(arr1[j][i])
    output.append(output_raw)

print(output)

