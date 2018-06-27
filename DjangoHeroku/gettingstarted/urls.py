from django.conf.urls import include, url
from django.urls import path

import hello.views

#My Url PAtterns
urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    #apis
    url(r'^word_to_check', hello.views.word_to_check, name='word_to_check'),
]
