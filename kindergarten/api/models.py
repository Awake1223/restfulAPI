from django.db import models

class Parent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    parent = models.ForeignKey(Parent, related_name='children', on_delete=models.CASCADE)

class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    children = models.ManyToManyField(Child, related_name='activities')