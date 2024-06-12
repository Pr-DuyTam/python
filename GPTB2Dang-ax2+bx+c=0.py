#Viết chương trình giải phương trình bậc 2 dạng: ax2 + bx + c = 0 với các hệ số a, b, c được nhập từ bàn phím (a # 0).
import math
print("Giải phương trình bậc 2 dạng: ax^2 + bx + c")
a = int(input("Giá trị của a = "))
b = int(input("Giá trị của b = "))
c = int(input("Giá trị của c = "))

delta = b**2 - 4*a*c
if(delta < 0):
    print("Phương trình" + " " + str(a) + "x^2 +" + str(b) + "x + " + str(c) + " " + "Vô nghiệm")
elif(delta == 0):
    x1 = x2 = (-b) / 2*a
    print("Phương trình" + " " + str(a) + "x^2 +" + str(b) + "x + " + str(c) + " " + "Có nghiệm kép x1 = x2: "+ str(x1))
else:
    x1 = (-b + math.sqrt(delta)/(2*a))
    x2 = (-b - math.sqrt(delta)/(2*a))
    print("Phương trình" + " " + str(a) + "x^2 +" + str(b) + "x + "+ str(c) + " " + "Có 2 nghiệm x1="+ str(x1) + "và" + "x2= " + str(x2) )