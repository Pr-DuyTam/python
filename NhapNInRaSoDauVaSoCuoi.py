"""
Bài 2.12.Viết chương trình nhập vào 1 số nguyên dương n
(có ít nhất 2 chữ số).
Hãy in ra màn hình chữ số đầu và chữ số cuối của n?
Ví dụ: n = 239 thì in ra màn hình là 2 và 9
"""

while True:
    n = int(input("Nhap so nguyen n (n>=10): "))
    if n >= 10:
        break

so_cuoi = n % 10
n //= 10
while n > 0:
    so_dau = n % 10
    n //= 10

print("So dau va cuoi cua {}: {} va {}".format(n, so_dau, so_cuoi))