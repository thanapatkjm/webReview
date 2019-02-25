from django.urls import path
from . import views

app_name='review'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('add_rest/', views.add_rest, name='add_rest'),
    path('creating/', views.creating, name='creating'),
    path('res/<int:rest_id>/', views.res, name='res'),
    path('add_review/<int:rest_id>', views.add_review, name='add_review'),
    path('home/searching', views.searching, name='searching'),
]
    # {% for name in latest_animal_name %}
    #     <li><a href="/animalSite/{{ Animal.id }}/">{{ name.animal_name }}</a></li>
    # {% endfor %}
