from flask import Flask, request
from handler import validate_encrypt_request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"




@app.route('/encrypt', methods=['POST'])
def encrypt():
    requestJson = request.get_json()
    validate_encrypt_request(requestJson)
    sender = requestJson['sender']
    algorithm = requestJson['algorithm']
    message = requestJson['message']
    key = requestJson['key']
    typed = requestJson['type']
    # build response
    # 
    # 
    # 
    # 
    return 'response'

#  lancer l'application à travers la programmation depuis un autre fichier python
# from app import app
# app.run(port=3000)