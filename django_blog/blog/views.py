from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from datetime import datetime
from .models import ArticleModel
from django.utils import timezone
from .forms import ArticleForm
# Create your views here.


class Home(View):
    """
    docstring
    """

    def get(self, request):
        """
        docstring
        """
        return HttpResponse('Welcome to my blog!')

    def post(self, request):
        return HttpResponse("[POST] Welcome to my blog!")


class Article(View):
    """
    docstring
    """

    def get(self, request):
        """
        docstring
        """
        articles = ArticleModel.objects.all()

        return render(request, "articles.html", {'articles': articles, 'form': ArticleForm()})

    def post(self, request):
        form = ArticleForm(request.POST)
        form.instance.creation_date = datetime.now(tz=timezone.utc)
        form.save()

        return redirect("/blog/articles")


class ArticleDetails(View):
    """
    docstring
    """

    def get(self, request, id):
        try:
            article = ArticleModel.objects.get(id=id)
            return render(request, 'article_details.html', {'article': article})
        except ArticleModel.DoesNotExists:
            return HttpResponseNotFound()
