# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserChangeForm, CustomPasswordChangeForm
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('personal_cabinet') 
            else:
                messages.error(request, "Iltimos xatoliklarni to'g'irlab qayta urinib kuring") # Redirect to appropriate page after login
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Akkaunt yaratildi")
            return redirect('personal_cabinet')  # Redirect to appropriate page after registration
        else:
            messages.error(request, "Iltimos xatoliklarni to'g'irlab qayta urinib kuring")
    else:
        form = CustomUserCreationForm()

    return render(request, 'registers.html', {'form': form})
@login_required
def personal_cabinet(request):
    if request.method == 'POST':
        account_form = CustomUserChangeForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        
        if 'update_account' in request.POST:
            if account_form.is_valid():
                account_form.save()
                messages.success(request, "Malumotlar o'zgardi")
                return redirect('personal_cabinet')

        elif 'change_password' in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, "Parol o'zgardi")
                return redirect('personal_cabinet')
    else:
        account_form = CustomUserChangeForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    context = {
        'account_form': account_form,
        'password_form': password_form,
        'user': request.user,
    }
    return render(request, 'my-account.html', context)