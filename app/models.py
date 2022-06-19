from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

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





