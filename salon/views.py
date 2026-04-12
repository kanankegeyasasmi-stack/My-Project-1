from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ContactMessage, Booking

def home(request):
    success = False

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and phone and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            success = True

    return render(request, 'salon/index.html', {'success': success})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'salon/signup.html', {'form': form})


@login_required
def booking_page(request):
    success = False

    if request.method == 'POST':
        service = request.POST.get('service', '').strip()
        appointment_date = request.POST.get('appointment_date', '').strip()
        appointment_time = request.POST.get('appointment_time', '').strip()
        notes = request.POST.get('notes', '').strip()

        if service and appointment_date and appointment_time:
            Booking.objects.create(
                user=request.user,
                service=service,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                notes=notes
            )
            success = True

    return render(request, 'salon/booking.html', {'success': success})

def gallery(request):
    return render(request, 'salon/gallery.html')
