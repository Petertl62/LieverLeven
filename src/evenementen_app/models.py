from django.db import models


class Evenement(models.Model):
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    title = models.CharField(max_length=256)
    url_title = models.CharField(max_length=256, default='title', unique=True)
    image = models.ImageField(upload_to='/media/evenement/', blank=True)

    tijdstip = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-tijdstip']
        verbose_name = 'Evenement'
        verbose_name_plural = 'Evenementen'

class Inschrijving(models.Model):
    evenement = models.ForeignKey('Evenement')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    voornaam = models.CharField(max_length=64)
    achternaam = models.CharField(max_length=64)
    email = models.EmailField()
    telefoon = models.CharField(max_length=64)
    bericht = models.TextField()

    def __str__(self):
        return "%s %s, %s" %(self.voornaam, self.achternaam, self.evenement.title)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Inschrijving'
        verbose_name_plural = 'Inschrijvingen'
