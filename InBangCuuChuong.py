#Viết chương trình Python đọc số n (1 <n < 9) và in bảng cửu chương n ra màn hình.
n = int(input())

if n < 1 or n > 9:
    print("Chỉ tính bảng cửu chương từ 1 đến 9 thôi")
else:
    for i in range(1,10):
        print("{} x {} = {}".format(n,i,n*i))