from django.db import models


class Haiku(models.Model):
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    title = models.CharField(max_length=256)
    url_title = models.CharField(max_length=32, default='hello')
    image = models.ImageField(upload_to="/media/haiku/", blank=True)

    line_one = models.CharField(max_length=64)
    line_two = models.CharField(max_length=64)
    line_three = models.CharField(max_length=64)

    text = models.TextField()

    def __str__(self):
        return "%s" %(self.title)

    class Meta:
        verbose_name = "Haiku"
        verbose_name_plural = "Haiku's"
