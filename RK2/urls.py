from django.urls import path
from computer import views
urlpatterns = [
    path('', views.index),
    path('createComp/', views.createComp),
    path('createDi/', views.createDi),
    path('deleteComp/<int:id>', views.deleteComp),
    path('deleteDi/<int:id>', views.deleteDi),
    path('editComp/<int:id>', views.editComp),
    path('editDi/<int:id>', views.editDi),
]
