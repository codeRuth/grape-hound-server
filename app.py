"""Flask App Project."""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    json_data = {'Hello': 'World!'}
    return jsonify(json_data)

@app.route('/test')
def test():
    return jsonify({"message": "Hello World, Testing"})


if __name__ == '__main__':
    app.run()
