from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
from .models import Subscribe


# def contact(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#         email = request.GET.get('email')
#         if email:
#             Subscribe.objects.create(email=email)
#         messages.success(request, "Sizning xabaringiz yuborildi. Xabaringiz uchun rahmat!")
#         return HttpResponseRedirect('/contact/')
#     context = {'form': form}
#     return render(request, 'contact/contact.html', context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    email = request.POST.get('email')
    if email:
        Subscribe.objects.create(email=email)
        return redirect('contact')
    context = {'form': form, 'email': email}
    return render(request, 'contact/contact.html', context)

