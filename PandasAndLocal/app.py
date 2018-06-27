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
#for handling nan types in data
from numpy import nansum
from pandas import isnull
#Gets db params
#from database import engine

import pandas as pd
import itertools



#dictionary_initialization
#imports the text file as a pandas datafram object-not the fastest format-but certainly the easiest to work with later on
df = pd.read_csv('dictionary.txt', sep=" ", dtype=str, header=None)
#adds a column name-Word
df.rename(columns={0:"Word"}, inplace=True)
#Makes all items in the word column strings-initially imported as floats
df["Word"] = df["Word"].astype(str)
#generates a word_length column that has the length of every word in the dictionary
df["word_length"] = df["Word"].apply(len)

def word_in_dictionary(word_to_check):
    #creates a variable that captures the length of the submitted word
    word_length = len(word_to_check)
    #generates a new dataframe comprised only of words that are the same length as the submitted word
    word_list_of_equal_length_words = df.loc[df["word_length"] == word_length]
    #determines whether or not the submitted word is in fact a word
    word_truthiness = '{}'.format(word_to_check) in word_list_of_equal_length_words.values
    #returns a boolean on the word
    return word_truthiness

def anagrams_of_word(word_to_check):
    #creates a variable that captures the length of the submitted word
    word_length = len(word_to_check)
    #generates a new dataframe comprised only of words that are the same length as the submitted word
    #this is done so that comparisons are done only for relevent words (shorter or longer words can't be anagrams)
    word_list_of_equal_length_words = df.loc[df["word_length"] == word_length]

    #intializes a list of all words that are found
    anagrams_that_are_words = []

    #gets a list of all the letters that are in the word being evaluated
    whole_word_character_list = sorted([letter for letter in word_to_check])
    #genrates a list of the dataframe created that contains all words of the same length
    equal_length_words = list(word_list_of_equal_length_words.values.flatten())
    #iterates through the list of equal length words
    for words in equal_length_words:
        #generates a sorted listed of all letters in the iterated word
        letters = sorted([letter for letter in str(words)])
        #checks if the list of letters from the iterated word equals the list of letters the word being evaluated
        if letters == whole_word_character_list:
            #if both lists are equal (meaning a known words containes the same letters as the word being evaluated-it means they're anagrams of each other)
            anagrams_that_are_words.append(words)

    return anagrams_that_are_words

def is_string_a_word_checker(word_to_check):
    #No items in the dictionary were fewer than 4 letters or longer than 12, so no point in searching for something that isn't there
    if len(word_to_check) < 4:
        return 'None: No word in dictionary is shorter than 4 letters'
    elif len(word_to_check) > 12:
        return 'None: No word in dictionary is longer than 12 letters'
    else:
        word_to_check = word_to_check.lower()
        word_truthiness = word_in_dictionary(word_to_check)
        #print(word_to_check)
        #print(word_truthiness)
        if word_truthiness == True:
            list_of_anagrams_that_are_words = anagrams_of_word(word_to_check)
            sorted_list_of_anagrams_that_are_words_by_second_letter = sorted(list_of_anagrams_that_are_words, key=itemgetter(1))
            return sorted_list_of_anagrams_that_are_words_by_second_letter
        else:
            return 'None: The word is not found in the dictionary'

#intializes app and connects to my database
app = Flask(__name__)

#Homepage
@app.route("/", methods=['GET'])
def index():
    return render_template('Homepage.html')

#APIs
#Gets all of a players records for a specific category over the course of their career
@app.route("/word_to_check", methods=['POST'])
def category_over_player_career():
    if request.method == 'POST':
        data = json.loads(request.data.decode())

        fields = [i for i in data]
        expected_fields = ["word"]
        #If the expected data params equal the approved data params for this api then we proceeed
        if expected_fields == fields:
            word_to_check = data["word"]

            list_of_anagrams = is_string_a_word_checker(word_to_check)
            return jsonify(list_of_anagrams)
        else:
            #if the data is formatted for the api right then this is sent
            return abort(400)
    #returns if request is not "post"
    return abort(405)

#Gets the party started
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)
