# Viết chương trình cho phép nhập vào 1 số nguyên dương n. Tùy theo giá trị của n,
# hãy in ra các dấu *
# Cách 1
""""
n = int(input("Nhập n vào đi: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
"""
# Cách 2
n = int(input("Nhập n vào đi bạn ơi: "))
for i in range(1, n+1):
    print("* "*i)