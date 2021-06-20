from django.urls import path
from .views import quem_somos, para_empresa, para_candidato, contato, arrow


urlpatterns= [
    path('', quem_somos, name='quem_somos'),
    path('para_empresa/', para_empresa, name='para_empresa'),
    path('para_candidato/', para_candidato, name='para_candidato'),
    path('contato/', contato, name='contato'),
    path('arrow/', arrow, name='arrow'),

]