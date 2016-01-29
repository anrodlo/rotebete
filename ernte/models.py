from django.db import models

# Create your models here.

from django.db import models


class Ware(models.Model):
    name = models.CharField(max_length=64)
    menge = models.DecimalField(decimal_places=2, max_digits=5)
    einheit = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Abholstelle(models.Model):
    name = models.CharField(max_length=200)
    adresse = models.TextField()

    def __str__(self):
        return self.name

class Gruppe(models.Model):
    abholstelle = models.ForeignKey(Abholstelle, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ernteanteil(models.Model):
    bezahlt = models.BooleanField(default=False)
    gruppe = models.ForeignKey(Gruppe, on_delete=models.CASCADE)
    zahl = models.DecimalField(decimal_places=1, max_digits=2, choices=[(0.5, 'halbe'), (1, 'volle'), (2, 'doppelte')])
    extras = models.ManyToManyField(Ware)

    def __str__(self):
        return ", ".join(p.name for p in self.person_set.all())

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(default='', blank=True)
    adresse = models.TextField(default='', blank=True)
    ernteanteil = models.ManyToManyField(Ernteanteil)

    def __str__(self):
        return self.name

class Lieferung(models.Model):
    datum = models.DateTimeField()
    # TODO: note the amount
    waren = models.ManyToManyField(Ware, through="Warenlieferung")
    abholstelle = models.ForeignKey(Abholstelle, on_delete=models.CASCADE)

    def __str__(self):
        return "delivery to {} ({})".format(self.abholstelle, self.datum)

class Warenlieferung(models.Model):
    ware = models.ForeignKey(Ware, on_delete=models.CASCADE)
    lieferung = models.ForeignKey(Lieferung, on_delete=models.CASCADE)
    menge = models.DecimalField(decimal_places=2, max_digits=5)
