from django.db import models

# модель таблицы в базе данных
class Women(models.Model):
    title = models.CharField(max_length=255)  # это атрибут, а если вызвать, то будет экземпляр
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.DateTimeField(default=True)

    def __str__(self):
        return self.title