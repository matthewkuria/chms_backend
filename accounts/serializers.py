from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from members.models import Member  
# Assuming Member is related to CustomUser

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)  # Use email as the username
            if not user:
                raise serializers.ValidationError('Invalid credentials')
        else:
            raise serializers.ValidationError('Both fields are required.')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_admin', 'is_member']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            'id', 'full_name', 'member_number', 'membership', 'dob', 
            'baptism_status', 'baptism_date', 'marital_status', 'gender', 
            'mobile', 'residence', 'postal_address', 'date_joined', 
            'date_left', 'profile_image'
        ]
        read_only_fields = ['id', 'member_number']  # Prevent updating primary keys or computed fields



class UserProfileSerializer(serializers.ModelSerializer):
    member = MemberSerializer()

    class Meta:
        model = User
        fields = ['id', 'email', 'is_admin', 'is_member', 'member']

    def update(self, instance, validated_data):
        # Extract member data
        member_data = validated_data.pop('member', None)

        # Update the Member instance if data is provided
        if member_data:
            member_instance = Member.objects.filter(user=instance).first()
            if member_instance:
                for attr, value in member_data.items():
                    setattr(member_instance, attr, value)
                member_instance.save()

        # Update User fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

