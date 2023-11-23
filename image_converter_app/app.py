from flask import Flask, render_template, request
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        file = request.files['imageInput']
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            convert_and_save(filepath)
            message = f"Conversion successful. Image saved at {os.path.join(app.config['UPLOAD_FOLDER'], file.filename.replace('.png', '.jpg'))}"
    return render_template('index.html', message=message)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'png'

def convert_and_save(input_path):
    try:
        # Open the PNG image
        with Image.open(input_path) as img:
            # Convert to RGB mode (required for JPG)
            rgb_img = img.convert('RGB')

            # Create the 'jpg' directory if it doesn't exist
            output_directory = os.path.join(app.config['UPLOAD_FOLDER'], 'jpg')
            os.makedirs(output_directory, exist_ok=True)

            # Save as JPG with the same name in the 'jpg' directory
            output_path = os.path.join(output_directory, os.path.basename(input_path).replace(".png", ".jpg"))
            rgb_img.save(output_path, 'JPEG')

    except Exception as e:
        print(f"Error converting image: {e}")

if __name__ == '__main__':
    app.run(debug=True)
