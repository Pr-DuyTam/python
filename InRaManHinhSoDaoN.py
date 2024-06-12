"""
Bài 2.13.Viết chương trình nhập vào 1 số nguyên dương n.
Hãy in ra màn hình số đảo của n?
Ví dụ: n = 489 thì in ra màn hình là 984.
"""

n = int(input("Nhap so nguyen duong n: "))
temp = n
ketqua = 0
while n > 0:
    ketqua = ketqua*10 + n % 10
    n //= 10

print("So dao cua {} la: {}".format(temp, ketqua))