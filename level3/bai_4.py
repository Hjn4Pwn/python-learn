'''
Một Robot di chuyển trong mặt phẳng bắt đầu từ điểm đầu tiên (0,0). 
Robot có thể di chuyển theo hướng UP, DOWN, LEFT và RIGHT với những bước nhất định. 
Dấu di chuyển của robot được đánh hiển thị như sau:
UP 5
DOWN 3
LEFT 3
RIGHT 3
Các con số sau phía sau hướng di chuyển chính là số bước đi. 
Hãy viết chương trình để tính toán khoảng cách từ vị trí hiện tại đến vị trí đầu tiên, 
sau khi robot đã di chuyển một quãng đường. 
Nếu khoảng cách là một số thập phân chỉ cần in só nguyên gần nhất.
Ví dụ: Nếu tuple sau đây là input của chương trình:

UP 5
DOWN 3
LEFT 3
RIGHT 2
thì đầu ra sẽ là 2.
'''

import math

pos = [0, 0]

while True:
    s = input()
    if not s:
        break
    move = s.split(" ")
    steps = int(move[1])
    match move[0]:
        case "UP":
            pos[0] += steps
        case "DOWN":
            pos[0] -= steps
        case "LEFT":
            pos[1] -= steps
        case "RIGHT":
            pos[1] += steps
        case _:
            pass

print(round(math.sqrt(pos[0]**2 + pos[1]**2)))
