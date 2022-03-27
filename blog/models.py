import os.path

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True, null=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author: 추후 작성 예정

    # 모델 메소드 정의(오버라이딩)
    def __str__(self):
        return f'[{self.pk}]    [{self.title}]'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)