from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
# from administrator.views import FeesView

app_name = 'administrator'


urlpatterns = [
    #path('studentdetails', views.s_details, name = 's_details'),#admin is doing it, so no use
    path('studentlog', views.studlog, name = 'studentlog'),#sign in page for students
    path('login', views.login, name = 'login'),#login page for student
    path('', views.home_page, name = 'home'),
    #path('register/', views.register, name='register'),
    path('signin_verify', views.signin_verify, name='signin_verify'),
    path('logout', views.logout, name='logout'),

    path('profile', views.profile, name='profile'),
    path('notice',views.notices, name='notice'),
    path('fees',views.fees, name='fees'),
    path('payment', views.payment, name='payment'),
    path('invoice', views.bill, name='invoice'),
    path('exam', views.examdetails, name='exam'),
    # path('fees', FeesView.as_view(), name='fees'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
