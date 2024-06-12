#Tính dãy số theo công thức. n nhập từ bàn phím.
try:
    x = int(input("Nhập x: "))
    n = int(input("Nhập n: "))
    sum = 0

    if n<0:
        print("Vui lòng nhập n lại: ")
    elif n==0:
        print(1)
    else:
        giaiThua = 1
        for i in range(1, n + 1):
            giaiThua *= i
            sum += x**i/giaiThua
        print("Kết quả là: ", sum)
except:
    print("Định dạng dấu vào không hợp lệ! ")