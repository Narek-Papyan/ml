num = int(input())
sum = 1
while num != 0:
    if num % 10 != 0:
        sum = sum * (num % 10)
    num = num // 10
print(sum)
