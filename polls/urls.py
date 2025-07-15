from django.urls import path 

from .import views

app_name = "polls"
urlpatterns=[
    path("", views.index, name="index"),
    path("masaje-facial/", views.masaje_facial, name="masaje_facial"), 
    path("masaje-relajante/", views.masaje_relajante, name="masaje_relajante"),
    path("masaje-descontracturante/", views.masaje_descontracturante, name="masaje_descontracturante"),
    path('tomar-turno/', views.tomar_turno, name='tomar_turno'),
    path('cancelar-turno/<int:turno_id>/', views.cancelar_turno, name='cancelar_turno'),

    path('turnos/', views.lista_turnos, name='lista_turnos'),
    path('turnos/limpiar/', views.limpiar_turnos, name='limpiar_turnos'),
    path('', lambda request: redirect('polls/', permanent=False)),
    path('polls/', include('polls.urls')),



    
   

]

    
