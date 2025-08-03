from django.urls import path
from . import views
from .views import logout_view
from django.contrib.auth import authenticate, login
from .views import home, login_view, services_view, book_service, admin_dashboard, register_view
from django.conf import settings
from django.conf.urls.static import static
from .models import Booking
from django.conf.urls import handler404

handler404 = 'bookings.views.custom_404_view'

urlpatterns = [
    path('', home, name='home'),
    path('login-placeholder/', login_view, name='login_view'),  # Optional if you're keeping old one
    path('services/', views.services, name='services'),
    path('book/', views.book_service, name='book_service'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('dashboard/', admin_dashboard, name='dashboard'),
    path('register/', register_view, name='register'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('logout/', logout_view, name='logout_view')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

