from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CapOrderForm, CapOrderImageForm
from .models import CapOrder, CapOrderImage
from django.core.files.storage import FileSystemStorage

# Create your views here.
def dashboard(request):
    results = CapOrder.objects.all()
    images = CapOrderImage.objects.all()
    print(images)
    for image in images:
        print(image.cap_order)
        print(image.image)
    

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
        'images': images,
    }
    return render(request, "dashboard.html", context)


def submit_form(request):
    # if request.method == 'POST':
    #     form = CapOrderForm(request.POST)
    #     if form.is_valid():  
    #         form.save()
    #         return redirect('dashboard')  # Redirect after successful submission
    # else:
    #     form = CapOrderForm()

    if request.method == 'POST':
        form = CapOrderForm(request.POST)
        # image = request.POST['image']
        # image = request.FILE['image']
        # print(image)
        # file_path = ""
        # if request.FILE['image']:
        #     # print(attachment.name, attachment_extension)
            
        #     # print("True, valid size")

        #     folder_name = '/cap_order_images'
        #     # media_root = settings.MEDIA_ROOT
        #     location = f'{folder_name}'
        #     # print(location)
        #     fs = FileSystemStorage(location=folder_name)
        #     filename = fs.save(image, image)
        #     # print(filename)
        #     file_path = f'{filename}'
        if form.is_valid():  
            form.save()
            # image = form.cleaned_data.get('image')
            # images = request.FILES.get('image')
            # print(request.FILES)
            # print(images)
            # for image in images:
            #     CapOrderImage.objects.create(cap_order=form, image=image)
            return redirect('dashboard')  # Redirect after successful submission
    else:
        form = CapOrderForm()

    return render(request, 'form.html', {'form': CapOrderForm()})
