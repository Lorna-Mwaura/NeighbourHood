from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
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
    
    def __str__(self):
        return self.name

class Business(models.Model):
    '''
    Model for business class in neighbourhood
    '''
    business_name = models.CharField(max_length=40)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    business_email = models.EmailField()
    business_number = models.IntegerField(blank=True,null=True)

    @classmethod
    def buisness_search(cls,search_term):
        return cls.objects.filter(buisness_name__icontains=search_term)

    def __str__(self):
        return f'Buisness {self.buisness_name} Owned by {self.user.username}'


