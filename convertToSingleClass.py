import os

def replace_words_with_zero(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):  # Check if the file is a .txt file
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()

                # Replace complete words with two or more consecutive alphanumeric characters with "0"
                modified_lines = []
                for line in lines:
                    words = line.strip().split()
                    modified_words = [word if not word.isalnum() or len(word) < 2 else '0' for word in words]
                    modified_line = ' '.join(modified_words) + '\n'
                    modified_lines.append(modified_line)

                with open(file_path, 'w') as f:
                    f.writelines(modified_lines)

if __name__ == "__main__":
    folder_path = r"C:\Users\Jackdon\Downloads\animals\train_combined"
    replace_words_with_zero(folder_path)
