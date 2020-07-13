import json
from flask import Flask, jsonify, request
from src.prediction import predict_disease

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
    image_data = data['img']
    detection_type = data['type']
    # image = base64.b64decode(str(imageData))
    # file_name = str(uuid.uuid4().hex)
    # with open(os.path.join(os.path.dirname(__file__) + FILE_UPLOAD_DIR, file_name + ".png"), 'wb+') as f:
    #     f.write(image)
    return jsonify({"image": image_data})


if __name__ == '__main__':
    # app.run(host="0.0.0.0", debug = True)
    # print(os.path.join("./uploads/48964b70121a4122ba03ca147685a864.png"))
    predict_disease()
