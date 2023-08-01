from django.contrib import admin
from app.models import Invoice
from .models import *



# Register your models here.
admin.site.register(Invoice)