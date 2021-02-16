from django.urls import path
from django.conf.urls import include

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('', include('bootstrap4.urls')),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # # ex: /polls/5/
    # path('<int:thought_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:thought_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:thought_id>/vote/', views.vote, name='vote'),

    # path('<slug:slug>/', views.post_thought,name='post_thought'),
    path('thoughts/', views.post_thought,name='post_thought'),

    # path('thoughts/', views.think, name='thought_sub'),
    path('thoughts/list', views.index, name='thought_index'),
    # path('thoughts/<int:thought_id>/', views.detail, name='thought_detail')

]