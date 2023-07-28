from django.db import models

# Below three lines added manually
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)
# Create your models here.

class showroom(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    pic = models.ImageField()
    address = models.CharField(max_length=100)


    def __str__(self): 
        return self.name
    

class staff(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    pic = models.ImageField()
    Role = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    qualification = models.CharField(max_length=30)
    contact = models.CharField(max_length=13)

    showroom = models.ForeignKey(showroom , on_delete=models.CASCADE , related_name='staff')

    def __str__(self):
        return self.name
    
class brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()
    founder = models.CharField(max_length=100)
    origin = models.CharField(max_length=20)
    contact = models.CharField(max_length=14)

    showroom = models.ForeignKey(showroom , on_delete=models.CASCADE , related_name='brand')

    def __str__(self):
        return self.name
    

class feature(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class engine(models.Model):
    name = models.CharField(max_length=20)
    Horse_power = models.CharField(max_length=30)
    fuel_type = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class engine_number(models.Model):
    engine_no = models.CharField(max_length=50 , blank=True , null=True)
    
    name = models.ForeignKey(engine , on_delete=models.CASCADE , related_name='engine_no', blank=True , null=True)
    

    def __str__(self):
        return self.engine_no
       # return f'{self.name}'



class model(models.Model):
    name = models.CharField(max_length=50)    
    image = models.ImageField()
    release_date = models.DateField(blank=True , null=True)
    price = models.IntegerField()

    features = models.ManyToManyField(feature ,  related_name = 'model')
    showroom = models.ForeignKey(showroom ,on_delete=models.CASCADE , related_name='model')
    engine = models.ForeignKey(engine , on_delete=models.CASCADE , related_name='model')
    brand = models.ForeignKey(brand , on_delete=models.CASCADE , related_name='model' , null=True , blank=True)

    quantity_in_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
class car(models.Model):
    name = models.ForeignKey(model , on_delete=models.CASCADE , related_name='car')    
    chessis_no = models.CharField(max_length=20 , primary_key=True)
    engine_number = models.OneToOneField(engine_number, on_delete=models.CASCADE , related_name='car', null=True )

    def __str__(self):
        return self.chessis_no



class customer(models.Model):
    name = models.CharField(max_length=30)
    pic = models.ImageField(blank=True)
    email = models.EmailField(blank=True , null=True)
    address = models.CharField(max_length=50 , null=True , blank=True)
    contact_no = models.CharField(max_length=14)

    def __str__(self):
        return self.name

class sale(models.Model):
    customer_name = models.ForeignKey(customer , on_delete=models.CASCADE , related_name='sale')    
    brand_name = models.ForeignKey(brand , on_delete=models.CASCADE , related_name='sale')
    model_name = models.ForeignKey(model , on_delete=models.CASCADE ,related_name='sale' , null=True , blank=True)
    chessis_no = models.OneToOneField(car , on_delete=models.CASCADE , related_name='sale')

    def __str__(self):
        return self.brand_name.name


   
