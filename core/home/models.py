from django.db import models

# Create your models here.


class Students(models.Model):
    # id=models.AutoField()                                   # This is for Default counter of Django that runs automatically(Also a primary key)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField()
    address = models.TextField()
    # image=models.ImageField(upload_to='./files/')                   # This is for image upload, Enter Path in strings
    # file=models.FileField(upload_to='./files/')                     # This is for file upload, Enter Path in strings


class Products(models.Model):
    pass


class car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField()

    def __str__(self) -> str:
        return self.car_name + str(self.speed)
