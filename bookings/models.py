from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Represents a service that can be booked (e.g., Haircut, Consultation)
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.DurationField(help_text="Enter duration like: 00:30:00 for 30 mins")
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

# Represents available time slots for booking
class TimeSlot(models.Model):
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.date} | {self.start_time} - {self.end_time}"

    class Meta:
        ordering = ['date', 'start_time']

# Represents a user's actual booking of a service at a time
class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if self.user:
            return f"{self.user.username} - {self.service.name} on {self.date} at {self.time}"
        return f"{self.service.name} on {self.date} at {self.time}"
