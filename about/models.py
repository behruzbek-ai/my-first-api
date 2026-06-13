from django.db import models

class About(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Technology(models.Model):
    name = models.CharField(max_length=100)
    year_of_manufacture = models.IntegerField()
    model_number = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name




