'''
Câu hỏi: Tính tuổi dựa trên ngày tháng năm sinh nhập vào.

Ví dụ: Nhập vào ngày tháng năm sinh dạng y/m/d, hãy tính tuổi của người này.

Gợi ý: Sử dụng module datetime. Sử dụng datetime, chúng ta có thể tìm tuổi bằng cách trừ năm sinh cho năm hiện tại.
'''

import datetime as dt

birth_day = input("Input your birthday (yy/mm/dd): ")

arr = []

arr = birth_day.split("/")

print(f"Now is {dt.date.today()}")

if dt.date.today().month > int(arr[1]):
    print(f"Your age is: {dt.date.today().year - int(arr[0])}+")
else:
    print(f"Your age is: {dt.date.today().year - int(arr[0])}-")
