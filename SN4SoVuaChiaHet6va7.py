#Viết chương trình in ra các số nguyên có 4 chữ số, vừa chia hết cho 6 và vừa chia hết cho 7?
for i in range(1000,9999+1):
    if i % 6 == 0 and i % 7 ==0:
        print("Kết quả là: ",i)