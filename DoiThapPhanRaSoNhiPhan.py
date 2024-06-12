#Viết chương trình đổi số nguyên hệ thập phân ra số nhị phân.
n = -1
while (n<=0):
    n = int(input("Nhập số nguyên n: "))
x = n
ketQua = ""
while(n>0):
    ketQua = str(n%2) + ketQua
    print("n%2 =", n%2)
    n = n // 2
    print("n = ", n)
print("Kết quả: ", ketQua)