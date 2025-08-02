from django.shortcuts import render, get_object_or_404, redirect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import SimpleRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils import timezone

from .models import Booking, Service
from .forms import BookingForm

def home(request):
    return render(request, 'bookings/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # 👇 This is what sends them to the dashboard
            next_url = request.GET.get('next')
            return redirect(next_url if next_url else 'dashboard')

        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'bookings/login.html')
def logout_view(request):
    logout(request)
    return redirect('home')  

@login_required
def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # ✅ attach the logged-in user
            booking.save()
            return redirect('dashboard')
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_form.html', {'form': form})

def services_view(request):
    services = Service.objects.all()
    return render(request, 'bookings/services.html', {'services': services})

def services(request):
    service_list = [
        {"name": "Online Appointment Scheduling", "slug": "appointment", "icon": "📅"},
        {"name": "Service Listing with Pricing", "slug": "pricing", "icon": "💰"},
        {"name": "Instant Booking Confirmation", "slug": "confirmation", "icon": "✅"},
        {"name": "Customer Login & Registration", "slug": "login", "icon": "👤"},
        {"name": "Custom Time Slot Selection", "slug": "slots", "icon": "🕒"},
        {"name": "Business Dashboard", "slug": "dashboard", "icon": "📊"},
        {"name": "Manage Services Panel", "slug": "admin", "icon": "🛠️"},
        {"name": "Booking History Tracking", "slug": "history", "icon": "📖"},
        {"name": "Manual Booking Creation", "slug": "manual", "icon": "✍️"},
        {"name": "Block Unavailable Times", "slug": "block", "icon": "🚫"},
        {"name": "Email Confirmations", "slug": "email", "icon": "📧"},
        {"name": "In-app Instructions", "slug": "notes", "icon": "📝"},
        {"name": "Mobile-Friendly UI", "slug": "mobile", "icon": "📱"},
        {"name": "Booking Wizard", "slug": "wizard", "icon": "🧙‍♂️"},
        {"name": "Dark Mode Toggle", "slug": "dark", "icon": "🌙"},
        {"name": "Google Calendar Sync", "slug": "calendar", "icon": "🗓️"},
        {"name": "Payment Integration", "slug": "payment", "icon": "💳"},
        {"name": "QR Code Check-in", "slug": "qr", "icon": "🔳"},
        {"name": "Multiple Locations", "slug": "locations", "icon": "📍"},
        {"name": "Ratings & Reviews", "slug": "reviews", "icon": "⭐"},
    ]
    return render(request, 'bookings/services.html', {"services": service_list})

@login_required
def admin_dashboard(request):
    today = timezone.now().date()

    # ✅ Show all bookings only to staff, else only user's bookings
    if request.user.is_staff:
        all_bookings = Booking.objects.select_related('service').order_by('-created_at')
    else:
        all_bookings = Booking.objects.filter(user=request.user).select_related('service').order_by('-created_at')

    today_count = all_bookings.filter(date=today).count()
    total_count = all_bookings.count()

    # Only show service stats to staff (optional)
    service_counts = {}
    if request.user.is_staff:
        for service in Service.objects.all():
            count = all_bookings.filter(service=service).count()
            service_counts[service.name] = count

    context = {
        'all_bookings': all_bookings,
        'today_count': today_count,
        'total_count': total_count,
        'service_counts': service_counts
    }
    return render(request, 'bookings/dashboard.html', context)
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('service').order_by('-date', '-time')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'booking_form.html', {'form': form, 'edit_mode': True})

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        booking.delete()
        return redirect('dashboard')
    
def register_view(request):
    if request.method == 'POST':
        form = SimpleRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ Log them in immediately
            return redirect('dashboard')  # ✅ Redirect to dashboard
    else:
        form = SimpleRegisterForm()
    return render(request, 'bookings/register.html', {'form': form})