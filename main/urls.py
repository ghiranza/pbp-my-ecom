from django.urls import path
from main.views import show_main, create_vbucks_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user
from main.views import logout_user
from main.views import edit_vbucks, delete_vbucks

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-vbucks-entry', create_vbucks_entry, name='create_vbucks_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-vbucks/<uuid:id>', edit_vbucks, name='edit_vbucks'),
    path('delete/<uuid:id>', delete_vbucks, name='delete_vbucks'),
]