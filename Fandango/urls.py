from django.urls import path
from Fandango.views import CreatePegoste, HomePage, PegostesList, PegosteView

app_name = 'Fandango'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('pegostes/', PegostesList.as_view(), name='pegostes_list'),
    path('pegoste/<int:pk>/', PegosteView.as_view(), name='pegoste'),
    path('create_pegoste/', CreatePegoste.as_view(), name='create_pegoste')
]
