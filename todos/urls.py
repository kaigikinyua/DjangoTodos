from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('/login',views.Login.as_view(),name="login"),
    path('/signup',views.SignUp.as_view(),name="signup"),
    path('/userpage',views.userpage,name="userpage"),
    path('/todo/<str:operation>/<str:todoid>',views.Todos.as_view(),name="todo"),
]
