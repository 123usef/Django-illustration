from django.db import models

# Create your models here.
#class ==> translation ==> table  ==> job for ORM (OBJECT RELATIONAL MAPPER )
class todo(models.Model):
    name = models.CharField(max_length=70 , null= True , blank=True)
    describtion = models.TextField(null= True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name 
    
#python manage.py makemigrations ===>detection 
#python manage.py migrate     ====> apply maigrations