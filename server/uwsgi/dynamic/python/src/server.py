from flask import Flask
from flask import redirect
from flask import request
import handler
app = Flask(__name__)

@app.route('/')
def test_query():
    return 'Server is up and running!'

@app.route('/assessment_form_handler', methods=['POST', 'GET'])
def print_query():
    handler.assessment_form_response(request)
    return redirect("/submitted.html", code=302)
