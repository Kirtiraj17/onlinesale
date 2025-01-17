from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class BillingProfileManager(models.Manager):
    def get_or_new(self, request):
        if request.user.is_authenticated:
            bill_obj = self.get_queryset().filter(user=request.user).first() or None
            if bill_obj is None:
                bill_obj = self.get_queryset().create(user=request.user, email=request.user.email)
            return bill_obj

class BillingProfile(models.Model):
    user = models.OneToOneField(User,blank=True,on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #customerid

    objects = BillingProfileManager()

    def __str__(self):
        return str(self.user)+"-"+self.email

def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        BillingProfile.objects.create(user=instance, email=instance.email)

post_save.connect(user_post_save_receiver, sender=User)