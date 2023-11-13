from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=400)
    image=models.ImageField()
    release_date=models.DateField()
    plot=models.CharField(max_length=1500)

    def __str__(self):
        return self.title

class favorite(models.Model):
    title=models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

