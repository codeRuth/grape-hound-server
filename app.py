from flask import Flask, jsonify, request
import json
import base64, os
import uuid

app = Flask(__name__)

FILE_UPLOAD_DIR = '/uploads/'

@app.route('/')
def index():
    json_data = {'message': 'Hello World!'}
    return jsonify(json_data)

@app.route('/test')
def test():
    return jsonify({"message": "Hello World, Testing"})

@app.route('/process', methods=["POST"])
def process():
    data = json.loads(request.data)
    imageData = data['img']
    type = data['type']
    image = base64.b64decode(str(imageData))
    file_name = str(uuid.uuid4().hex)
    with open(os.path.join(os.path.dirname(__file__) + FILE_UPLOAD_DIR, file_name + ".png"), 'wb+') as f:
        f.write(image)
    return jsonify({"message": "Image saved Successful"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = True)
