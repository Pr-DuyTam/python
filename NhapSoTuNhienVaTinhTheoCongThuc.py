"""Viết các chương trình nhập một số tự nhiên n và tính các giá trị sau:
a) Tính số các ước số nguyên tố khác nhau của n (tính cả n).
b) Tính tổng các ước số thực sự của n (không tính n).
c) Tính tổng 12 + 22 +32+....+n."""
n = int(input("Nhập số tự nhiên n: "))
count=0
sum_uocSo=0
for i in range(1,n+1):
    if(n%i==0):
        count=count + 1
    if(n%i==0 and i<n):
        sum_uocSo=sum_uocSo+i
print("Số tự nhiên n có " + ""+str(count)+" "+ "Ước số")
print("Tống các ước số thực khác n = "+str(sum_uocSo))