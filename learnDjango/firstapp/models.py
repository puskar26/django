from django.db import models
from django.utils import timezone

# Create your models here.

class SuperHeroes(models.Model):
    SUPERHEROES_NAME = [
        ('CA', 'CAPTAIN AMERICA'),
        ('IM', 'IRON MAN'),
        ('SM', 'SUPERMAN'),
        ('BM', 'BATMAN'),
        ('TR', 'THOR'),
        ('HL', 'HULK'),
    ]
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='firstapp/')
    date_added = models.DateTimeField(default = timezone.now)
    type = models.CharField(max_length = 2, choices = SUPERHEROES_NAME)
    
    def __str__(self):
        return self.name