from django.shortcuts import render
from django.views import View
from account.forms import CustomerRegistrationForm
from django.contrib import messages

# Create your views here.

class registerView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'account/register.html' , {'form':form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your Registration will Successfully.')
            form.save()
        return render(request, 'account/register.html' , {'form':form})
    



    

