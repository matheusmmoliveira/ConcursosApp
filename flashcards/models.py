"""
    Database models for the Flashcard App
"""

from django.db import models

class Assunto(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
