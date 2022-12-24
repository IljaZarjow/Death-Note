from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views. sign_up, name = 'sign_up'),
    path('home/', views. index, name = 'home'),
    path('news/', views. news_home, name = 'news'),
    path('create/', views. create, name = 'create'),
    path('login', views.MyprojectLoginView.as_view(), name='login'),
    path('register', views.RegisterUserView.as_view(), name='register'),
    path('logout/', views.MyProjectLogout.as_view(), name='logout'),
    path('<int:pk>', views.NewsDetailView.as_view(), name = 'detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name = 'update'),
    path('<int:pk>/delete', views.NewsDeletelView.as_view(), name = 'delete')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)