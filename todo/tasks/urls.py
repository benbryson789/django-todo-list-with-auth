from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name ="list"),
    path('update_task/<str:pk>/', views.updateTask, name = "update_task"),
    path('delete/<str:pk>/', views.deleteTask, name = "delete"),
    path('login/',views.loginForm,name='login'),
    path('myaccount/',views.myAccount),
    path("logout",views.logoutForm),
    path("register/",views.registrationForm)
    # path('signup/', SignUpView.as_view(), name = 'signup'),
]