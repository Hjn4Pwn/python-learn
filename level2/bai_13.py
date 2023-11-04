'''
Viết chương trình Python nhập một dãy số nguyên, sau đó kiểm tra xem nó có khả đối xứng không? 
Nếu có, hãy biến đổi nó để được một dãy đối xứng.
'''

input_list = [int(x) for x in input("Input your list of numbers: ").split(" ")]
if input_list == input_list[::-1]:
    print("The list is a palindrome.")


# Đề bài này không được chặt chẽ cho lắm, cơ mà vấn đề ở đây có lẻ để nhắc
# chúng ta nhớ syntax [::-1] chứ còn logic code cho việc đổi xứng thì không phải vấn đề
