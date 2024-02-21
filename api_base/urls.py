from django.urls import path
from . import views
from .views import ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    # path('article/', views.article_list),
    # path('article/', ArticleAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    # path('detail/<int:pk>/', views.article_detail),
    path('detail/<int:id>/', ArticleDetails.as_view()),
]
