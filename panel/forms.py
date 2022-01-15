from django.forms import ModelForm

from accounts.models import *


class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MusicForm, self).__init__(*args, **kwargs)
        # self.fields['main_id'].label = "آی دی در سایت"
        self.fields['title'].label = "عنوان"
        self.fields['file'].label = "فایل"
        self.fields['description'].label = "توضیحات"
        self.fields['category'].label = "گروه"
        self.fields['cover'].label = "عکس"

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        # self.fields['main_id'].label = "آی دی در سایت"
        self.fields['title'].label = "عنوان"
        self.fields['description'].label = "توضیحات"
        self.fields['time_of_day'].label = "زمان"
        self.fields['cover'].label = "عکس"

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'name', 'email', 'phone', 'phone_verified', 'payed_until', 'admin', 'staff'
        )

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # self.fields['main_id'].label = "آی دی در سایت"
        self.fields['name'].label = "نام"
        self.fields['email'].label = "ایمیل"
        self.fields['admin'].label = "ایا ادمین هست؟"
        self.fields['staff'].label = "ایا کارمند هست؟"
        self.fields['phone'].label = "تلفن همراه"
        self.fields['phone_verified'].label = "شماره تایید شده؟"
        self.fields['payed_until'].label = "تا چه زمانی پرداخت کرده؟"
        self.fields['payed_until'].widget.attrs['readonly'] = True

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class TimeOfDayForm(ModelForm):
    class Meta:
        model = TimeOfDay
        fields = (
            'title', 'key'
        )

    def __init__(self, *args, **kwargs):
        super(TimeOfDayForm, self).__init__(*args, **kwargs)
        # self.fields['main_id'].label = "آی دی در سایت"
        self.fields['title'].label = "عنوان"
        self.fields['key'].label = "کلید"

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
