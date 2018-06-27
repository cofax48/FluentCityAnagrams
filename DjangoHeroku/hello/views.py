from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.http import JsonResponse
#Don't want to deal with CSRF
from django.views.decorators.csrf import csrf_exempt
#El classico
import json
from sqlalchemy import create_engine
#fancy dictionary sorting
from operator import itemgetter
#for handling nan types in data
from numpy import nansum
from pandas import isnull
#Where my anagram_algorithm is located
from .anagram_algorithm import is_string_a_word_checker

#connects to my database
engine = create_engine('postgres://iwogouitiuowon:a1e97051f3c10aff7a0d0fedcaf759a7b259be0130e4a6b1790ed5c6c70a02e1@ec2-54-221-220-59.compute-1.amazonaws.com:5432/daepj190brg9i7')#10 million rows
conn = engine.connect()

# My views are here.
@csrf_exempt #As this is an unpaid proejct I'm skipping CSRF Protocal
def index(request):
    return render(request, 'Homepage.html')

#APIs

#Gets word from client-runs the anagram algorithm and returns anagrams as json
@csrf_exempt
def word_to_check(request):
    data = json.loads(request.body.decode('utf-8'))
    fields = [i for i in data]
    expected_fields = ["word"]
    #If the expected data params equal the approved data params for this api then we proceeed
    if expected_fields == fields:
        word_to_check = data["word"]
        list_of_anagrams = is_string_a_word_checker(word_to_check, conn)

        return JsonResponse(list_of_anagrams, safe=False)
