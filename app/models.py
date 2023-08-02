from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Invoice(models.Model):
    invoice_date=models.DateField(null=True,blank=True)
    invoice_number=models.CharField(max_length=10,null=True,blank=True)
    customer_name=models.CharField(max_length=30,null=True,blank=True)
    invoice_duedate=models.DateField(null=True,blank=True)
    Product=models.CharField(max_length=20,null=True,blank=True)
    Quantity=models.CharField(max_length=20,null=True,blank=True)
    Rate=models.CharField(max_length=50,null=True,blank=True)
    Total=models.CharField(max_length=50,null=True,blank=True)
    #user=models.ForeignKey(User,related_name="invoice", on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.title