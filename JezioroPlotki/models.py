from django.db import models

class Link(models.Model):
    title = models.CharField(max_length=50)
    link = models.TextField()

    def str(self):
        return self.title

    def get_absolute_url(self):
        return self.link