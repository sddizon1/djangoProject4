from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    return render(request, "home_page.html")


def contact_page(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form
    }
    if contact_form.is_valid():
        print(request.POST.get('fullname'))
    return render(request, "contact/contact.html", context)