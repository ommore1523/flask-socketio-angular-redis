from flask import Flask,jsonify
from . import send_socket

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def socket():
    for i in range(10):
        print(f'message {i}')
        send_socket("process1","/xtest",13,"test","hello socket")
    return jsonify({"msg":"api_data"})

if __name__ != '__main__':
  app.run()