from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    BEGINNER = 'BE'
    INTERMEDIATE = 'IN'
    ADVANCED = 'AD'
    GENERALSKILLS = 'GE'

    DIFF_CHOICES = ((BEGINNER, 'Beginner'), (INTERMEDIATE, 'Intermediate'), (ADVANCED, 'Advanced'), (GENERALSKILLS, 'General skills'))
    
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    difficulty = models.CharField(max_length = 15, choices=DIFF_CHOICES, default='Beginner' )
    link = models.URLField()
    text = models.TextField()
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)

    def __str__(self):
        return "%s's profile" % self.user

def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)



# Signal while saving user
#from django.db.models.signals import post_save
#post_save.connect(create_profile, sender=User)
