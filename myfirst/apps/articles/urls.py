from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name = 'index' ),
    path('<int:article_id>/', views.detail, name = 'detail' ),
    path('<int:article_id>/leave_comment', views.leave_comment, name = 'leave_comment' ),
    path('new_article', views.new_article, name = 'new_article' ),
    path('add_article', views.add_article, name = 'add_article' )
]