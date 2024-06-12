"""Viết chương trình nhập 3 số tự nhiên từ bàn phím là day, month và year có ý nghĩa là ngày, tháng, năm tương ứng.
Kiểm tra xem bộ dữ liệu đã nhập có hợp lý hay không."""
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

if (nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0)):
    n = 366
    print("Năm" + " " + str(nam) + " " + "Đây là năm đúng, là năm nhuận")
else:
    n = 365
    print("Năm" + " " + str(nam) + " " + "Đây là năm đúng, không là năm nhuận")

if (1 <= thang <= 12):

    print("Tháng" + " " + str(thang) + " " + "Đây là tháng trong năm" + " " + str(nam))
else:
    print("Tháng" + " " + str(thang) + " " + "Đây không là tháng trong năm" + " " + str(nam))

if (1 <= ngay <= 365 and n == 365):
    print("Ngày" + " " + str(ngay) + " " + "Là ngày trong năm" + " " + str(nam))
elif (1 <= ngay <= 366 and n == 366):
    print("Ngày" + " " + str(ngay) + " " + "là ngày trong năm" + " " + str(nam))
else:
    print("Ngày này không có trong năm")