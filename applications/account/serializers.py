from rest_framework import serializers, response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from applications.account.tasks import send_confirmation_email

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6)
    password_confirm = serializers.CharField(
        min_length=6,
        write_only=True,
        required=True,
    )
    
    
    class Meta:
        model = User
        fields = [
            "username", "email", 
            "password", "password_confirm", 
            "bank_card", "gender", 
            "contact",
        ]
        
    
    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError('Password dont match!')

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        send_confirmation_email.delay(user.email, code)
        return user