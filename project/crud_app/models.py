from django.db import models

class PanCard(models.Model):
    GENDER = [('F','Female'),('M','Male'),('O','Other')]
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    mobile_number = models.IntegerField()
    pan_no = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10,choices=GENDER)

