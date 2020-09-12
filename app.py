from flask import Flask
from flask import jsonify
from functions import get_full_person
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!", 200

@app.route('/random-person')
def get_person():
    data = get_full_person()
    return jsonify(data)

# We only need this for local development.
if __name__ == '__main__':
    app.run()