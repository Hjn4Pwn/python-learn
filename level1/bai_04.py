'''
Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều khiển, tạo ra một danh sách và một tuple chứa mọi số.

Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

'''

input_str = input("Input your number list: ")

tuple_result = tuple(input_str.split(","))
list_result = list(input_str.split(","))

print(f"Tuple: {tuple_result}")
print(f"List: {list_result}")
