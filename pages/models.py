from django.db import models

class Page(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    last_update = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/pages/detail/%s/' % self.id
