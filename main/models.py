from django.db import models



class Files(models.Model):
    title=models.CharField(default='no title', max_length=50)
    file=models.FileField(upload_to='files/')
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    