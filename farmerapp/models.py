from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    usertype=models.CharField(max_length=40)
    ViewPassword=models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.username
# Create your models here.
    
class Farmer(models.Model):
    farmer=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=30, null=True)
    email=models.EmailField()
    mob=models.IntegerField()
    address=models.TextField()
    img=models.ImageField(upload_to="gallery", null=True)
    gender=models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name
    
class Farmtech(models.Model):
    farm=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=30, null=True)
    email=models.EmailField()
    mob=models.IntegerField()
    img=models.ImageField(upload_to="gallery", null=True)
    gender=models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="gallery")
    farmername=models.ForeignKey(Farmer,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField(max_length=100, null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    quantity=models.IntegerField()
    img=models.ImageField(upload_to="gallery")
    fid=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    price=models.IntegerField()
    status=models.CharField(max_length=100, null=True, default="0") 
    
    def __str__(self):
        return self.name
    
    
class Loan(models.Model):
    
    fid=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    techid=models.ForeignKey(Farmtech, on_delete=models.CASCADE)
    status=models.CharField(max_length=20, default='0')
    purpose=models.TextField()
    amount=models.IntegerField()

class Feedback(models.Model):
    fid=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    content=models.TextField()
    rating=models.IntegerField()

    
class Lands(models.Model):
    area=models.CharField(max_length=50,null=True)
    duration=models.CharField(max_length=50,null=True)
    amount=models.IntegerField()
    techid=models.ForeignKey(Farmtech,on_delete=models.CASCADE)
    img=models.ImageField(upload_to="gallery")
    status=models.CharField(max_length=100, null=True, default="0") 
    
    
class Vehicle(models.Model):
    type=models.CharField(max_length=30,null=True)
    duration=models.CharField(max_length=30,null=True)
    amount=models.IntegerField()
    techid=models.ForeignKey(Farmtech,on_delete=models.CASCADE)
    img=models.ImageField(upload_to="gallery")
    status=models.CharField(max_length=100, null=True, default="0") 

    
    
class Bookvehiclerent(models.Model):
    fid=models.ForeignKey(Farmer,on_delete=models.CASCADE,null=True)
    techid=models.ForeignKey(Farmtech,on_delete=models.CASCADE,null=True)
    vid=models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True)
    startingdate=models.DateField()
    endingdate=models.DateField()
    totalamount=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=20,null=True,default="0")
    
    
class Booklandrent(models.Model):
    fid=models.ForeignKey(Farmer,on_delete=models.CASCADE,null=True)
    techid=models.ForeignKey(Farmtech,on_delete=models.CASCADE,null=True)
    lid=models.ForeignKey(Lands,on_delete=models.CASCADE,null=True)
    startingdate=models.DateField()
    endingdate=models.DateField()
    totalamount=models.CharField(max_length=20,null=True)
    status=models.CharField(max_length=100, null=True,default="0")
    


    