from django.contrib.auth.forms import UserCreationForm
from accounts.models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "ایمیل"
        self.fields['password2'].label = "پسورد"
        self.fields['password1'].label = "تکرار پسورد"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
