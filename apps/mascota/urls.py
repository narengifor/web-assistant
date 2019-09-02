from django.urls import path, include
from apps.mascota.views import listadousuarios, index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, \
    MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    path('', index, name='index'),
    # path('nuevo', mascota_view, name='mascota_crear'),
    # path('listar', mascota_list, name='mascota_listar'),
    #path('editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
    # path('eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_eliminar'),

    path('nuevo', MascotaCreate.as_view(), name='mascota_crear'),
    path('listar', MascotaList.as_view(), name='mascota_listar'),
    path('editar/<int:pk>/', MascotaUpdate.as_view(), name='mascota_editar'),
    path('eliminar/<int:pk>/', MascotaDelete.as_view(), name='mascota_eliminar'),
    #path('editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_editar'),
    # path('eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_eliminar'),
    path('listado', listadousuarios, name='listado'),
]
