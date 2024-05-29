# Importa il modulo path da Django
from django.urls import path
# Importa le viste dal modulo corrente
from . import views

# Definisci gli URL patterns per l'applicazione 'blog'
urlpatterns = [
    # Associa la vista index alla radice del sito
    path('', views.index, name='index'),
]
