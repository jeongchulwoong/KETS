from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
from django.http import HttpResponse
from .models import NewsListData

def index(request):

    newslist = NewsListData.objects.order_by('id')[:5]
    newspaper = []
    newstitle = []
    newsdate = []
    reporter = []
    newslink = []
    for news in newslist:
        # newspaper.append(news.newspaper)
        newstitle.aoppend(news.title)
        # newsdate.append(news.newsdate)
        # reporter.append(news.reporter)
        newslink.append(news.link)
    context = {
        # 'newspaper': newspaper,
        'newstitle': newstitle,
        # 'newsdate': newsdate,
        # 'reporter': reporter,
        'newslink': newslink,
    }
    return render(request, 'newslist/index.html')

# Create your views here.
