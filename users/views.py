from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from products.models import Basket
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

@login_required(login_url='/users/login/') # декор закрывающий возможность использования функции def profile(request) без входа под своим логином login_url='/users/login/' - страница на которую перенаправляеться пользователь при попытке использования def profile(request)
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data = request.POST, files=request.FILES, instance=request.user) #instance - указывает какую сущность мы обновляем
        if form.is_valid():
            form.save()
            return render(request, 'users/user_update.html')
        else:
            print(form.errors)
            context = {'form':form}
            return render(request, 'users/profile.html', context)

    else:

        form = UserProfileForm(instance=request.user)
    baskets = Basket.objects.filter(user=request.user)
    total_quantity = 0
    total_sum = 0
    for basket in baskets:
        total_quantity += basket.quantity
        total_sum += basket.sum()

    context = {'form':form,
               'title': 'Store - Личный кабинет',
               'baskets': baskets,
               'total_quantity': total_quantity,
               'total_sum': total_sum,}

    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))
