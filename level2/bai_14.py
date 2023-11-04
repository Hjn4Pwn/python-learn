'''
Viết chương trình Python nhập một mảng hai chiều các số thực A (m hàng, n cột) từ bàn phím.
a. Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột
b. Tìm phần tử lớn nhất và phần tử nhỏ nhất của mảng A cùng các chỉ số hàng và cột của 2 phần tử này.
c. Trong mảng A có bao nhiêu phần tử bằng phần tử lớn nhất.

Gợi ý:
Sử dụng thư viện numpy để khởi tạo mảng A và thực hiện các phép toán trên mảng.
Câu lệnh np.amax(A, axis=0) trả về giá trị lớn nhất trên mỗi cột của mảng A, còn np.amin(A, axis=0) trả về giá trị nhỏ nhất trên mỗi cột.
Để tìm phần tử lớn nhất và nhỏ nhất của mảng A cùng với chỉ số hàng và cột của 2 phần tử này, 
chúng ta sử dụng np.amax(A) và np.amin(A) để tìm giá trị lớn nhất và nhỏ nhất của mảng A, 
sau đó sử dụng hàm np.unravel_index để chuyển đổi chỉ số dạng 1 chiều thành chỉ số dạng 2 chiều.
'''

import numpy as np

m, n = map(int, input("Input m,n: ").split(","))

arr = np.zeros((m, n))

for i in range(m):
    arr[i, :] = list(
        map(int, input(f"Input row {i+1} of the array: ").split(" ")))

print(f"Maximum values in each column: {np.amax(arr, axis=0).astype(int)}")
print(f"Minimum values in each row: {np.amin(arr, axis=1).astype(int)}")

max_value = np.amax(arr)
max_idx = np.unravel_index(np.argmax(arr), arr.shape)
print(
    f"The maximum value in the array is  {max_value} at [{max_idx[0]}][{max_idx[1]}]")


count_max_value = np.count_nonzero(arr == max_value)
print(
    f"The number of times the maximum value appears in the array is {count_max_value}")


value_to_find = 11
indices = np.where(arr == value_to_find)
print(f"Index found: {indices[0]}{indices[1]}")
