import datetime
from django.db import models
from apps.user_app.models import CustomUser
# Create your models here.

def user_directory_path(instance, filename):

    return datetime.datetime.now().strftime('%Y/%m/%d/') + f'user_{instance.user.id}/{filename}'

class Content(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='content')
    name = models.CharField(max_length=100, verbose_name='Название')
    upload = models.FileField(upload_to=user_directory_path)


    class Meta:
        verbose_name_plural = 'Файлы'
    
    def __str__(self) -> str:
        return self.name