from django.urls import path
from .import views
urlpatterns = [
    path('student/',views.showdata,name='addandshow'),
    path('delete/<int:id>/',views.delete_data,name='deldata'),
]
