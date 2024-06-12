"""
Bài 2.14.Cho phương trình đường thẳng 4x – 3y = 7.
Hãy viết chương trình liệt kê tất cả các cặp giá trị (x, y)
thỏa phương trình trên với điều kiện x, y là số nguyên,
x ∈ [-50, 100], y ∈ [-100, 50].
"""


for x in range(-50, 100+1):
    y = (4*x - 7)/3
    if int(y) == y and -100 <= y <= 50:
        print((x, int(y)))