from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('search/', views.index, name='search'),
    path('add/', views.add, name='add'),
    path('scheck/', views.sCheck, name='scheck'),
    path('fundamentals/', views.fundamentals, name='fundamentals'),
    path('holidays/', views.holidays, name='holidays'),
    path('results/', views.results, name='results'),
    path('options/', views.options, name='options'),
    path('fiidii/', views.fiidii, name='fiidii'),
    path('ipos/', views.ipos, name='ipos')
    #path('showplt/', views.graph_data, name='showplt'),

]
