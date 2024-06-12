# Nhập 1 kí tự, 1 số nguyên, 1 số thực. In ra màn hình kí tự độ rộng 3, số nguyên rộng 6, số thực 8 và 3 chữ số lẻ
kitu = input ("Nhap mot ký tự: ")
soNguyen = int (input ("Nhap mot so nguyen: "))
soThuc =float (input("Nhap so thực: "))

print ("|{:3s}|".format (kitu)) # s là kiểu char với 3 là bỏ 3 khoảng trống
print ("|{:6d}|".format (soNguyen)) # d là kí hiệu số nguyên với 6 khoảng trống
print ("|{:8.3f}|".format (soThuc)) # với 8 khoảng và lấy 3 số sau dấu phẩy