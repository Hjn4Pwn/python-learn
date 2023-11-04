'''
Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy 
và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.

'''

# input_str = input("Input your list word: ")

# arr = input_str.split(",")
# arr.sort()
# print(arr)

arr = [x for x in input("Input your string: ").split(",")]
arr.sort()
print(arr)
