from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
    path('words/', csrf_exempt(views.Words.as_view()), name='words'),
    
    path('do-you-know/', csrf_exempt(views.DoYouKnowView.as_view()), name='do_you_know'),
    # path('you-dont-know/', views.YouDontKnowView.as_view(), name='you_dont_know'),
    
    # path('all-of-them', views.AllOfThemView.as_view(), name='all_of_them'),
    # path('all-with-abbreviation', views.AllWithAbbreviations.as_view(), name='all_with_abbreviations'),
]

"""
    - just show the words and ask if you know it or not and save these iknow or i don't know status as a counter.
    - in a page just show those words that i do not know them with all the description.
    
    - in a page just show all of them with all the description.
    - all of them with just abbreviations like before.
"""
