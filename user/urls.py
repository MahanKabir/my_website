

from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'), #localhost:8000/accounts/register
    path('profile/', views.profile, name='profile'), #localhost:8000/accounts/profile
    path('desktop/', views.desktop, name='desktop'), #localhost:8000/accounts/desktop
    path('perm', views.perm, name='perm'), #localhost:8000/accounts/perm
    path('group', views.group_user, name='group'), #localhost:8000/accounts/group
    path('c_g', views.create_group, name='c_g'), #localhost:8000/accounts/c_g
    path('manage', views.user_manage, name='manage'), #localhost:8000/accounts/manage
]
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']


# MVT
# Model View Template