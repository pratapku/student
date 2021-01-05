from django.db import models

# Create your models here.
# create model here and storing in database octs os mysql
 
class contact(models.Model):
    project=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50,default="")
    semester=models.CharField(max_length=50,default="")
    address=models.CharField(max_length=50,default="")
    Email=models.CharField(max_length=50,default="")


    def __str__(self):
        return self.name
    


