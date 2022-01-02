
from django.contrib import admin
from django.urls import path 
from poll import views as view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.home, name='home'),
    path('create/', view.create, name='create'),
    path('vote/<poll_id>', view.vote, name='vote'),
    path('results/<poll_id>', view.results, name='results'),
]
