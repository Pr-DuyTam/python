#.Viết chương trình Python tính diện tích hình tròn với bán kính được nhập từ bàn phím.
from math import pi
r = int(input("Bán kính là: "))

dientich = pi*r*r
print("Kết quả dien tich là: {}".format(dientich))

