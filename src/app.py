from flask import Flask, request
from src.schemas import InputDataSchema

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def files_upload():
    try:
        data = request.form
        files = request.files
        print(files)
        print(len(data))
        if not data or not files:
            return {"error": "attached files not found."}, 400

        # here: logic to files upload

        return {"message": "files uploaded with success"}, 200
    except Exception as e:
        return {"error": str(e)}, 400
