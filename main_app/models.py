from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration  = models.CharField(max_length=25)

    def __str__(self):
        return self.title

class Instructor(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Add_course(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration  = models.CharField(max_length=25)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


