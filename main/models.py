from django.db import models
from django.contrib.auth.models import User


class Files(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(default='no title', max_length=50)
    file=models.FileField(upload_to='files/')
    uploated_at=models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering=['-uploated_at']

    def __str__(self):
        return self.title
    