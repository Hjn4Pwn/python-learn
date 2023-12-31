'''
Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều.
Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.

Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.

Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''

X = int(input("Input your X: "))
Y = int(input("Input your Y: "))

multi_list = [[0 for col in range(Y)] for row in range(X)]

for row in range(X):
    for col in range(Y):
        multi_list[row][col] = row*col

print(multi_list)
