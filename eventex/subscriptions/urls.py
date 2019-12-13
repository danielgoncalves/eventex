from django.urls import path

from .views import new
from .views import detail

app_name = 'subscriptions'

urlpatterns = [
    path('', new, name='new'),
    path('<uuid:hash_id>/', detail, name='detail'),
]
