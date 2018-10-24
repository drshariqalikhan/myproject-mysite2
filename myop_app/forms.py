from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from .models import JourneyData

class RegistrationFrom(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self,commit = True):
        user = super(RegistrationFrom, self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class JourneyDataFrom(ModelForm):
    class Meta:
        model  = JourneyData
        # fields = '__all__'
        fields = [
            'patient_name','IsActiveSession',
            'patient_firstname','op_name',
             'patient_lastname','op_date',
             'patient_mobile_number','journey_point',
            'gender','planned_postop_location',
            'date_of_birth','race',
            'weight_at_op','height',
            'sbp_at_op','dbp_at_op',
            'heartrate_at_op',
            'AboutAnesLinks','AboutPhysioLinks',
            'AboutWoundCareLinks','AboutOpSurgeryLinks',

            ]
