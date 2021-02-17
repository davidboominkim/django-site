from django.urls import path
from django.conf.urls import include

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('polls/', views.IndexView.as_view(), name='index'),

    path('polls/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),

    path('polls/thoughts/', views.post_thought,name='post_thought'),

    path('polls/thoughts/list', views.index, name='thought_index'),

]