from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().order_by('-published_at')

    for article in articles:
        article.scopes = article.tags.all().order_by('-scope__is_main', 'name')

    context = {
        'articles': articles
    }

    return render(request, template, context)
