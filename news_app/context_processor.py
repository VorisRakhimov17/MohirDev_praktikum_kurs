from .models import News, Category
def letest_news(request):
    latest_news = News.objects.all().order_by('publish_time')[:10]

    context = {
        'latest_news': latest_news
    }

    return context

def letset_category(request):
    letset_category = Category.objects.all()

    context = {
        'letset_category': letset_category
    }

    return context