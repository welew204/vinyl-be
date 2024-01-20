from django.db import models

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    bringer = models.CharField(max_length=120)
    # bringer will be foreign keyed to the user model

    def _str_(self):
        return self.title