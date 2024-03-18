from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'




    def __str__(self):
        return self.title



from django.db import models
from django.core.exceptions import ValidationError


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Scope(models.Model):
    tag = models.ForeignKey(Tag, related_name='scopes', on_delete=models.CASCADE, verbose_name='Тег')
    article = models.ForeignKey(Article, related_name='scopes', on_delete=models.CASCADE, verbose_name='Статья')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        # Уникальность пары статья-тег для избежания дубликатов
        unique_together = ('article', 'tag')
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'

    def __str__(self):
        return f'{self.tag.name} - {self.article.title} {"(основной)" if self.is_main else ""}'

    def clean(self):
        # Проверка, что у статьи может быть только один основной тег
        if self.is_main:
            main_count = Scope.objects.filter(article=self.article, is_main=True).exclude(pk=self.pk).count()
            if main_count >= 1:
                raise ValidationError('У статьи может быть только один основной тег.')

