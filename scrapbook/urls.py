from django.urls import path
from .views import ScrapbookView

urlpatterns = [
    path('scrapbook/', ScrapbookView.as_view(), name='scrapbook'),
]
