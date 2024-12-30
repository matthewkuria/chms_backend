from rest_framework import serializers
from .models import  Event, Attendance, Inventory, Notice, Group, GMember

# serializer for Event Model
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields='__all__'


# Serializer for Attendance model
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'total_present', 'doa', 'present_status']

# Serializer for Inventory model
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

# Serializer for Notice model
class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'title', 'message', 'date_posted']



class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GMember
        fields = ['id', 'user', 'group', 'joined_at']

class GroupSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'created_at', 'members', 'coordinated_by']
