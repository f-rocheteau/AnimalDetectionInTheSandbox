import os
import random
import shutil

def copy_files_with_annotations(source_folder, dest_train, dest_val, dest_test, split_ratio=(0.8, 0.15, 0.05)):
    for root, dirs, files in os.walk(source_folder):
        if not files:
            continue
        
        # Create corresponding train, val, and test subfolders
        dest_train_subfolder = os.path.join(dest_train, os.path.relpath(root, source_folder))
        dest_val_subfolder = os.path.join(dest_val, os.path.relpath(root, source_folder))
        dest_test_subfolder = os.path.join(dest_test, os.path.relpath(root, source_folder))
        os.makedirs(dest_train_subfolder, exist_ok=True)
        os.makedirs(dest_val_subfolder, exist_ok=True)
        os.makedirs(dest_test_subfolder, exist_ok=True)

        # Shuffle the list of files
        random.shuffle(files)
        num_files = len(files)
        num_train = int(num_files * split_ratio[0])
        num_val = int(num_files * split_ratio[1])

        # Copy files to train folder
        for file in files[:num_train]:
            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(dest_train_subfolder, file)
            dest_annotation_path = os.path.join(dest_train_subfolder, f"{os.path.splitext(file)[0]}.txt")
            shutil.copy(src_file_path, dest_file_path)
            shutil.copy(f"{src_file_path[:-4]}.txt", dest_annotation_path)

        # Copy files to val folder
        for file in files[num_train:num_train + num_val]:
            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(dest_val_subfolder, file)
            dest_annotation_path = os.path.join(dest_val_subfolder, f"{os.path.splitext(file)[0]}.txt")
            shutil.copy(src_file_path, dest_file_path)
            shutil.copy(f"{src_file_path[:-4]}.txt", dest_annotation_path)

        # Copy files to test folder
        for file in files[num_train + num_val:]:
            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(dest_test_subfolder, file)
            dest_annotation_path = os.path.join(dest_test_subfolder, f"{os.path.splitext(file)[0]}.txt")
            shutil.copy(src_file_path, dest_file_path)
            shutil.copy(f"{src_file_path[:-4]}.txt", dest_annotation_path)

if __name__ == "__main__":
    source_folder = r"C:\Users\Jackdon\Downloads\animals\train_combined"
    dest_train = r"C:\Users\Jackdon\Downloads\animals\train_split\train1"
    dest_val = r"C:\Users\Jackdon\Downloads\animals\train_split\val1"
    dest_test = r"C:\Users\Jackdon\Downloads\animals\train_split\test1"

    copy_files_with_annotations(source_folder, dest_train, dest_val, dest_test, split_ratio=(0.8, 0.15, 0.05))
