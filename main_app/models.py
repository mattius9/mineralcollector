from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.

class Mineral(models.Model):
    name = models.CharField(max_length=100)
    m_class = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    hardness = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(10.0)])
    magnetic = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'mineral_id': self.id})
