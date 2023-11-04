'''
Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ giao diện điều khiển.
Định dạng nhật kí được hiển thị:

D 100
W 200
(D là tiền gửi, W là tiền rút)

Giả sử đầu vào được cung cấp là:
D 300
D 300
W 200
D 100
Thì đầu ra sẽ là: 500
'''
result = 0
check = []
while True:
    s = input()
    if s:
        check = s.split(" ")
        if check[0] == "D":
            result += int(check[1])
        elif check[0] == "W":
            result -= int(check[1])
        else:
            pass
    else:
        break

print(f"Result: {result}")
