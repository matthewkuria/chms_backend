from django import forms
from django.contrib.auth.models import User
from . import models

#for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']


#for Member related form
class MemberUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class MemberExtraForm(forms.ModelForm):
    class Meta:
        model=models.MemberExtra
        fields=['member_number','dept','mobile','status']

#for churchleader related form
class ChurchLeaderUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class ChurchLeaderExtraForm(forms.ModelForm):
    class Meta:
        model=models.ChurchLeaderExtra
        fields=['mobile','status']


#for Attendance related form
presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    present_status=forms.ChoiceField( choices=presence_choices)
    date=forms.DateField()

class AskDateForm(forms.Form):
    date=forms.DateField()

#for notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model=models.Notice
        fields='__all__'

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your name'}))
    Email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email Address'}))
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class': 'form-control','rows': 4, 'cols': 30}))
