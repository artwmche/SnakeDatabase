from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ex: /snakeApps/
    path('',views.default, name='default'),

    path('snakeDB', views.index, name='index'),
    # ex: /snakeApps/add/
    path('add', views.add, name='add'),

    path('loadAdd', views.loadAdd, name='loadAdd'),

    path('loadEdit/<int:snake_id>', views.loadEdit, name='loadEdit'),

    # ex: /snakeApps/edit/5
    path('edit/<int:snake_id>', views.edit, name='edit'),
    # ex: /snakeApps/delete/5
    path('delete/<int:snake_id>', views.delete, name='delete'),

    #path('loadLogin', auth_views.loadLogin, name='loadLogin'),

    url(r'^login/$', auth_views.login,{'template_name': 'registration/login.html'}, name='login'),

    url(r'^logout/$', auth_views.logout,{'template_name': 'registration/logout.html'}, name='logout'),

    path('loadRegistration', views.loadRegistration, name='loadRegistration'),

    path('registration', views.registration, name='registration'),

    path('scientist', views.scientist, name='scientist'),

    path('deleteScientist/<int:s_id>', views.deleteScientist, name='deleteScientist'),
]
