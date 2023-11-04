'''
Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó. 

Giả sử đầu vào sau được cấp cho chương trình: hello world! 123
Thì đầu ra sẽ là:
Số chữ cái là: 10
Số chữ số là: 3
'''


char_count = {"digits": 0, "letters": 0}

user_input = input("Input your sentence: ")

for char in user_input:
    if char.isdigit():
        char_count["digits"] += 1
    elif char.isalpha():
        char_count['letters'] += 1

print(
    f"In your sentence, there are {char_count['digits']} digits and {char_count['letters']} letters.")
