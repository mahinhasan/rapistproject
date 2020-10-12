from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import*
from .import views
urlpatterns = [
    
    path('',PostLIst.as_view(),name='home'),
    path('rapist/<int:pk>',RapistDetail.as_view(),name='rapist-detail'),
    path('addrapist',AddRppist.as_view(),name='addrapist'),
    path('update/<int:pk>',UpdateRapist.as_view(),name='update'),
    path('delete/<int:pk>/remove',DeleteRapist.as_view(),name='delete'),
    path('register',UserRegister.as_view(),name = 'register'),
    



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
