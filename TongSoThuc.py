"""""
Viết chương trình cho phép người dùng nhập số thực từ bàn phím, giá trị tổng được
khởi tạo bằng 0. Trong khi số được nhập lớn hơn 0, thì tính tổng nghịch đảo và cho phép
người dùng nhập tiếp tục. Khi số được nhập nhỏ hơn hay bằng 0, thì in ra giá trị tổng và kết
thúc chương trình.
"""

tong = 0
so_thuc = 1
while so_thuc > 0:
    so_thuc = float(input("Hãy nhập số vào đi bạn ơi: "))
    if so_thuc <= 0:
        break
    tong = tong + 1 / so_thuc

print("Kết quả là: {}".format(tong))