from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)
    document = models.FileField(upload_to='documents/')

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    address = models.TextField(blank=True, null=True)
    
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )

    aadhar = models.FileField(upload_to='aadhar_docs/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Policy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    document = models.FileField(upload_to='policies/', blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    role = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.role