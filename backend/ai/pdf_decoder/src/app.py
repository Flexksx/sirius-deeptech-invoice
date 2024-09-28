from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/home/liviu/GigaHack24/sirius-deeptech-invoice/backend/database/FIles'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        # Check if the request has files
        if 'files' not in request.files:
            return jsonify({'error': 'No files part in the request'}), 400

        files = request.files.getlist('files')  # Get multiple files

        # Check if at least one file is uploaded
        if len(files) == 0:
            return jsonify({'error': 'No files uploaded'}), 400

        saved_files = []
        for file in files:
            # Save each file
            if file and allowed_file(file.filename):
                filename = file.filename
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                saved_files.append(filename)
            else:
                return jsonify({'error': 'File type not allowed'}), 400
        return jsonify({'message': 'Files successfully uploaded', 'files': saved_files}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt', 'png', 'jpg'}  # Allowed file types
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
