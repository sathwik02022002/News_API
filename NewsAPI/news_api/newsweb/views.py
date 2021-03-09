from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    news_api_requests=requests.get("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=5c7683d66b274d4ca3e9b30b34b7c6cc")
    api=json.loads(news_api_requests.content)
    return render(request,'home.html',{'api':api})