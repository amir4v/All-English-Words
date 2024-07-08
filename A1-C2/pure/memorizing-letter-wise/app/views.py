import pickle
import random
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.utils.decorators import method_decorator

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import Word
from .first_letter import letterize, mini_letterize


class Words(View):
    def __init__(self):
        self.words = Word.objects.order_by('?')
        super().__init__()
    
    def word(self):
        word = self.words.order_by('?').first()
        word = {
            'id': word.id,
            'word': word.word,
            'definitions': word.definitions.replace(' . ', '.<br>'),
            'examples': word.examples.replace(' . ', '.<br>'),
            'synonyms': word.synonyms,
            'antonyms': word.antonyms,
        }
        word = json.dumps(word)
        return word
    
    def get(self, request):
        context = {'word': self.word(),}
        return render(request, 'app/words.html', context)
    
    def post(self, request):
        return HttpResponse(self.word())


class IndexView(View):
    def get(self, request):
        return render(request, 'app/index.html')
    
    @csrf_exempt
    def post(self, request):
        text = request.POST['text']
        separator = '\n'
        parts = 3
        display = False
        randomize = True
        results = letterize(text, separator=separator, parts=parts, display=display, randomize=randomize)
        
        return render(request, 'app/index.html', {'results': results})


class DoYouKnowView(View):
    def get(self, request):
        return render(request, 'app/do_you_know.html')
    
    def post(self, request):
        id = request.POST.get('id')
        _word = request.POST.get('word')
        direction = request.POST.get('direction')
        
        if all([id, _word, direction]):
            id = int(id)
            direction = int(direction)
            word = Word.objects.get(id=id, word=_word)
            word.rut += direction
            if direction == +1:
                word.known += 1
            if direction == -1:
                word.dont_know += 1
            word.save()
        
        words = Word.objects.filter(known=0, dont_know=0).order_by('?')
        word = words.first()
        count = words.count()
        
        json_renderer = JSONRenderer()
        json_response = json_renderer.render({'id': word.id, 'word': word.word, 'count': count})
        return HttpResponse(json_response)


# class YouDontKnowView


# class AllOfThemView


# class AllWithAbbreviations
