from django.urls import include, path
from . import views

urlpatterns = [
    
   #path('home/',views.home,name='Shophome'),
    path('',views.index,name='Index'),
    path('about/',views.about, name='AboutUS'),
    path('tracker/',views.tracker, name='Trackorder'),
    path('contact/',views.contact, name='ContactUS'),
    path('search/',views.search, name='search'),
    path('products/<int:id>/',views.productview, name='productview'),
    path('checkout/',views.checkout,name='checkout'),
]