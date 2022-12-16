from django.db import models
# Create your models here.
class Service(models.Model):
    service_id = models.AutoField(db_column='service _id', primary_key=True)  # Field renamed to remove unsuitable characters.
    service = models.CharField(max_length=50)
    details = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    u_id = models.IntegerField()
    # u = models.ForeignKey(Customer, to_field='c_id', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'service'

