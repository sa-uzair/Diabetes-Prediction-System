from django.db import models

# Create your models here.
from django.db import models

class diet(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class prevention(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)

    def __str__(self):
        return self.product_name