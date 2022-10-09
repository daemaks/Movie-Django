from django.urls import path
from .views import ContactDataView

urlpatterns = [
    path('', ContactDataView.as_view(), name='mailing_url')
]
