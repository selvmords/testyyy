from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    popular = models.IntegerField(default=0)

    def __str__(self):
        return self.title


    def is_popular(self):
        """Zwraca True, jeśli książka została wypożyczona więcej niż 100 razy."""
        # Zwraca wartość logiczną True, jeśli liczba wypożyczeń przekracza 100.
        return self.popular > 1



