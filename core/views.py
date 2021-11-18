from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .forms import AddressForm, CrispySubmitForm, CrispyAddressForm, CustomFieldForm

def getContext(request):
    name = ""
    address_1 = ""
    address_2 = ""
    city = ""
    state = ""
    zip_code = ""

    submitbutton = request.POST.get("submit")
    form = AddressForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        address_1 = form.cleaned_data.get("address_1")
        address_2 = form.cleaned_data.get("address_2")
        city = form.cleaned_data.get("city")
        state = form.cleaned_data.get("state")
        zip_code = form.cleaned_data.get("zip_code")

    context = {"form": form, "name": name, "address_1": address_1,
               "address_2": address_2, "city": city, "state": state,
               "zip_code": zip_code, "submitbutton": submitbutton, }

    return context

def index(request):
    context = getContext(request)
    return render(request, "index.html", context)

def success(request):
    context = getContext(request)
    return render(request, "success.html", context)

def finish(request):
    context = getContext(request)
    return render(request, "finish.html", context)


class AddressFormView(FormView):
    form_class = AddressForm
    success_url = reverse_lazy('success')
    template_name = 'form_2.html'

class CrispyAddressFormView(FormView):
    form_class = CrispyAddressForm
    success_url = reverse_lazy('success')
    template_name = 'form_3.html'

class CrispySubmitFormView(FormView):
    form_class = CrispySubmitForm
    success_url = reverse_lazy('success')
    #template_name = 'crispy_form.html'
    template_name = 'form_4.html'

class CustomFieldFormView(FormView):
    form_class = CustomFieldForm
    success_url = reverse_lazy('success')
    template_name = 'crispy_form.html'

#class SuccessView(TemplateView):
#    template_name = 'success.html'
