from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
app_name='gadgets'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.GadgetCreate.as_view(), name='gadget_create'),
    path('main/<int:pk>/update/', views.GadgetUpdate.as_view(), name='gadget_update'),
    path('main/<int:pk>/delete/', views.GadgetDelete.as_view(), name='gadget_delete'),
    path('lookup/', views.TypeView.as_view(), name='type_list'),
    path('lookup/create/', views.TypeCreate.as_view(), name='type_create'),
    path('lookup/<int:pk>/update/', views.TypeUpdate.as_view(), name='type_update'),
    path('lookup/<int:pk>/delete/', views.TypeDelete.as_view(), name='type_delete'),
]

# Note that type_ and gadgets_ give us uniqueness within this application

