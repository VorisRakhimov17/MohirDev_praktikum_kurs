from django.urls import path
from .views import news_list, news_detail, HomePageView, ContactPageViews, Page404Views, LocalNewsViews, SportNewsViews, TexnalogiyaNewsViews, XorijNewsViews
urlpatterns =[
    path('', HomePageView.as_view(), name='home-page'),
    path('news', news_list, name='all_news_list'),
    path('<slug:news>/', news_detail, name='news-detail_page'),
    path('Mahalliy/news/', LocalNewsViews.as_view(), name='local-news-page'),
    path('Xorij/news/', XorijNewsViews.as_view(), name='xorij-news-page'),
    path('sport/news/', SportNewsViews.as_view(), name='sport-news-page'),
    path('texnalogiya/news/', TexnalogiyaNewsViews.as_view(), name='texnalogiya-news-page'),
    path('contact-us/', ContactPageViews.as_view(), name='contact'),
    path('404-page/', Page404Views, name='404-page'),
]