from django.urls import path
from . import views
from .views import home, login_view, services_view, book_service, admin_dashboard, register
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('login-placeholder/', login_view, name='login_view'),  # Optional if you're keeping old one
    path('services/', views.services, name='services'),
    path('book/', book_service, name='book_service'),
    path('dashboard/', admin_dashboard, name='dashboard'),
    path('register/', register, name='register'),  # ✅ New
    path('my-bookings/', views.my_bookings, name='my_bookings'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

