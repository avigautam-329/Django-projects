from django.conf.urls import url
from .views import *
app_name='payment'
urlpatterns =[
    url(r'^process/$',payment_process,name='process'),
    url(r'^done/$', payment_done, name='done'),
    url(r'^canceled/$',payment_canceled, name='canceled'),
    ]
