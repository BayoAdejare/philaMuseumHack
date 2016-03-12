from django.db import models

class User(models.Model):
    name = models.TextField()
    collection = models.TextField()
    like_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)

    @property
    def __str__(self):
        return '%s id:%s' % (self.name, self.id)
