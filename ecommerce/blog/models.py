from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length = 1000)
    creation_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=40)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'