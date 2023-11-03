'''
Viết chương trình nhập: số giờ làm mỗi tuần, thù lao trên mỗi giờ làm tiêu chuẩn,
từ đó tính ra số tiền thực lĩnh của nhân viên. Biết rằng: số giờ tiêu chuẩn mỗi tuần là 44 giờ, 
và mỗi giờ vượt chuẩn được trả gấp rưỡi so với giờ làm chuẩn.

'''

hour_for_working = int(input("Input your hour for working: "))
cost = int(input("Input cost per hour: "))

if hour_for_working > 44:
    print(f"Your salary is: {44*cost + (hour_for_working-44)*cost*1.5}")
else:
    print(f"Your salary is: {hour_for_working*cost}")
