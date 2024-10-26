from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CapOrderForm
from .models import CapOrder

# Create your views here.
def dashboard(request):
    results = CapOrder.objects.all()
    

    if request.method == 'POST':
        content = request.POST['content']
        try:
            s_results = CapOrder.objects.get(ps_number=content)
        except:
            try:
                s_results = CapOrder.objects.get(ps_date=content)
            except:
                try:
                    # s_results = CapOrder.objects.get(byr=content)
                    pass
                except:
                    pass


        context = {
            's_results': s_results,
            }
        return render(request, "dashboard.html", context)


    
    context = {
        'results': results,
    }
    return render(request, "dashboard.html", context)


def submit_form(request):
    if request.method == 'POST':
        form = CapOrderForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('dashboard')  # Redirect after successful submission
    else:
        form = CapOrderForm()

    return render(request, 'form.html', {'form': form})
