import os

def normalize_coordinates(coords, image_width, image_height):
    x, y, w, h = coords
    normalized_x = x / image_width
    normalized_y = y / image_height
    normalized_w = w / image_width
    normalized_h = h / image_height
    return normalized_x, normalized_y, normalized_w, normalized_h

def recalculate_annotations(source_folder):
    image_files = []
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
                image_files.append(os.path.join(root, file))

    for image_path in image_files:
        annotation_path = image_path[:-4] + '.txt'
        if not os.path.exists(annotation_path):
            print(f"Annotation file not found for image: {image_path}")
            continue

        img_width, img_height = get_image_dimensions(image_path)

        # Read and update annotation coordinates
        with open(annotation_path, 'r') as f:
            annotation_lines = f.readlines()

        with open(annotation_path, 'w') as f:
            for line_num, line in enumerate(annotation_lines, start=1):
                line = line.strip()
                if not line:
                    continue

                values = line.split()
                if len(values) == 5:
                    class_name, x, y, w, h = values
                elif len(values) == 7:
                    class_name, _, _, x, y, w, h = values
                else:
                    print(f"Invalid annotation format in file '{annotation_path}' at line {line_num}: {line}")
                    continue

                x, y, w, h = float(x), float(y), float(w), float(h)
                normalized_coords = normalize_coordinates((x, y, w, h), img_width, img_height)
                f.write(f"{class_name} {normalized_coords[0]} {normalized_coords[1]} {normalized_coords[2]} {normalized_coords[3]}\n")

def get_image_dimensions(image_path):
    # Use PIL to get image dimensions
    from PIL import Image
    with Image.open(image_path) as img:
        return img.size

if __name__ == "__main__":
    source_folder = r"C:\Users\Jackdon\Downloads\animals\train_combined"

    recalculate_annotations(source_folder)

