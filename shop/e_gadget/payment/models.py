from django.db import models

# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    price = models.CharField(max_length=50)
    u_id = models.IntegerField()
    status = models.CharField(max_length=50)
    o_id = models.IntegerField()
    date = models.DateField()
    amount=models.IntegerField()
    p_id = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'payment'

