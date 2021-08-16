from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4',
                                                             'placeholder':'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control py-4',
                                                             'placeholder':'Введите пароль'}))
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите адрес ел.почты'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Подтвердите пароль'}))

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'



class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'readonly': True}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(), required=False) # делает поле необязательным

    class Meta():
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'

            self.fields['image'].widget.attrs['class'] = 'custom-file-input' #class="custom-file-input" in file profile.html (id="userAvatar")

