
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=256)
    stablish_time = models.DateField()
    ceo = models.CharField(max_length=256)
    brand_detail = models.OneToOneField("BrandDetail", on_delete=models.CASCADE)

class BrandDetail(models.Model):
    headquarters = models.CharField(max_length=256)
    founder = models.CharField(max_length=256)
    market_ocp = models.DecimalField(max_digits=10, decimal_places=2)

class GPU(models.Model):
    GPU_name = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    frequency = models.DecimalField(max_digits=10, decimal_places=2)
    power_dissipation = models.DecimalField(max_digits=10, decimal_places=2)
    VRAM_cap = models.DecimalField(max_digits=10, decimal_places=2)
    VRAM_type = models.CharField(max_length=256)
    publish_time = models.DateField()

class Price(models.Model):
    Brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    GPU = models.ForeignKey("GPU", on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10, decimal_places=2)

# class Admin(models.Model):
#     nick_name = models.CharField(max_length=256)
#     account_number = models.CharField(max_length=256)
#     password  = models.CharField(max_length=256)

class User(models.Model):
    user_name = models.CharField(max_length=256)
    account_number = models.CharField(max_length=256)
    password  = models.CharField(max_length=256)