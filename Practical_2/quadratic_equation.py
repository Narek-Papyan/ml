import math
a = input()
b = input()
c = input()

if a == 0:
    print("Non-quadratic equation")
    if b == 0 and c == 0:
        print("Infinite solutions")
    elif b==0 and c != 0:
        print("No solutions")
    else:
        print(-float(c) / float(b))
if a != 0:
    print("Quadratic equation")
    D = b*b - 4*a*c
    print("Discriminant",  D)
    if D < 0:
        print("No Solutions")
    else:
        x_1 = (-b + math.sqrt(D)) / 2*a
        x_2 = (-b - math.sqrt(D)) / 2*a
        print(x_1)
        print(x_2)
