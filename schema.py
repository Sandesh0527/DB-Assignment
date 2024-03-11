from django.db import models


class ProductCategory(models.Model):
  name = models.CharField(max_length=50,blank=False,null=False)
  desc = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now_add=True)
  deleted_at = models.DateTimeField(auto_now_add=True)


class ProductInventory(models.Model):
  quantity = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now_add=True)
  deleted_at = models.DateTimeField(auto_now_add=True)

class Discount(models.Model):
  name = models.CharField(max_length=50,blank=False,null=False)
  desc = models.TextField(blank=True, null=True)
  discount_percent = models.FloatField()
  active = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now_add=True)
  deleted_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
  name = models.CharField(max_length=50,blank=False,null=False)
  desc = models.TextField(blank=True, null=True)
  SKU = models.CharField(max_length=50,blank=True,null=True)
  category_id = models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
  inventory_id = models.ForeignKey(ProductInventory,on_delete=models.CASCADE)
  price = models.FloatField()
  discount = models.ForeignKey(Discount,on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now_add=True)
  deleted_at = models.DateTimeField(auto_now_add=True)
