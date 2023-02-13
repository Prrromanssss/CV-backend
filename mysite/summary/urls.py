from django.urls import path

from summary.views import HomePageView

app_name = 'summary'

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]
