from django.db import models

class daycareInsert(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    datedd=models.DateField(max_length=100)
    datedd2=models.DateField(max_length=100)
    class Meta:
        db_table="daycare"

class daycareDisplay(models.Model):
    name=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    datedd=models.DateField(max_length=100)
    datedd2=models.DateField(max_length=100)

class adoptInsert(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    selectdog=models.CharField(max_length=100)
    class Meta:
        db_table="adopt"

class fosterInsert(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    selectdog=models.CharField(max_length=100)
    class Meta:
        db_table="foster"

class contactInsert(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    textbox=models.TextField(max_length=100)
    class Meta:
        db_table="contact"

class dogs(models.Model):
    #id=models.IntegerField()
    name=models.CharField(max_length=100)
    breed=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/',null=True, blank=True)
    link=models.URLField(max_length=100)
    class Meta:
        db_table="dogs"

    

        

