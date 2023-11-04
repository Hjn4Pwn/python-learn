'''
Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, 
phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. 
Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.

Ví dụ đầu vào là: 0100,0011,1010,1001
Đầu ra sẽ là: 1010
'''

result = []
for i in input("Input your list of numbers: ").split(","):
    convert_str_to_bin = int(i, 2)
    if convert_str_to_bin % 5 == 0:
        result.append(i)
print(", ".join(result))
