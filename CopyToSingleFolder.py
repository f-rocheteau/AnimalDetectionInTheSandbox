import os
import shutil

def is_image_file(filename):
    img_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
    return any(filename.lower().endswith(ext) for ext in img_extensions)

def copy_files_to_single_directory(source_folder, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)  # Create destination folder if it doesn't exist

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if is_image_file(file) or file.endswith('.txt'):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(destination_folder, file)
                shutil.copy(src_file, dst_file)

if __name__ == "__main__":
    source_folder = r"C:\Users\Jackdon\Downloads\animals\train"
    destination_folder = r"C:\Users\Jackdon\Downloads\animals\train_combined"

    copy_files_to_single_directory(source_folder, destination_folder)
