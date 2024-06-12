# Viết chương trình in ra các số nguyên có 3 chữ số và chia hết cho 7?
for i in range(100, 999+1):
    if i % 7 == 0:
        print(i)