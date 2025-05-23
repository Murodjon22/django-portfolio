from django.urls import path
from .views import postListView
from .views import Custom404View

urlpatterns = [
    path("", postListView.as_view(), name='home'),
    path('404-test/', Custom404View.as_view(), name='404-test'),
]