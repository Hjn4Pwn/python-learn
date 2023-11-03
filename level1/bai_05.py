'''
Định nghĩa một class có ít nhất 2 method:

getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
printString: in chuỗi vừa nhập sang chữ hoa.
Thêm vào các hàm kiểm tra đơn giản để kiểm tra method của class.

'''


class input_string:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Input your string: ")

    def printString(self):
        print(f"Your upcase string: {self.s.upper()}")


test = input_string()
test.getString()
test.printString()
