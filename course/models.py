from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True,max_length=15)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Lecturer(models.Model):
    id = models.IntegerField(primary_key=True,max_length=15)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    department = models.CharField(max_length=300)
    faculty = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Course(models.Model):
    id = models.IntegerField(primary_key=True,max_length=15)
    title = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return f'{self.title} {self.id}'

