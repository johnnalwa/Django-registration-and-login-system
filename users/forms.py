from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import DisciplinaryAction, EducationalProgram, Facility, Incident, Infraction, Inmate, InmateEducation, LegalCase, MedicalRecord, Profile, ReleasePlan, UserProfile, Visitor, WorkAssignment, WorkRecord


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        # Generate the agent code
        user_profile = UserProfile(user=user, agent_code=f'COACL{UserProfile.objects.count() + 1:03d}')
        user_profile.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class InmateForm(forms.ModelForm):
    class Meta:
        model = Inmate
        fields = '__all__'


class ReleasePlanForm(forms.ModelForm):
    class Meta:
        model = ReleasePlan
        fields = '__all__'


class WorkAssignmentForm(forms.ModelForm):
    class Meta:
        model = WorkAssignment
        fields = '__all__'


class WorkRecordForm(forms.ModelForm):
    class Meta:
        model = WorkRecord
        fields = '__all__'


class InfractionForm(forms.ModelForm):
    class Meta:
        model = Infraction
        fields = '__all__'


class DisciplinaryActionForm(forms.ModelForm):
    class Meta:
        model = DisciplinaryAction
        fields = '__all__'


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = '__all__'


class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = '__all__'


class LegalCaseForm(forms.ModelForm):
    class Meta:
        model = LegalCase
        fields = '__all__'


class EducationalProgramForm(forms.ModelForm):
    class Meta:
        model = EducationalProgram
        fields = '__all__'


class InmateEducationForm(forms.ModelForm):
    class Meta:
        model = InmateEducation
        fields = '__all__'

