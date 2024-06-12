"""Giả sử một người A có số tiền bằng X, đem gửi tiết kiệm với lãi suất tháng là 0,6%;
hỏi rằng sau 18 tháng thì A có tất cả bao nhiêu tiền?
Hãy viết chương trình cho người dùng nhập vào số tiền X sau đó tính tổng tiền sau 18 tháng.
Biết rằng cứ 6 tháng thì tiền lãi được cộng vào gốc và người A không rút tiền."""

x = float(input("Số tiền gốc lúc đầu: "))
a = x * (1 + (0.6 / 100) * 6)**3
print("Tổng số tiền là: ", a)