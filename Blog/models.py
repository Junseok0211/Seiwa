from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # 제목
    title = models.CharField(max_length=80, null=False)
    # 글 내용
    content = models.TextField(null = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    #글 생성일
    create = models.DateTimeField(auto_now_add=True)
    # 글 수정일
    updated = models.DateTimeField(auto_now=True)

