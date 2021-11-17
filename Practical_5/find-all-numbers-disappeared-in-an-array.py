num = [4,3,2,7,9,2,3,1]
n = len(num)
num = set(num)
output = list()
for i in range(1, n):
    if i in num:
        continue
    else:
        output.append(i)
print(output)
