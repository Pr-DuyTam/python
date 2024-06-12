"""Nhập vào 1 tháng, xuất tháng đó có bao nhiêu ngày.
Ví dụ tháng 1, 3, 5, 7, 8, 10, 12 có 31 ngày. Tháng 4, 6, 9, 11 có 30 ngày.
Nếu là tháng 2 thì yêu cầu nhập thêm năm. Năm nhuận thì tháng 2 có 29 ngày, không nhuần có 28 ngày."""

Thang = int(input("Nhập tháng mà bạn muốn biết số ngày: "))
if(Thang == 1 or Thang == 3 or Thang == 5 or Thang == 7 or Thang == 8 or Thang == 10 or Thang == 12):
    print("Tháng này có 31 ngày nè")
elif(Thang == 4 or Thang == 6 or Thang == 9 or Thang == 11):
    print("Tháng này có 30 ngày nè")
else:
    Nam = int(input("Nhập năm mà bạn muốn xem: "))
    if(Nam % 400 == 0 or (Nam % 4 == 0 and Nam % 100 != 0)):
        print("Tháng có 21 ngày")
    else:
        print("Tháng có 28 ngày")