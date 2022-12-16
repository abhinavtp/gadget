from django.db import models

# Create your models here.
class Order(models.Model):
    o_id = models.AutoField(primary_key=True)
    p_id = models.IntegerField()
    date = models.DateField()
    amount = models.CharField(max_length=50)
    u_id = models.IntegerField()
    status = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'order'

