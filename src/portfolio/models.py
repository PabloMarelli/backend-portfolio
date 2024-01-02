from django.db import models

# Create your models here.

class Resumee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    summary = models.TextField()
    experience = models.ForeignKey('Experience', on_delete=models.CASCADE)
    education = models.TextField()
    projects = models.TextField()
    links = models.TextField()
    languages = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    reference = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
