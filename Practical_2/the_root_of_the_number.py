number = int(input())
def summer(n):
    sum = 0
    while n != 0:
        sum = sum + (n % 10)
        n = n // 10
    print(sum)
    return sum
#sum = 0
a = summer(number)
while a >= 10:
    b = a
    a = summer(b)
