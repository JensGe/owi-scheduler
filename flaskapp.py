from flask import Flask, jsonify

app = Flask(__name__)

example_list = [
    {
        'meta': 'information',
        'length': 2,
        'urls': ['http://www.example.com', 'http://www.abc.com'],
    }
]


@app.route("/")
def hello_world():
    return 'Hello, try <a href="./url_frontier">url_frontier</a>'


@app.route('/url_frontier', methods=['GET'])
def get_new_list():
    return jsonify(example_list)


if __name__ == "__main__":
    app.run()
