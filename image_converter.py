# Simple python image converter (PNG to JPG)
from PIL import Image
import os

# def convert_png_to_jpg(path):
#     for filename in os.listdir(path):
#         if filename.endswith('.png'):
#             img = Image.open(f'{path}{filename}')
#             clean_name = os.path.splitext(filename)[0]
#             img.save(f'{path}{clean_name}.jpg', 'jpeg')
#             print('All done!')

def convert_png_to_jpg(input_path, output_path):
    try:
        # Open the PNG image
        with Image.open(input_path) as img:
            # Convert the image to RGB mode (required for JPG)
            rgb_img = img.convert('RGB')

            # Save the JPG
            rgb_img.save(output_path, format='JPEG', quality=90)

        print(f"Saved JPG image to {output_path}")

    except Exception as e:
        print(f"Unable to convert {input_path} to JPG")
        print(e)

# if __name__ == '__main__':
#     convert_png_to_jpg('./images/png/canvas.png', './images/jpg/canvas.jpg')

# Example
input_image_path = 'canvas.png'
output_image_path = 'canvas.jpg'

convert_png_to_jpg(input_image_path, output_image_path)