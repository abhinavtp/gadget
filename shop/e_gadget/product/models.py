from django.db import models

# Create your models here.
class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=50)
    image = models.CharField(max_length=150)
    price = models.CharField(max_length=50)
    specifications = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product'

