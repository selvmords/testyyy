from django.db import models
from datetime import date
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator, MaxValueValidator

class Filmy(models.Model):
    title = models.CharField(max_length=70)
    genre = models.CharField(max_length=70)
    premiere = models.DateField(default=date.today)
    review = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.title

    def title_by_genre(self):
        """ Zwraca tytul i gatunek """
        return f"{self.title} to gatunek: {self.genre}"

    def is_review_correct(self):
        """ Sprawdza czy ocena jest prawidlowa """
        return self.review >= 11

    def is_oldschool(self):
        """ Sprawdza czy film jest starszy niz 40 lat """
        return (datetime.now().date() - self.premiere) <= timedelta(days=14400)