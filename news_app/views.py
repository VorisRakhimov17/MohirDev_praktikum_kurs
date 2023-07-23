from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import News,  Category
from .forms import ContactForm

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published) # bu birinchi usul
    news_list = News.published.all() # bu ikkinchi usul
    context = {
        "news_list": news_list
    }


    return render(request, 'news/news_list.html', context=context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }
    return render(request, 'news/news_detail.html', context)


# def HomePageView(request):
#     category = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:5]
#     local_one = News.published.filter(category__name='Mahalliy').order_by('-publish_time')[:1]
#     local_news = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6] #Agar category='mahalliy' diganimda bu notogri bolardi sababi category ForeignKey ga ulangan shu uchun "__name" ni qo'shdik
#
#     context = {
#         "news_list": news_list,
#         "category": category,
#         'local_one': local_one,
#         'local_news': local_news,
#     }
#     return render(request, 'news/index.html', context=context)

class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:5]
        context['local_one'] = News.published.filter(category__name='Mahalliy').order_by('-publish_time')[:1]
        context['local_news'] = News.published.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:6]
        context['local_world'] = News.published.filter(category__name='Jahon').order_by('-publish_time')[:1]
        context['local_worlds'] = News.published.all().filter(category__name='Jahon').order_by('-publish_time')[1:6]
        context['local_tex'] = News.published.filter(category__name='Texnologiya').order_by('-publish_time')[:1]
        context['local_texs'] = News.published.all().filter(category__name='Texnologiya').order_by('-publish_time')[1:6]
        context['local_sport'] = News.published.filter(category__name='Sport').order_by('-publish_time')[:1]
        context['local_sports'] = News.published.all().filter(category__name='Sport').order_by('-publish_time')[1:6]

        return context

# def ContactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("<h2>Biz bilan bog'langaningiz uchun tashakkur</h2>")
#     context = {
#         'form': form
#     }
#     return render(request, 'news/contact.html', context)

class ContactPageViews(TemplateView):
    template_name = 'news/contact.html'
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }

        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h3>Biz bilan bog'langaningiz uchun tashakkur</h3>")

        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

def Page404Views(request):
    context = {

    }

    return render(request, 'news/404.html', context)

class LocalNewsViews(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy-yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Mahalliy')

        return news


class XorijNewsViews(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij-yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Jahon')

        return news



class SportNewsViews(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport-yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')

        return news



class TexnalogiyaNewsViews(ListView):
    model = News
    template_name = 'news/texnalogiya.html'
    context_object_name = 'texnalogiya-yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Texnologiya')

        return news