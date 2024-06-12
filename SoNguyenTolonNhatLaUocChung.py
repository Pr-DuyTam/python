"""Viết hàm số f(m, n) với các tham số là các số tự nhiên.
Hàm sẽ trả lại số nguyên tố lớn nhất đồng thời là ước chung của m và n. Nếu số đó không tồn tại thì trả lại 0."""
def kiemTraSoNguyenTo(n):
    check = True
    if(n<2):
        check = False
        return check
    for i in range(2,n):
        if n % i == 0:
            check = False
            break
    return check
def uSCLN(a,b):
    if(b == 0):
        return a
    return uSCLN(b,a%b)
def f(m,n):
    if(kiemTraSoNguyenTo(uSCLN(m,n))):
        return uSCLN(m,n)
    else:
        return 0
x1 = int(input("Nhập số tự nhiên m: "))
x2 = int(input("Nhập số tự nhiên n: "))
print("Kết quả trả lại: ",f(x1,x2))