from django.db import models
from customer.models import Customer
# Create your models here.
class Rating(models.Model):
    r_id = models.AutoField(primary_key=True)
    # u_id = models.IntegerField()
    u=models.ForeignKey(Customer,to_field='c_id',on_delete=models.CASCADE)
    rating = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rating'

