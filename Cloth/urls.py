from django.urls import path
from . import views

urlpatterns = [
    path('',views.cloth),
    path('cloth/',views.cloth),
    path('shirt/',views.getShirt, name='shirt'),
    path('pant/',views.getPant),
    path('tshirt/',views.getTshirt),
    path('reg/',views.getReg),

    

    

]

