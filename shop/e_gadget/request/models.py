from django.db import models
from customer.models import Customer
from service.models import Service
# Create your models here.
class RequestService(models.Model):
    requst_id = models.IntegerField(primary_key=True)
    # u_id = models.IntegerField()
    u=models.ForeignKey(Customer,to_field='c_id',on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    # service_id = models.IntegerField()
    service=models.ForeignKey(Service,to_field='service_id',on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'request_service'

