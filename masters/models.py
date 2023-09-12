from django.db import models
from datetime import datetime

# Create your models here.


class MasterModel(models.Model):
    f_name = models.CharField(max_length=100, default='')
    l_name = models.CharField(max_length=100, default='')
    data_of_birth = models.DateTimeField(default=datetime.now)

    def str(self):
        return f'{self.f_name} {self.l_name}'

    class Meta:
        db_table = 'Master'


class OrderModel(models.Model):
    order_name = models.CharField(max_length=100, default='')
    time_of_order = models.CharField(max_length=100, default='')

    def str(self):
        return self.order_name

    class Meta:
        db_table = 'Order'
