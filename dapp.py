from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Set a folder to store uploaded files temporarily
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store the file paths in an array (for example)
selected_files_array = []

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/upload', methods=['POST'])
def upload_files():
    global selected_files_array
    if 'files' not in request.files:
        return "No file part", 400
    
    files = request.files.getlist('files')
    
    # Store the selected file paths in an array (just as an example, you can also store the files themselves)
    selected_files_array = [file.filename for file in files]

    # Optionally, you can save files to the server
    for file in files:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    
    return f'Files uploaded: {", ".join(selected_files_array)}'

if __name__ == '__main__':
    app.run(debug=True)
