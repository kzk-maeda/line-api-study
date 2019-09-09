from flask import Flask, redirect, url_for, request, logging, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  # app.logger.warn('warning')
  return jsonify(name='John', email='john@mail.com')

@app.route('/', methods=['POST'])
def post_json():
  json_data = request.get_json()
  # app.logger.info(json_fata)
  return jsonify(json_data)

@app.route('/my', methods=['GET'])
def my_route_get():
  return 'get!'

@app.route('/my', methods=['POST'])
def my_route_post():
  return 'post!'

@app.route('/hello')
def hello():
  return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()