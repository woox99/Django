from django.db import models
import re
import bcrypt

# No methods in our new manager should ever receive the whole request object as an argument! 
# (just parts, like request.POST)
class UserManager(models.Manager):
    def validate_registration(self, data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        # add keys and values to errors dictionary for each invalid field
        if len(data['name']) < 3:
            errors["name"] = "name must be at least 3 chars"
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = 'invalid email'
        if len(data['password']) < 3:
            errors['password'] = 'password must be at least 3 char'
        if data['password'] != data['confirm']:
            errors['confirm'] = 'passwords must match'
        return errors
    
    def validate_login(self, data):
        errors = {}

        try:
            existing_user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            errors['email'] = "No account matches that email."
            return errors

        if not bcrypt.checkpw(data['password'].encode(), existing_user.password.encode()):
            errors['password'] = 'Invalid password'
        
        return errors


class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager() # Add This Line