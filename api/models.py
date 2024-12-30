from django.conf import settings
from django.db import models
from datetime import date
from PIL import Image

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

custodian=[('bible school', 'Bible School'), ('church','Church')]
condition = [('good', 'Good'), ('faulty','Faulty'), ('poor','Poor')]
statuses= [('present','Present'),('absent','Absent')]
depts=[('Protocol','Protocol'),('worship','Praise & Worship'),('prayers','Prayer & Intercessory'),
('media','Media & Publicity'),('pastoral','Pastoral'),('evangelism','Evangelism'),('discipleship','Discipleship'),('youth','Youth'),('children','Children'),('men','Men'),('women','Women'),('mercy','Mercy Team'),('church_care','Church Care'),('missions','Missions')]


# Church Leader Model
class ChurchLeader(models.Model):
    member = models.ForeignKey('members.Member', on_delete=models.CASCADE)
    position = models.CharField(max_length=100, null=True)
    date_appointed=models.DateField(default=None, blank=True, null=True)
    def __str__(self):
        return f"{self.member.full_name} - {self.position}"
        
# End of Church
class Event(models.Model):
    title = models.CharField(max_length=200)
    doe = models.DateField(default=None, blank=True, null=True)
    description = models.TextField()
    event_image = models.ImageField(default='default.jpg', upload_to='images/')
    venue = models.CharField(max_length=100, default="NCCI, Lanet.")
    coordinated_by = models.CharField(max_length=100, default="pst. Sharon")
    budget = models.CharField(blank=True, null=True, max_length=255)
    dept = models.CharField(max_length=255, choices=depts, default="mercy")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Call the original save method to save the object
        super().save(*args, **kwargs)

        # Resize the event image if it exceeds dimensions
        if self.event_image:
            img = Image.open(self.event_image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.event_image.path)

class Attendance(models.Model):
    total_present = models.CharField(max_length=10, default=0)
    doa=models.DateField(default=None, blank=True, null=True, unique=True)
    present_status = models.CharField(max_length=10, choices=statuses)

    class Meta:
        unique_together = ('total_present', 'doa')
        
    def __str__(self):
        return f" {self.doa} -{self.total_present} -{self.present_status}"

class Notice(models.Model):
    title = models.CharField(max_length=255, default='News')
    date_posted=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='church admin')
    message=models.CharField(max_length=500)
    def __str__(self):
        return self.title
        
class Inventory(models.Model):
    qty= models.CharField(max_length=255,default=1)
    serial_number = models.CharField(max_length=100,  blank=True, null=True)
    item_name= models.CharField(max_length=30)   
    issued_to = models.CharField(choices=custodian,max_length=50, default="ncci") 
    description = models.CharField(max_length=255)
    date_received = models.DateField(default=None, blank=True, null=True)
    current_condition=models.CharField(max_length=50, choices=condition)
    def __str__(self):
        return self.item_name



class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    coordinated_by = models.CharField(max_length=100, default="pst. Sharon")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GMember(models.Model):
    user = models.ForeignKey('members.Member', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="members")
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} in {self.group.name}"
