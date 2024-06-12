# "*" ngược
# cách 1
"""
n = int(input("Nhập n vào đi nào: "))

for i in range(1, n+1, 1):
    for j in range(n, i-1, -1):
        print("*",end=" ")
    print()

"""

# cách 2
n = int(input("Nhập n vào đi bạn gì ơi: "))
for i in range(n, 0 - 1, -1):
    print("* " * i)


