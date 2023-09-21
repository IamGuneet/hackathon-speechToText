from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_audio():
    try:
        # Check if the POST request contains a file named 'audio'
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400

        audio_file = request.files['audio']

        # Check if the file is empty
        if audio_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Define the directory where you want to save the uploaded audio files
        upload_dir = 'uploads'

        # Save the uploaded audio file to the specified directory
        audio_file.save(f'{upload_dir}/{audio_file.filename}')

        return jsonify({'message': 'Audio file uploaded successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
