"""
Bài 2.11.Viết chương trình nhập vào 1 số nguyên dương n.
Hãy tính và in ra màn hình tổng các chữ số của n?
Ví dụ: n = 145
thì tổng các chữ số của n là 1 + 4 + 5 = 10
"""

n = int(input("Nhap so nguyen duong n: "))
tong = 0
temp = n
while n > 0:
    tong += n%10
    n //= 10

print("Tong cac chu so cua {}: {}".format(temp, tong))