'''
Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.

Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234

'''

def cal(n):
    a = int("%s" % (n))
    aa = int("%s%s" % (n, n))
    aaa = int("%s%s%s" % (n, n, n))
    aaaa = int("%s%s%s%s" % (n, n, n, n))
    return a + aa + aaa + aaaa


print(cal(int(input("Input your number: "))))
