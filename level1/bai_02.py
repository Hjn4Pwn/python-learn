'''
Viết một chương trình có thể tính giai thừa của một số cho trước. 
Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
'''

# input = int(input("Input: "))

# result = 1
# for i in range(2, input+1):
#     result *= i

# print(f"Ket qua cua giai thua {input} la: {result}")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


input = int(input("Input: "))

print(f"Factorial of {input} is: {factorial(input)}")
