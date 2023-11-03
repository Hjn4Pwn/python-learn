'''
My script has some logical bugs, so I'm just using it for simple task
'''


import os
import subprocess

folder_name = input("Input your folder name: ")
number_of_file = int(input("Input your number files: "))
template_file_name = input(
    "Input your template (when X will be replaced like baiX.py => bai123.py): ")

solution = int(
    input("Input your choose 1 or 2 for difference solution but just one result: "))


match solution:
    case 1:
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        for i in range(1, number_of_file + 1):
            file_name = template_file_name.replace("X", str(i))
            with open(os.path.join(folder_name, file_name), "w") as file:
                file.write(f"# file number: {i}")
        print(f"Created {number_of_file} files in folder {folder_name}")

    case _:
        subprocess.run(["mkdir", folder_name])

        for i in range(1, number_of_file + 1):
            file_name = template_file_name.replace("X", str(i))
            subprocess(["touch", os.path.join(folder_name, file_name)])

        print(f"Created {number_of_file} files in folder {folder_name}")
