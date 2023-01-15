from django.urls import path
from .import views
urlpatterns = [
    path('student/',views.showdata,name='addandshow'),
    path('delete/<int:id>/',views.delete_data,name='deldata'),
    path('update/<int:id>/',views.update_data,name='updata'),
]
