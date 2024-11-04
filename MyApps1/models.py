from audioop import reverse

from django.db import models

# Create your models here.
from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse;
#Create your models here....
class Students(models.Model):
    rollno=models.IntegerField();
    name=models.CharField(max_length=128)
    dept=models.CharField(max_length=128)
    marks=models.FloatField(max_length=128)
    def __str__(self):
        return str(self.rollno)+"\t"+str(self.name)+"\t"+str(self.dept)+"\t"+str(self.marks)
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})



