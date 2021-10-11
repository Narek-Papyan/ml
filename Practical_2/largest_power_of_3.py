N = int(input())
n = 0
while 3 ** n <= N:
    n += 1
print(3 **(n - 1))
