from django.conf.urls import url
from news.views import MyTestView

urlpatterns = [
    url(r'^testing/', MyTestView.as_view(), name="test"),
    # url(r'^', include('news.urls')),
]