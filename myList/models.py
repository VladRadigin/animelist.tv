from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Аниме')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    views = models.FloatField(null=True, blank=True, verbose_name='Просмотры')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Жанры')

    class Meta:
        verbose_name_plural = 'Список аниме'
        verbose_name = 'Аниме'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'
        ordering = ['name']
