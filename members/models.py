from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.models import CustomUser

memberships =[('regular','Regular'),('associate','Associate'), ('guest', 'Guest')]
maritals = [('single','Single'), ('married','Married'),('divorced','Divorced'), ('widowed', 'Widowed')]
genders=[('male','Male'),('female','Female')]
depts=[('Protocol','Protocol'),('worship','Praise & Worship'),('prayers','Prayer & Intercessory'),
('media','Media & Publicity'),('pastoral','Pastoral'),('evangelism','Evangelism'),('discipleship','Discipleship'),('youth','Youth'),('children','Children'),('men','Men'),('women','Women'),('mercy','Mercy Team'),('church_care','Church Care'),('missions','Missions')]
baptised= [('yes','Yes'),('no','No')]

class Member(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,default=None,blank=True, null=True, related_name="member")
    profile_image = models.ImageField(upload_to='profile-pics/', default="defaultuser.png")
    full_name=models.CharField(max_length=30, default=None)
    member_number = models.CharField(max_length=10, unique=True, default=None)
    membership = models.CharField(max_length=20, choices=memberships, default="regular")
    baptism_status =models.CharField(max_length=10,choices=baptised,default='no')
    baptism_date =models.DateField(default=None,blank=True, null=True)
    marital_status = models.CharField(max_length=25, choices=maritals, default='single')
    dob= models.DateField(default=None,blank=True, null=True)
    gender=models.CharField(max_length=10, choices=genders,default='male')
    mobile = models.CharField(max_length=40,null=True)
    residence=models.CharField(max_length=40,default='Nakuru')
    postal_address=models.CharField(max_length=40,default="20100")
    date_joined= models.DateField(default=None, blank=True, null=True)
    date_left= models.DateField(default=None, blank=True, null=True)
    status=models.BooleanField(default=False) 
    role = models.CharField(max_length=50, default="Member")   
    def __str__(self):
        return self.full_name


