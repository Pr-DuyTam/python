"""
Viết các thủ tục thực hiện các công việc sau:
a) Tham số là số tự nhiên n, in ra màn hình kết quả tổng các số 1+2+ ... + n
b) Tham số là 2 số tự nhiên m, n, in ra thông báo: ‘Hai số này là nguyên tố cùng hoặc ‘Hai số này không là nguyên tố cùng nhau’.
c) Tham số là số tự nhiên s chỉ số giây, thông báo số giờ, phút, giây mà giá trị chuyển sang"""
# Câu a
import math
def tinhTong():
    n = int(input("Nhập n: "))
    sum = 0
    for i in range(0, n+1):
        sum = sum +i
    print("Tống 1+2+...+n: " + str(sum))
tinhTong()

# Câu b
def cungNguyenTo():
    n = int(input("Nhập n: "))
    m = int(input("Nhập m: "))
    for i in range(1, min(n,m)+1):
        if(n%i==0 and m % i == 0):
            uocChung = i
    if(uocChung == 1):
        print("Là nguyên tố cùng nhau")
    else:
        print("Không là nguyên tố cùng nhau")
cungNguyenTo()

#Câu c
def transSecond():
    s = int(input("Nhập số giây muốn chuyển: "))
    if(s<3600):
        gio = 0
        phut =int(s/60)
        giay =int(s%60)
    else:
        gio = int(s/3600)
        phut = int((s -(gio * 3600))/60)
        giay = int(s -(gio*3600+phut*60))
    print("-->"+str(gio)+"Giờ"+str(phut)+"Phút"+str(giay)+"Giây")
transSecond
#Câu d
def abs():
    a = int(input("Nhập số thực a: "))
    b = int(input("Nhập số thực b: "))
    print("|a-b| = ",math.fabs(a-b))
abs()