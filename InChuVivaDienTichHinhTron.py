# Viết chương trình nhập vào bán kính của đường tròn. Tính vào in ra chu vi hình tròn và diện tích của hình tròn.
from math import pi
r = int(input("Bán kính là: "))
chuvi = 2*pi*r
dientich = pi*r*r
print("Kết quả chu vi là: {}".format(chuvi))
print("Kết quả dien tich là: {}".format(dientich))