from django.db import models

# Create your models here
class Employee(models.Model):
    first_name = models.CharField(max_length=250)
    last_name =  models.CharField(max_length=250)
    position =  models.CharField(max_length=250)
    job_type =  models.CharField(max_length=250)
    image = models.ImageField(upload_to='employee')
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name