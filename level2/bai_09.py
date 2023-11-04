'''
Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.

Giả sử đầu vào là: Quản Trị Mạng
Thì đầu ra là:
Chữ hoa: 3
Chữ thường: 8

'''

char_count = {"uppercase": 0, "lowercase": 0}
user_input = input("Input your sentence: ")

for char in user_input:
    if char.isupper():
        char_count["uppercase"] += 1
    elif char.islower():
        char_count["lowercase"] += 1

print(f"In your sentence, there are {char_count['uppercase']} uppercase characters and {char_count['lowercase']} lowercase characters.")
