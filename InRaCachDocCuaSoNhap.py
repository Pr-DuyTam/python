"""Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.  Ví dụ: n=35 => Ba mươi lăm, n=5 => năm)."""
list_HangChuc = ["Mười","Hai mươi","Ba mươi","Bốn mươi","Năm mươi","Sáu mươi","Bảy mươi","Tám mươi","Chín mươi"]
list_HangDonVi =["Không","Một","Hai","Ba","Bốn","Năm","Sáu","Bảy","Tám","Chín"]
list_SoDacBiet =["Một","Hai","Ba","Bốn","Lăm","Sáu","Bảy","Tám","Chín"]
callNumberName =""
while(True):
    n = int(input("Nhập số nguyên tối đa là hai chữ số: "))
    if(0<=n<=99):
        break

if(n/10!=0):
    if(n == 11):
        callNumberName += list_HangChuc[int(n/10)-1]+" "+ list_HangDonVi[1]
    elif(n % 10 in [1,5]):
        callNumberName += list_HangChuc[int(n/10)-1]+" "+ list_SoDacBiet[n%10-1]
    else:
        callNumberName += list_HangChuc[int(n/10)-1]+" "+ list_HangDonVi[n%10]
else:
    callNumberName += list_HangDonVi[n%10]
print("Gọi bằng chữ: "+callNumberName)