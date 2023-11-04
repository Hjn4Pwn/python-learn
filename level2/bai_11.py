'''
Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.

Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9

'''
result = [x for x in input("Input your list of numbers: ").split(
    " ") if int(x) % 2 != 0]
print(" ".join(result))
