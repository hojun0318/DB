from tokenize import blank_re
from django.db import models
from django.conf import settings

# Create your models here.

def models_image_path(instance, filename):
        return f'image/{instance.user.username}/{filename}'

# 각각 유형에 맞는 필드 타입 설정, null=True 입력하지 않아도 저장 가능하도록 하기
# models.py 수정/추가 시 migrate 해주기
class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    audience = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    genre = models.CharField(max_length=30, null=True)
    score = models.FloatField(null=True)
    poster_url = models.TextField(blank=True, null=True)
    description = models.TextField(null=True)
    # image = models.ImageField(blank=True)
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    # image = models.ImageField(blank=True, upload_to=models_image_path)
    image = models.ImageField(blank=True, upload_to='images/')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

    # def __str__(self):
    #     return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # ForeignKey
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content