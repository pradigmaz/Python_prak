import os

os.makedirs("test_dir/f1", exist_ok=True)

file_path_exists = "test_dir/f1/4.txt"

with open(file_path_exists, 'w') as f:
    f.write("hello")

def check_file(path_to_file):

    print(f"Проверка пути: '{path_to_file}'")

    if os.path.exists(path_to_file):

        file_name = os.path.basename(path_to_file)

        dir_name = os.path.dirname(path_to_file)

        access_time = os.path.getatime(path_to_file)

        print(f"{file_name} ({dir_name}) - last access time {access_time} sec")
        
    else:

        print(f"Сообщение: Файл '{path_to_file}' не найден.")

check_file("test_dir/f1/4.txt")

check_file("non_existent_file.txt")