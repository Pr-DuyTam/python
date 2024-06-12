"""Viết các chương trình nhập số tự nhiên n và tính các giá trị sau:
a) Tính tổng 1 +2 +....+2n.
b) Tính tổng các số tự nhiên < n và là số lẻ.
c) Tính tổng các số tự nhiên < n và là số chẵn."""
n = int(input("Nhập số tự nhiên n: "))
#Câu a
sum1 = 0
for i in range(1,n*2):
    sum1 += i
print("Tổng 1 + 2 +...+2n= " + str(sum1))
#Câu b
i = 1
sum2 = 0
while(i<n):
    sum2 += i
    i += 2
print("Tống các số tự nhiên nhỏ hơn n và là số lẻ = " + str(sum2))
#Câu c
i = 0
sum3 = 0
while(i<n):
    sum3 += i
    i += 2
print("Tổng các số tự nhiên nhỏ hơn n và là số chẵn = " + str(sum3))