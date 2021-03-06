from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image', null=True)
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
    business_name = models.CharField(max_length=40)
    image=CloudinaryField('image', null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    business_email = models.EmailField()
    business_number = models.IntegerField(blank=True,null=True)

    @classmethod
    def business_search(cls,search_term):
        return cls.objects.filter(business_name__icontains=search_term)

    def __str__(self):
        return f'Buisness {self.business_name} Owned by {self.user.username}'

class User_Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True)
    id_number = models.IntegerField(blank=True,null=True)
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'{self.user.username} profile'
    
class News(models.Model):
    image=CloudinaryField('image',null=True)
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=150)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    
    def save_stories(self):
        self.save()
        
    def delete_stories(self):
        self.delete()
    
    def __str__(self):
        return f'{self.category} story from {self.neighbourhood.name} Neighborhood'
       
    



