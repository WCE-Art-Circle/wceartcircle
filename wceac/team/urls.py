
from django.urls import path
from team import views
urlpatterns = [
    path('register-as-member',views.MemberRegistration.as_view(),name='MemberRegistration'),
]
