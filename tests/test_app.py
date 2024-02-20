import io
from unittest import TestCase
from src.app import app


class TestApp(TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_upload_without_attached_files(self):
        response = self.client.post('/upload')
        self.assertEqual(400, response.status_code)
        self.assertEqual('{"error":"attached files not found."}\n', response.text)

    def test_upload_one_attached_file(self):
        file_1_csv = (io.BytesIO(b"training file content example...")), "training.csv"
        response = self.client.post('/upload', data={"files": file_1_csv}, content_type="multipart/form-data")
        self.assertEqual(400, response.status_code)
        self.assertEqual('{"error":"attached files not found."}\n', response.text)

    def test_upload_two_attached_file_without_params(self):
        file_1_csv = (io.BytesIO(b"training file content example...")), "training.csv"
        file_2_csv = (io.BytesIO(b"model file content example...")), "model.onnx"
        response = self.client.post('/upload', data={"files": [file_1_csv, file_2_csv]}, content_type="multipart/form-data")
        self.assertEqual(200, response.status_code)
