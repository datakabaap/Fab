from django.urls import path
from .views import (
    home,
    details,

)

urlpatterns = [
    path('', home, name='search-home'),
    path('details/', details, name='search-details'),



]