"""
Viết chương trình cho phép người dùng nhập điểm cho 1 sinh viên, biết điểm là số
thập phân và nằm trong đoạn từ 0 đến 10. Nếu người dùng nhập không hợp lý thì yêu cầu
nhập lại, nếu nhập hợp lý thì in ra điểm vừa nhập và kết thúc chương trình?
"""

diem = float(input("Nhập điểm: "))
if 0 <= diem <= 10:
    print("Điểm vừa nhập: {}".format(diem))
    print("Kết thúc rồi. Chúc mừng *-*")
else:
    print("Nhập sai rồi. Chỉ trong khoảng từ 0 đến 10. Nhập lại đi!")
    diem = float(input("Nhập lại điểm: "))
    print("Kết thúc rồi. Chúc mừng *-*")

"""
diem = float(input("Nhập điểm: "))
while not (0 <= diem <= 10):
    diem = float(input("Nhập điểm lại. Vì điểm đã ra ngoài khoảng 0 đến 10: "))
print("Điểm vừa nhập: {}".format(diem))
print("Kết thúc rồi. Chúc mừng *-*")
"""