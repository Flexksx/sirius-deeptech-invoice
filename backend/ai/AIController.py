from concurrent.futures import ThreadPoolExecutor, as_completed
from flask import Flask, request, jsonify, Blueprint
import os
from .ContractDecoder import ContractDecoder

ai_blueprint = Blueprint('ai_blueprint', __name__)

UPLOAD_DIR_PATH = os.path.join(os.path.dirname(__file__), "./res")

if not os.path.exists(UPLOAD_DIR_PATH):
    os.makedirs(UPLOAD_DIR_PATH)

@ai_blueprint.route('/upload', methods=['POST'])
def upload_files():
    try:
        if 'files' not in request.files:
            return jsonify({'error': 'No files part in the request'}), 400

        files = request.files.getlist('files')
        if len(files) == 1 and files[0].filename == '' or len(files) == 0:
            return jsonify({'error': 'No files uploaded'}), 400

        files_to_process = []
        for file in files:
            if file and allowed_file(file.filename):
                filename = file.filename
                file_path = os.path.join(
                    UPLOAD_DIR_PATH, filename)
                file.save(file_path)
                files_to_process.append(file_path)
            else:
                return jsonify({'error': 'File type not allowed'}), 400

        contract_decoder = ContractDecoder()
        results = []

        with ThreadPoolExecutor() as executor:
            future_to_file = {executor.submit(
                contract_decoder.decode_file, file_path): file_path for file_path in files_to_process}
            for future in as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    print(f'Error decoding file {file_path}: {e}')
                    results.append({'file': file_path, 'error': str(e)})

        print(results)
        return jsonify({'status': 'success', 'data': results}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx',
                          'txt', 'png', 'jpg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    ai_blueprint.run(debug=True)
