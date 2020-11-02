from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^checkout$', views.checkout),
    url(r'^store/receipt/(?P<order_id>[0-9]+)$', views.receipt)
]