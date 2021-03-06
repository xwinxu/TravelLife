from django.urls import path

from . import views

app_name = 'insprices'
urlpatterns = [
    path('', views.index, name='index'),
    path('plans/tic/', views.ticplan, name='ticplan'),
    path('plans/berkley/', views.berkplan, name='berkplan'),
    path('plans/allianz/', views.alliplan, name='alliplan'),
    path('plans/manulife/', views.manuplan, name='manuplan'),
    path('plans/gms/', views.gmsplan, name='gmsplan'),
    path('plans/tugo/', views.tugoplan, name='tugoplan'),
    path('plans/21stcentury/', views.twenfirstplan, name='twenfirstplan'),
    path('prices/', views.prices, name='prices'),
    path('prices/results', views.results, name='results'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact')
]