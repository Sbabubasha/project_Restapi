from django.db import models

# Create your models here.

class Product_catagory(models.Model):
    pc_id=models.IntegerField()
    pc_name=models.CharField(max_length=100)

    def __str__(self) :
        return self.pc_name
    

class Product(models.Model):
   pc_name=models.ForeignKey(Product_catagory,on_delete=models.CASCADE)
   pid=models.IntegerField()
   pname=models.CharField(max_length=100)
   price=models.DecimalField(max_digits=6,decimal_places=2)
   pdate=models.DateField()

   def __str__(self) -> str:
        return self.pname
   