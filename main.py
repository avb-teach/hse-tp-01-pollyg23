import os
import shutil
import sys

def copy_flat(input_dir, output_dir):
    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)

    for root, dirs, files in os.walk(input_dir):
       
        if output_dir.startswith(root):
            dirs[:] = [d for d in dirs if os.path.abspath(os.path.join(root, d)) != output_dir]

        for file in files:
            source_path = os.path.join(root, file)
            target_path = os.path.join(output_dir, file)

          
            if os.path.exists(target_path):
                name, ext = os.path.splitext(file)
                count = 1
                while True:
                    new_name = f"{name}_{count}{ext}"
                    target_path = os.path.join(output_dir, new_name)
                    if not os.path.exists(target_path):
                        break
                    count += 1

            shutil.copy2(source_path, target_path)

if len(sys.argv) < 3:
    print("Usage: main.py input_dir output_dir")
    sys.exit(1)

input_dir = sys.argv[1]
output_dir = sys.argv[2]

if not os.path.isdir(input_dir):
    print(f"Ошибка: директория {input_dir} не существует.")
    sys.exit(1)

os.makedirs(output_dir, exist_ok=True)

copy_flat(input_dir, output_dir)
