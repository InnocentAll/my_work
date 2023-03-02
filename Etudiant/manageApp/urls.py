from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('students_list', views.students_list, name='students_list'),
    path('add_student', views.add_student, name='add_student'),
    path('show_student/<student_id>', views.show_student, name='show_student'),
    path('delete_student/<student_id>', views.delete_student, name='delete_student'),
    path('update_student/<student_id>', views.update_student, name='update_student'),
    
    path('adresses_list', views.adresse_list, name='adresses_list'),
    path('add_adresse', views.add_adresse, name='add_adresse'),
    path('update_adresse/<adresse_id>', views.update_adresse, name='update_adresse'),
    path('delete_adresse/<adresse_id>', views.delete_adresse, name='delete_adresse'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
