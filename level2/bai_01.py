'''
Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) 
(bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H]. 
Với giá trị cố định của C là 50, H là 30. D là dãy giá trị tùy biến, được nhập vào 
từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.

Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.

Gợi ý:
Nếu đầu ra nhận được là một số dạng thập phân, bạn cần làm tròn thành giá trị gần nhất, ví dụ 26.0 sẽ được in là 26.
Trong trường hợp dữ liệu đầu vào được cung cấp cho câu hỏi, nó được giả định là đầu vào do người dùng nhập từ giao diện điều khiển.

'''
import math

C = 50
H = 30


def cal(D):
    return round(math.sqrt(2*C*D/H))  # round lam tron den so nguyen gan nhat


str_input = input("Input your number: ")

arr = str_input.split(",")
result = []
for i in arr:
    result.append(str(cal(int(i))))

print("Result: " + (", ".join(result)))
