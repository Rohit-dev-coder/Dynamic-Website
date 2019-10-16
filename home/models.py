from django.db import models

class users(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    mobileno = models.CharField(max_length=10,unique = True)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length= 21)

    def __str__(self):
        return self.name
    
    def getpwd(self):
        return self.password
