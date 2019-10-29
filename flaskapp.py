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
    return 'Hello, this is OWI-Scheduler speaking ...<br> try <a href="./new_list">new_list</a>'


@app.route('/new_list', methods=['GET'])
def get_new_list():
    return jsonify(example_list)


if __name__ == "__main__":
    app.run()
