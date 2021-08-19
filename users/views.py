from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            messages.success(request, f" Вы успешно вошли как {username}!")

            if user or user.is_active:

                auth.login(request, user)

                return redirect(reverse('index'))
        return render(request, 'users/login.html', {'form': form})

    else:

        form = UserLoginForm()
        context = {'form':form}
        return render(request, 'users/login.html', context)



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
        else:
            print(form.errors) # класная штука (видно почему не регистрирует)
            return render(request, 'users/register.html', {'form':form})


    else:
        form = UserRegistrationForm()
        context = {'form':form}
        return render(request, 'users/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data = request.POST, files=request.FILES, instance=request.user) #instance - указывает какую сущность мы обновляем
        if form.is_valid():
            form.save()
            return render(request, 'users/user_update.html')
        else:
            print(form.errors)
            return render(request, 'users/profile.html', {'form':form})

    else:

        form = UserProfileForm(instance=request.user)
        context = {'form':form}
        return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))
