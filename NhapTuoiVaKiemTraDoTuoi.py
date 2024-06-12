# Viết chương trình nhập vào số tuổi, kiểm tra độ tuổi,
# tuổi <= 12 là trẻ em
# 12 < tuổi < 18, vị thành niên
# 18 <= tuổi là thanh niên

tuoi = int(input("Tuổi là:"))
if tuoi <= 12:
    print("là trẻ em")
elif 12 <tuoi< 18:
    print("Là vị thành niên")
elif 18 <= tuoi:
    print("trưởng thành")
# else:
#    print("trưởng thành")