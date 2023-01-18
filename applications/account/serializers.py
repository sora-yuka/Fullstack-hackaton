from rest_framework import serializers, response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from applications.account.tasks import send_confirmation_email, send_confirmation_code

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
    

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(
        required=True,
        min_length=6
    )
    new_password_confirm = serializers.CharField(
        required=True,
        min_length=6
    )

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        new_password_confirm = attrs.get('new_password_confirm')
        if new_password != new_password_confirm:
            raise serializers.ValidationError('Password dont match!')
        return attrs

    def validate_old_password(self, old_password):
        request = self.context.get('request')
        user = request.user
        if not user.check_password(old_password):
            raise serializers.ValidationError('Wrong password!')
        return old_password

    def set_new_password(self):
        user = self.context.get('request').user
        password = self.validated_data.get('new_password')
        user.password = make_password(password)
        user.save()
        
    
class ForgotPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    
    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError("User with this username doesn't exist")
        return username
    
    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email doesn't exist.")
        return email
    
    def send_code(self):
        email = self.validated_data.get("email")
        user = User.objects.get(email=email)
        user.create_confirm_code()
        user.save()
        send_confirmation_code.delay(email, user.confirm_code)
        
        
class ForgotPasswordConfirmSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    code = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)
    
    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError("User with this username doesn't exist.")
        return username
    
    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with this email doesn't exist.")
        return email
    
    @staticmethod
    def validate_code(code):
        if not User.objects.filter(confirm_code=code).exists():
            raise serializers.ValidationError("Wrong code!")
        return code
    
    def validate(self, attrs):
        password = attrs.get("new_password")
        password_confirm = attrs.get("new_password_confirm")

        if password != password_confirm:
            raise serializers.ValidationError("Password dont match!")
        return attrs
    
    def set_new_password(self):
        email = self.validated_data.get("email")
        password = self.validated_data.get("password")
        user = User.objects.get(email=email)
        user.password = make_password(password)
        user.confirm_code = ""
        user.save()