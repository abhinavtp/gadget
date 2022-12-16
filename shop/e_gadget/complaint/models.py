from django.db import models
from customer.models import Customer
# Create your models here.
class Complaint(models.Model):
    comp_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=50)
    date = models.DateField()
    reply = models.CharField(max_length=50)
    time = models.TimeField()
    # u_id = models.IntegerField()
    u=models.ForeignKey(Customer,to_field='c_id',on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'complaint'

