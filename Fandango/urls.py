from django.urls import path

from Fandango.views import AddPegoste, HomePage, PegosteView, Pegostes, UpdatePegoste, RedirectSlugPegoste

app_name = 'Fandango'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('<username>/pegostes/', Pegostes.as_view(), name='pegostes_list'),
    path('<username>/pegoste/add', AddPegoste.as_view(), name='add_pegoste'),
    path('<username>/pegoste/<int:pk>/', RedirectSlugPegoste.as_view(), name='pegoste_pk'),
    path('<username>/pegoste/<slug:slug>/update', UpdatePegoste.as_view(), name='update_pegoste'),
    path('<username>/pegoste/<slug:slug>/', PegosteView.as_view(), name='pegoste'),
]
