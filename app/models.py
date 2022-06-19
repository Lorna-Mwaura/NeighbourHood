from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    admin = models.ForeignKey(
        'app.User', on_delete=models.CASCADE, related_name='neighbourhoods', null=True)
    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()
    
    @classmethod
    def update_neighbourhood(cls, id):
        cls.objects.filter(id=id).update(id=id)
    
    @classmethod
    def search_neighbourhood(cls, search_term):
        neighbourhoods = cls.objects.filter(neighbourhood_name_icontains=search_term)
        return neighbourhoods

class User(AbstractUser):
    name = models.CharField(max_length=124)
    email = models.CharField(max_length=124, unique=True)
    avatar = CloudinaryField('image', null=True)
    bio = models.TextField(max_length=500, null=True)
    contact = models.TextField(max_length=20, null=True,)
    neighbourhood = models.ForeignKey(
        Neighbourhood, on_delete=models.SET_NULL, null=True, related_name="users",)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    @property
    def url_formatted_name(self):
        return self.full_name.replace(' ', '+') or self.username

   



