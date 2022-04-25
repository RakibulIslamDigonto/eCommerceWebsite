from django.db import models
from loginApp.models import User
from coreApp.models import BaseModel
from shopApp.models import Category, Product

# Create your models here.
class Card(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_title = models.ForeignKey(Product, on_delete=models.CASCADE)
    quentity = models.IntegerField(default=1)
    purchase = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quentity} X {self.item_title}'

    def get_total(self):
        total_price= self.item_title.price * self.quentity
        total_in_float = format(total_price, '.2f')
        return total_in_float
        
    class Meta:
        ordering = ['-id']


class Order(BaseModel):
    orderItems = models.ManyToManyField(Card)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderedOrNot = models.BooleanField(default=False)
    paymentID = models.CharField(max_length=264, blank=True, null=True)
    orderID = models.CharField(max_length=264, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total_price = 0
        for order_item in self.orderItems.all():
            total_price += order_item.get_total()
            total_in_float = format(total_price, '.2f')
        return total_in_float

    class Meta:
        ordering = ['-id']
        

    


