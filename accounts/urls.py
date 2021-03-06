from django.conf.urls import url
from django.contrib.auth import views as auth_views  # autoriation views para que no se confunda con el view the abajo
from django.urls import reverse
from . import views

# Blog accounts view created by CarlaPastor
app_name = 'accounts'

urlpatterns = [
    url(r"login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"signup/$", views.SignUp.as_view(), name="signup"),
]
