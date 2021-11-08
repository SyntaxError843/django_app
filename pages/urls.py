from django.urls import path, include
from . import views

app_name = 'pages';

urlpatterns = [
    path('', views.index, name='index'),
    path( 'shop/', include( ('shop.urls', 'shop'), namespace='shop') ),
]
