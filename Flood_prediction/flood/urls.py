from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('prediction',views.prediction),
    path('graph_view',views.graph_view),
    path('monthly_prediction',views.monthly_prediction),
]
