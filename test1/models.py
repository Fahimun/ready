from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Phone = models.CharField(max_length=11)
    Address = models.TextField()
    # Location = models.TextField()
    # is_active = models.BooleanField(False)
    # create_at = models.TimeField(True)



    def __str__(salf): 
        return f"Name: {salf.Name} // Age: {salf.Age}"

