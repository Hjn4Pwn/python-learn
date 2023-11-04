import subprocess
import os
folder_name = input("Input your folder name: ")
from_num, to_num = map(int, input(
    "Input distance of file to push like 5 7 for push file-5, file-6, file-7: ").split(" "))
tempalte_file_name = "bai_X.py"
num_files = input("Input number files of working folder: ")

for i in range(from_num, to_num + 1):
    formatted_i = f"{i:0{len(num_files)}}"
    file_name = tempalte_file_name.replace("X", formatted_i)

    relative_path_file = os.path.join(folder_name, file_name)
    subprocess.run(["git", "add", relative_path_file])

    commit_message = "update"
    subprocess.run(["git", "commit", "-m", commit_message])

    subprocess.run(["git", "push", "origin", "master"])


# code này nhầm mục đích luyện python, sẵn tiền buff tí commit
# thay vì add .  thì add từng file ăn gian tí thuiii
