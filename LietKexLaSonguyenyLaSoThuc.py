"""
Bài 2.15.Cho hàm so y = sqrt(3x^2 + 3x + 5)
Hãy viết chương trình liệt kê tất cả các cặp giá trị
(x, y) thỏa mãn hàm số trên với điều kiện
x là số nguyên, y là số thực, x ∈ [-10, 5].
"""

from math import sqrt

for x in range(-10, 5+1):
    y = sqrt(3*x*x + 3*x + 5)
    print((x, y))