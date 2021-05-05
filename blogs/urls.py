from django.urls import path
from blogs import views
urlpatterns = [
    path('publish',views.publish.as_view(),name='publish'),
]