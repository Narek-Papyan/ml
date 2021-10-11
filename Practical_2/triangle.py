a = int(input())
b = int(input())
c = int(input())
if a+b <= c or a+c <= b or b+c <= a:
    print("No Triangle")
elif a == b == c:
    print("Acute Triangle")
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
    print("Right Triangle")
else: print("Obtuse Triangle")
