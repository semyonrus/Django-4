from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        has_main_tag = False
        for form in self.forms:
            # Проверяем, не помечены ли два тега как основные
            if form.cleaned_data.get('is_main', False):
                if has_main_tag:
                    raise ValidationError('Может быть только один основной тег для статьи.')
                has_main_tag = True
        # Проверка, что хотя бы один тег установлен как основной
        if not has_main_tag:
            raise ValidationError('Укажите основной тег для статьи.')

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormSet
    extra = 1
    min_num = 1  # убедимся, что хотя бы один тег назначен
    fk_name = 'article'  # указываем, что связь идет через поле article модели Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')  # можно добавить другие поля для отображения
    list_filter = ('published_at', )  # фильтруем статьи по дате публикации
    search_fields = ('title', 'text')  # поиск по заголовку и тексту
    inlines = [ScopeInline] # добавляем inline для тегов

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',)  # добавляем поиск по тегам

