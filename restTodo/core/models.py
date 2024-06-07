from django.db import models

# Create your models here.


class toDo(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=1000, blank=True)
    completed = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
