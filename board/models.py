from django.db import models
from user.models import User

# Create your models here.
from django.utils import timezone

class Board(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey('user.User',on_delete=models.CASCADE)
    content = models.TextField()
    regdate = models.DateTimeField(auto_now=timezone.now)
    readcount = models.IntegerField(default=0)
    
    def __str__(self):
        return '%s. %s(%d)' % (self.title, self.writer, self.content, self.readcount)
    def increamentReadCount(self):
        self.readcount += 1
        self.save()