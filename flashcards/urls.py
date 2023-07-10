""" 
    Controls all URLs from Flashcards App
"""
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.CardListView.as_view(), name="lista-de-cartoes")
]
