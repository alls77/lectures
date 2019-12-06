from PIL import Image
from django.forms import ImageField
from django.contrib.auth.models import User
from .models import Users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm


class FormControlMixin(object):
    def __init__(self, *args, **kwargs):
        super(FormControlMixin, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class AuthForm(FormControlMixin, AuthenticationForm):
    pass


class RegistrationForm(FormControlMixin, UserCreationForm):
    photo = ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'photo',
                  'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=commit)
        new_user = Users(user=user)
        if self.cleaned_data['photo']:
            new_user.photo = self.cleaned_data['photo']
            image = Image.open(new_user.photo)
            image.save(new_user.photo)
        if commit:
            new_user.save()
        return new_user


class ProfileForm(FormControlMixin, ModelForm):
    photo = ImageField(required=False)

    class Meta:
        model = User
        fields = ['photo', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=commit)
        update_user = Users.objects.get(user=user)
        if self.cleaned_data['photo']:
            update_user.photo = self.cleaned_data['photo']
            image = Image.open(update_user.photo)
            image.save(update_user.photo)
        if commit:
            update_user.save()

        return update_user
