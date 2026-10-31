from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    skintone=models.CharField(max_length=100)
    skintype=models.CharField(max_length=100)
    sensitivity_level=models.CharField(max_length=100)
    loginid=models.ForeignKey('Login',on_delete=models.CASCADE)

class Login(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    usertype=models.CharField(max_length=10)
    login_status=models.IntegerField(default=0)

     



class Hospital(models.Model):
    Hospital_name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    State=models.CharField(max_length=10)
    District=models.CharField(max_length=10)
    City=models.CharField(max_length=10)
    Hospital_id=models.ForeignKey('Login',on_delete=models.CASCADE)
    def __str__(self):
        return self.Hospital_name

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    qualifications=models.CharField(max_length=50)
    experience=models.CharField(max_length=10)
    contact=models.IntegerField()
    loginid=models.ForeignKey('Login',on_delete=models.CASCADE)
    hospitalid=models.ForeignKey('Hospital',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Appointment(models.Model):
    user_id=models.ForeignKey('User',on_delete=models.CASCADE)
    doctor_id=models.ForeignKey('Doctor',on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    current_date=models.DateTimeField(auto_now_add=True)
    prescription=models.CharField(max_length=100)
    Appointment_status=models.IntegerField(default=0)


class Complaint(models.Model):
    complaint=models.CharField(max_length=300)
    current_date=models.DateTimeField(auto_now_add=True)
    loginid=models.ForeignKey('Login',on_delete=models.CASCADE)
    reply=models.CharField(max_length=200)


class Product(models.Model):
    name=models.CharField(max_length=300)
    description=models.CharField(max_length=200)
    image=models.FileField()
    current_date=models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    account_holder_name=models.CharField(max_length=200)
    card_number=models.CharField(max_length=100)
    cvv=models.CharField(max_length=100)
    current_date=models.DateTimeField(auto_now_add=True)
    product_id=models.ForeignKey('Product',on_delete=models.CASCADE)
    loginid=models.ForeignKey('User',on_delete=models.CASCADE)
    expiry_date=models.CharField(max_length=100)





