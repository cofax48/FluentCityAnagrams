#Flask app: serve apis, gets data from my db and connect my homepage
import datetime
import os
#El Classico
from flask import Flask, abort
from flask import request, render_template
from flask import jsonify
from flask import Response
from sqlalchemy import create_engine
#fancy dictionary sorting
from operator import itemgetter
#Self explanatory
import json
from datetime import datetime
import time
#Gets db params
from database import engine
from anagram_algorithm import is_string_a_word_checker

#intializes app and connects to my database
app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']
conn = engine.connect()

#Homepage
@app.route("/", methods=['GET'])
def index():
    return render_template('Homepage.html')

#APIs
#Gets word from client-runs the anagram algorithm and returns anagrams as json
@app.route("/word_to_check", methods=['POST'])
def anagram_word_api():
    if request.method == 'POST':
        data = json.loads(request.data.decode())
        fields = [i for i in data]
        expected_fields = ["word"]
        #If the expected data params equal the approved data params for this api then we proceeed
        if expected_fields == fields:
            word_to_check = data["word"]
            list_of_anagrams = is_string_a_word_checker(word_to_check, conn)
            return jsonify(list_of_anagrams)
        else:
            #if the data is not formatted for the api right then this is sent
            return abort(400)
    #returns if request is not "post"
    return abort(405)

#Gets the party started
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)
