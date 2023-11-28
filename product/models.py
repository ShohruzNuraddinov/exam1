from collections.abc import Iterable
import cv2
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='lesson/')
    duration = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # def save(self, *args, **kwargs):
    #     print("http://127.0.0.1:8000" + self.video.url)
    #     print(self.video_duration("http://127.0.0.1:8000" + self.video.url))
    #     self.duration = self.video_duration(self.video.url)
    #     return super(Lesson, self).save(*args, **kwargs)

    # def video_duration(self):
    #     video = cv2.VideoCapture(a)
    #     frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    #     fps = video.get(cv2.CAP_PROP_FPS)
    #     return round(frames / fps)


class Product(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Lesson)
    view_count = models.IntegerField(default=0)
    # users = models.ManyToManyField('auth.User')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def update_view_count(self):
        self.view_count += 1
        self.save()


class ProductSubscribers(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='subscribers')
    subscribers = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class LessonHistory(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_history')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_history')
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='history'
    )

    end_point = models.IntegerField()
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        if self.end_point <= .8 * self.lesson.duration:
            self.status = False
        self.status = True
        return super().save(*args, **kwargs)
