from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
# @receiver(signal=post_save,sender=Profile)


# sender->the model that sent,instance ->instance of the model, created -> If the model was added or saved again
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email=user.email,
            name = user.first_name
        )


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print("Deleting User...")


post_save.connect(createProfile, sender=User)


post_delete.connect(deleteUser,sender=Profile)