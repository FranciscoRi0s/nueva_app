from django.urls import path
from . import views

urlpatterns= [
path("todas/",views.TodasAPIView.as_view(),name="todas_las_vulnerabilidades"),
path("vulnerabilidad/<str:codigo>/",views.InformacionAPIView.as_view(),name="detalles"),
path("vulnerabilidad_descripcion/<str:descripcion>/",views.InformacionDescripcionAPIView.as_view(),name="descripcion"),

]