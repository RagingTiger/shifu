from flask import Flask
from flask import request
from flask import render_template
import handler
app = Flask(__name__)

@app.route('/')
def test_query():
    return 'Server is up and running!'

@app.route('/assessment_form_handler', methods=['POST', 'GET'])
def print_query():
    handler.assessment_form_response(request)
    return render_template('submitted.html')
