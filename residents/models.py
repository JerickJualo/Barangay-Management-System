
from django.db import models

class Purok(models.Model):
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f"Purok {self.number}"

class Street(models.Model):
    name = models.CharField(max_length=30)
    purok = models.ForeignKey(Purok, on_delete=models.CASCADE, related_name='streets')

    def __str__(self):
        return self.name

class Household(models.Model):
    number = models.IntegerField()
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='households')
    head_of_family = models.CharField(max_length=100)

    def __str__(self):
        return f"Household {self.number} on {self.street}"

class Resident(models.Model):
    name = models.CharField(max_length=30)
    birthdate = models.DateField()
    sex = models.CharField(max_length=6)
    civil_status = models.CharField(max_length=20)
    contact_number = models.CharField(max_length = 15)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    household = models.ForeignKey(Household, on_delete=models.CASCADE, related_name='residents')
    email_address = models.CharField(max_length = 30, blank = True, null = True)
    purok_no = models.ForeignKey(Purok, on_delete= models.CASCADE, related_name= 'residents', blank = True)
    

    def __str__(self):
        return self.name
