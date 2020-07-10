from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = {'Hello': 'World!'}
    return jsonify(json_data)

@app.route('/test')
def test():
    return jsonify({"message": "Hello World, Testing"})

@app.route('/process', methods=["POST"])
def process():
    print(request.body())
    return jsonify({"message": "Successful"})


if __name__ == '__main__':
    app.run()
