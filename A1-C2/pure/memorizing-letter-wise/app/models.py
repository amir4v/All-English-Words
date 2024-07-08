from django.db import models


class Word(models.Model):
    word = models.TextField(null=False, blank=False, unique=True, db_index=True)
    definition = models.TextField()
    synonyms = models.TextField()
    antonyms = models.TextField()
    letterized_1 = models.TextField()
    letterized_2 = models.TextField()
    letterized_3 = models.TextField()
    definitions = models.TextField()
    examples = models.TextField()
    
    rut = models.IntegerField(default=0)
    known = models.IntegerField(default=0)
    dont_know = models.IntegerField(default=0)
