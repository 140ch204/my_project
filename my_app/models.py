from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Contact(models.Model):
    email = models.EmailField(max_length=100)
    date_inscription = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date d'inscription'")
    
    class Meta:
        verbose_name = "contact"
        ordering = ['date_inscription']
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.email


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['email']
        