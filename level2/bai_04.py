'''
Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng này 
thành chữ in hoa và in ra màn hình. Giả sử đầu vào là:

Hello world
Practice makes perfect

Thì đầu ra sẽ là:

HELLO WORLD
PRACTICE MAKES PERFECT
'''

lines = []

while True:
    input_str = input()
    if input_str:
        lines.append(input_str.upper())
    else:
        break

print("\n".join(lines))
