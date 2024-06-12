#Viết chương trình in ra các số nguyên có 4 chữ số, chia hết cho 6 hoặc 7?
for i in range(1000,9999+1):
    if i % 6 == 0 or i % 7 == 0:
        print("Kết quả: ",i)    #print("Kết quả: {}".format)