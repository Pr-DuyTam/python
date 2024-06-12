"""Viết chương trình cho người dùng nhập vào từ bàn phím hai số a, b và một ký tự ch.
Kiểm tra nếu: ch là ‘+’ thì thực hiện phép tính a + b và in kết quả lên màn hình.
Nếu ch là ‘_’ thì thực hiện phép tính a – b và in kết quả lên màn hình, nếu ch là ‘*’ thì thực hiện phép tính a * b.
và in kết quả lên màn hình, nếu ch là ‘/’ thì thực hiện phép tính a / b và
in kết quả lên màn hình, nếu ch là ký tự khác các ký tự trên thì hiển thị ra màn hình ‘ký tự ‘ ch ‘ không phải là một toán tử."""
a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
ch = input("Nhap vao ki tu ch: ")

if ch == '+':
   print("Tổng của 2 số: ",a+b)
elif ch == '-':
   print("Hiệu của 2 số: ",a-b)
elif ch == '*':
   print("Tích của 2 số: ",a*b)
elif ch == '/':
   print("Thương của 2 số: ",a/b)
else:
    print("Ký hiệu 'ch' không phải là toán tử")