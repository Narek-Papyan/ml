x = int(input())
i = 1
sum = 0
while i <= x:
    if x % i == 0:
        sum += 1 
    i += 1
print(sum)
