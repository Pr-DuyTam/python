# Viết chương trình nhập 3 số thực x,y,z. Hãy in ra giá trị trung bình của 3 số đó.
x = float (input("Nhập số thực thứ 1: "))
y = float (input("Nhập số thực thứ 2: "))
z = float (input("Nhập số thực thứ 3: "))

tB = ((x+y+z)/3)
print ("Giá trị trung bình là: {}".format(tB))