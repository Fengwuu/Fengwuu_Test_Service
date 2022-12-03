from django.db import models
from django.contrib.auth.models import User
from tests.models import Test


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='photos/avatars/users', verbose_name='Изображение', blank=True)
    completed_tests = models.ManyToManyField('tests.Test', verbose_name='Completed_tests',
                                             blank=True,
                                             )


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
