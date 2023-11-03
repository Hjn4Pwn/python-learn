'''
Với số nguyên n nhất định, hãy viết chương trình để tạo ra 
một dictionary chứa (i, i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này.
'''

n = int(input("Input: "))

result_dict = {}
for i in range(1, n+1):
    result_dict[i] = i*i

for key, value in result_dict.items():
    print(f"{key}: {value}")
