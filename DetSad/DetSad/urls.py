from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login1, name='login'),
    path('register/', views.register, name='register'),
    path('change_profile/<int:id>/', views.change_profile, name='change_profile'),
    path('logout/', views.logout1, name='logout'),
    path('child_info/<int:id>/', views.child_info, name='child_info'),
    path('add_section_child/', views.add_section_child, name='add_section_child'),
    path('sections/', views.sections, name='sections'),
    path('load_childs', views.load_childs, name='load_childs'),
    path('garten_search', views.garten_search, name='garten_search'),
    path('garten/<int:id>/', views.garten, name='garten'),
    path('add_parent/', views.add_parent, name='add_parent'),
    path('add_section/', views.add_section, name='add_section'),
    path('add_organization/', views.add_organization, name='add_organization'),
]
