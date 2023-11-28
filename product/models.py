import cv2
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='lesson/')
    duration = models.IntegerField(blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     # print("http://127.0.0.1:8000" + self.video.url)
    #     # print(self.video_duration("http://127.0.0.1:8000" + self.video.url))
    #     # self.duration = self.video_duration(self.video.url)
    #     return super(Lesson, self).save(*args, **kwargs)

    # def video_duration(self):
    #     print("http://127.0.0.1"+self.video.url)
    #     video = cv2.VideoCapture("http://127.0.0.1"+self.video.url)
    #     frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    #     fps = video.get(cv2.CAP_PROP_FPS)
    #     print(frames)
    #     print(self.video.url)
    #     print(fps)
    #     return round(frames / fps)


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Lesson)
    view_count = models.IntegerField(default=0)
    # users = models.ManyToManyField('auth.User')


class StatusChoise(models.Choices):
    viewed = 'Viewed'
    not_viewed = 'Not Viewed'


class LessonHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='history'
    )
    duration = models.IntegerField()
    status = models.CharField(max_length=32, choices=StatusChoise.choices)

    def save(self, *args, **kwargs):
        
        return super(LessonHistory, self).save(*args, **kwargs)
