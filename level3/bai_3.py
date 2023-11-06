'''
Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7

Gợi ý dùng: yield
'''


def putNumbers(n):
    i = 0
    while i < n:
        j = i
        i += 1
        if j % 7 == 0:
            yield j


for i in putNumbers(50):
    print(i)

'''
yield sẽ không trực tiếp trả về kết quả như là return mà nó sẽ tạm thời lưu trữ ở đó và cho phép hạm được tiếp tục thực thi. 
Điều này cho phép hàm đó có thể trả về 1 loạt các giá trị.
Nếu 1 hàm được khai báo với def và trong đó thay vì dùng return nó dùng yield thì hàm này sẽ tự động trở thành hàm tạo - generator function

Ghi thì ghi thể chứ thực tế như nào phải gặp nhiều sử dụng nhiểu mới hiểu được rõ bản chất của nó
'''
