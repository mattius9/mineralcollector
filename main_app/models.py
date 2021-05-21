from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
LEVELS = (
    ('L','Low Risk' ),
    ('R', 'Restricted'),
    ('T', 'Top Secret')
)

class Tool(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tools_detail', kwargs={'pk': self.id})

class Mineral(models.Model):
    name = models.CharField(max_length=100)
    m_class = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    hardness = models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(10.0)])
    tools = models.ManyToManyField(Tool)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'mineral_id': self.id})

class Viewing(models.Model):
    date = models.DateField('viewing date')
    visitor = models.CharField(max_length=50)
    level = models.CharField(
        max_length=1,
            choices=LEVELS,
            default=LEVELS[0][0]
    )
    
    mineral = models.ForeignKey(Mineral, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.visitor} - {self.get_level_display()} on {self.date}"

    class Meta:
        ordering = ['-date']