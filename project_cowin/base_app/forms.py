from django.forms import ModelForm
from . import models

class signup_form(ModelForm):

    class Meta:
        model = models.Person
        fields = '__all__'

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['city'].queryset = City.objects.none()