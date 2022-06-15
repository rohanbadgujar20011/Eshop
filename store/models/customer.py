from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    email_Adress=models.EmailField()
    Password=models.CharField(max_length=500)

    def __str__(self):
        return self.first_name

   
    
    def isExits(self):
        if Customer.objects.filter(email_Adress = self.email_Adress):
            return True
        return False
    
    @staticmethod
    def get_email_check(email):
        try:
            return Customer.objects.get(email_Adress=email)
        except:
            return False