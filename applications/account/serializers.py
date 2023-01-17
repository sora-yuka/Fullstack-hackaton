from rest_framework import serializers
from applications.account.models import CustomUser
from django.contrib.auth import get_user_model
from applications.account.tasks import send_confirmation_email

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=6)
    password_confirm = serializers.CharField(
        min_length=6,
        write_only=True,
        required=True,
    )
    
    class Meta:
        model = CustomUser
        # fields = ["username", "email", "password", "password_confirm", "bank_card", "gender", "contact"]
        exclude = ["is_active", "activation_code", "confirm_code"]
        
    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm")
        
        if password != password_confirm:
            raise serializers.ValidationError("Password doesn't match")
        
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        send_confirmation_email.deley(user.email, code)
        return user
    
