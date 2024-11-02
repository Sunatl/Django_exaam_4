from django.db import models


class User(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=13)
    register_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.username
    
    
    

    
    
    
class Movie(models.Model):
    name = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="static/images",null=True,blank=True)
    description = models.TextField() 
    vedio = models.FileField(upload_to="static/images",null=True,blank=True)
    zhanr = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    amount = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Payment(models.Model):
    cordss = [
        ("DC","Dc"),
        ("ALIF","Alif")
    ]    
    cord = models.CharField(max_length=50,choices=cordss)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.cord
    
    

    
    