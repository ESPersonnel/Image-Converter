# Simple python image converter (PNG to JPG)
from tkinter import Tk, filedialog, Label, Button
from PIL import Image
import os

# def convert_png_to_jpg(input_path, output_path):
#     try:
#         # Open the PNG image
#         with Image.open(input_path) as img:
#             # Convert the image to RGB mode (required for JPG)
#             rgb_img = img.convert('RGB')

#             # Save the JPG
#             rgb_img.save(output_path, format='JPEG', quality=90)

#         print(f"Saved JPG image to {output_path}")

#     except Exception as e:
#         print(f"Unable to convert {input_path} to JPG")
#         print(e)


# # Example
# input_image_path = './images/png/canvas.png'
# output_image_path = './images/jpg/canvas.jpg'

# convert_png_to_jpg(input_image_path, output_image_path)

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter")

        self.label = Label(root, text="Choose a PNG image to convert:")
        self.label.pack(pady=10)

        self.button = Button(root, text="Choose PNG", command=self.choose_png)
        self.button.pack(pady=10)

    def choose_png(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PNG Files", "*.png")],
            title="Choose a PNG image"
        )
        if file_path:
            self.convert_and_save(file_path)

    def convert_and_save(self, input_path):
        # output_path = os.path.splitext(input_path)[0] + ".jpg"
        try:
            # Open the PNG image
            with Image.open(input_path) as img:
                # Convert the image to RGB mode (required for JPG)
                rgb_img = img.convert('RGB')

                # Create the 'jpg' directory if it doesn't exist
                output_dir = os.path.join(os.path.dirname(os.path.abspath(input_path)), "..", "jpg")
                os.makedirs(output_dir, exist_ok=True)

                # Save as JPG with the same name in the 'jpg' directory
                output_path = os.path.join(output_dir, os.path.basename(input_path).replace(".png", ".jpg"))
                rgb_img.save(output_path, format='JPEG', quality=90)

            self.display_message(f"Conversion successful! Saved JPG image to {output_path}")

        except Exception as e:
            print(f"Unable to convert {input_path} to JPG")
            print(e)

    def display_message(self, message):
        result_label = Label(self.root, text=message, fg="green")
        result_label.pack(pady=10)


if __name__ == "__main__":
    root = Tk()
    app = ImageConverterApp(root)
    root.mainloop()