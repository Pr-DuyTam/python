"""Viết chương trình nhập 3 số dương a, b, c trên một dòng cách nhau bởi dấu phẩy, kiểm tra xem 3 số này
có tạo thành độ dài của một tam giác được hay không
thể hiện trên màn hình dòng chữ ‘Có thể tạo thành một tam giác’ hoặc ‘Không thể tạo thành một tam giác’."""
a, b ,c = map(float,input("Nhập a,b,c: ").split())
if(a+b>c and a+c>b and b+c>a):
    print("Có thể tạo thành 1 tam giác")
else:
    print("Không thể tạo thành 1 tam giác")