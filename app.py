# from flask import Flask, render_template, request, send_file
# from PIL import Image
# import os
# import io
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'uploads')

# def convert_and_save(input_path, output_format, quality):
#     try:
#         with Image.open(input_path) as img:
#             output_directory = os.path.join(app.config['UPLOAD_FOLDER'], output_format)
#             os.makedirs(output_directory, exist_ok=True)

#             if output_format == 'original':
#                 output_path = os.path.join(output_directory, os.path.basename(input_path))
#                 if input_path.lower().endswith('.png'):
#                     img.save(output_path, optimize=True, quality=quality)
#                 else:
#                     img.save(output_path)
#             else:
#                 if output_format == 'jpg':
#                     rgb_img = img.convert('RGB')
#                     output_path = os.path.join(output_directory, os.path.basename(input_path).replace(os.path.splitext(input_path)[1], '.jpg'))
#                     rgb_img.save(output_path, 'JPEG', quality=quality)
#                 else:
#                     output_path = os.path.join(output_directory, os.path.basename(input_path).replace(os.path.splitext(input_path)[1], f'.{output_format}'))
#                     img.save(output_path, output_format.upper(), quality=quality)

#             os.remove(input_path)  # Delete the original file after conversion
#     except Exception as e:
#         print(f"Error converting/compressing image: {e}")

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         try:
#             file = request.files.get('imageInput')
#             output_format = request.form.get('outputFormat')
#             quality = request.form.get('quality', type=int)
            
#             if not file or not output_format or quality is None:
#                 raise ValueError("Missing input fields")

#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'original', file.filename)
#             os.makedirs(os.path.dirname(filepath), exist_ok=True)
#             file.save(filepath)
#             convert_and_save(filepath, output_format, quality)
#             return render_template('index.html', message="Image successfully converted/compressed.")
#         except ValueError as ve:
#             return render_template('index.html', message=str(ve))
#         except Exception as e:
#             print(f"Unexpected error: {e}")
#             return render_template('index.html', message="An unexpected error occurred. Please try again.")
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, render_template, request
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def convert_and_save(input_path, output_format, quality):
    try:
        with Image.open(input_path) as img:
            output_directory = os.path.join(app.config['UPLOAD_FOLDER'], output_format)
            os.makedirs(output_directory, exist_ok=True)

            if output_format == 'original':
                output_path = os.path.join(output_directory, os.path.basename(input_path))
                if input_path.lower().endswith('.png'):
                    img.save(output_path, optimize=True, quality=quality)
                else:
                    img.save(output_path)
            else:
                if output_format == 'jpg':
                    rgb_img = img.convert('RGB')
                    output_path = os.path.join(output_directory, os.path.basename(input_path).replace(os.path.splitext(input_path)[1], '.jpg'))
                    rgb_img.save(output_path, 'JPEG', quality=quality)
                else:
                    output_path = os.path.join(output_directory, os.path.basename(input_path).replace(os.path.splitext(input_path)[1], f'.{output_format}'))
                    img.save(output_path, output_format.upper(), quality=quality)

    except Exception as e:
        print(f"Error converting/compressing image: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('imageInput')
        output_format = request.form.get('outputFormat')
        quality = request.form.get('quality', type=int)
        
        if not file or not output_format or quality is None:
            return render_template('index.html', message="Missing input fields. Please try again.")
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'original', file.filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        file.save(filepath)
        convert_and_save(filepath, output_format, quality)
        return render_template('index.html', message=f"Image successfully converted/compressed.")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
