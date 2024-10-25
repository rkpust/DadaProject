from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CapOrderForm

# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html")


def submit_form(request):
    if request.method == 'POST':
        form = CapOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect after successful submission
    else:
        form = CapOrderForm()

    return render(request, 'form.html', {'form': form})
