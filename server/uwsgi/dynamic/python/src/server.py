from flask import Flask
from flask import request
import handler
app = Flask(__name__)

@app.route('/')
def test_query():
    return 'Server is up and running!'

@app.route('/contactform_handler', methods=['POST', 'GET'])
def print_query():
    handler.contactform(request)
    return 'Contact data received!'
