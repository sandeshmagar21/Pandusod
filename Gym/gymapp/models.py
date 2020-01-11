from django.db import models

from django.db import models
class Gym(models.Model):
    workoutname = models.CharField(max_length = 50) 
    picture = models.ImageField()
    email = models.EmailField(blank = False) 
    workoutdesc = models.TextField(default = '')
    def __str__(self):
        return self.workoutname