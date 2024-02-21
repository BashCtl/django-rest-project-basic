from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer


@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        article_serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(article_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        article_serializer = ArticleSerializer(data=data)

        if article_serializer.is_valid():
            article_serializer.save()
            return JsonResponse(article_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        article_serializer = ArticleSerializer(article)
        return JsonResponse(article_serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        article_serializer = ArticleSerializer(article, data=data)
        if article_serializer.is_valid():
            article_serializer.save()
            return JsonResponse(article_serializer.data)
        return JsonResponse(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
