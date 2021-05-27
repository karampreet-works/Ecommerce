from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50 , default="")
    sub_category = models.CharField(max_length=50 , default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=30000  )
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shops/images" , default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.IntegerField(default=0)
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    product_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=111 ,default="")
    email = models.CharField(max_length=500)
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500)
    State = models.CharField(max_length=300)
    city = models.CharField(max_length=111)
    zip = models.CharField(max_length=111 ,default="")


class updateOrder(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=500)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:12] + '....'