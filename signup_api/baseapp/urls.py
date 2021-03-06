from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'baseapp'
urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.LoginPage,name='login'),
    path('register/',views.register,name='register'),
    path('welcome/',views.welcome,name='welcome'),
    path('logout/',views.LogoutPage,name='logout'),
    # path('addcourse/',views.postCourse,name='addcourse'),

    # path('api/course/', views.CourseView.as_view() ,name='course'),
    path('api/course/', views.CourseView.as_view() ,name='course'),
    path('api/getcourses',views.getcourses,name='getcourses'),
    path('api/getcoursenames',views.getCourseNames,name='getcoursenames'),
]
