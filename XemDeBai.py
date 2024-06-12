"""Viết chương trình tính:
S = 1 + 2 + ... + n
S1 = 1 + 3 + ... + (2n - 1)
S2 = 2 + 4 + ... + 2n
S3 = 12 + 22 + ... + n2
S4 = 1/1 + 1/2 + ... + 1/n
với n nguyên dương được nhập từ bàn phím."""

n = int(input("Nhập số n : "))

S = 0
S1 = 0
S2 = 0
S3 = 0
S4 = 0
for i in range(1, n + 1, 1):
    S = S + i
    S1 = S1 + 2 * i - 1
    S2 = S2 + 2 * i
    S3 = S3 + (i ** 2)
    S4 = S4 + (1 / n)

print("S = 1 + 2 + ... + ", n, " = ", S)
print("S1 = 1 + 3 + ... + (2 *", n, " - 1)   = ", S1)
print("S2 = 2 + 4 + ... + 2*", n, " = ", S2)
print("S3 = 1^2 + 2^2 + ... + ", n, "^2 = ", S3)
print("S4 = 1/1 + 1/2 + ... + 1/", n, " = ", S4)
"""
def TongLe()
 tongchan = 0
 for i in range (1,n):
    if i % 2 == 0:
        tongchan += i
    return tongchan

def TongLe()
 tongle = 0
 for i in range (1,n):
    if i % 2 != 0:
        tongle += i
    return tongle
def main():
    n = 30
    print(TongChan(n))
    print(TongLe(n))
    n = 50
    print(TongChan(n))
    print(TongLe(n)) """
