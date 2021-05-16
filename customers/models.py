from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    cpf = models.CharField(max_length=14,unique=True)
    join_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
