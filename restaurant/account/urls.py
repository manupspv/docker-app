from django.urls import path
from . import views
from .forms import UserLoginForm


urlpatterns = [
    path('', views.signup, name="account-signup"),
    path('signup/', views.signup, name="account-signup"),
    path('login/', views.MyLoginView.as_view(authentication_form=UserLoginForm,redirect_authenticated_user=True), name="account-login"),
    path('logout/', views.MyLogoutView.as_view(template_name='account/logout.html'), name="account-logout"),

]