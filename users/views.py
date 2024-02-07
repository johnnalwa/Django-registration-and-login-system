from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import DisciplinaryActionForm, EducationalProgramForm, FacilityForm, IncidentForm, InfractionForm, InmateEducationForm, LegalCaseForm, LoginForm, MedicalRecordForm, RegisterForm, ReleasePlanForm, UpdateProfileForm, UpdateUserForm, VisitorForm, WorkAssignmentForm, WorkRecordForm 



        
@login_required
def home(request):
    return render(request, 'users/home.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)
        return reverse_lazy('home')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})


def release_plan_list(request):
    release_plans = ReleasePlanForm.objects.all()
    return render(request, 'release_plan_list.html', {'release_plans': release_plans})


def work_assignment_list(request):
    work_assignments = WorkAssignmentForm.objects.all()
    return render(request, 'work_assignment_list.html', {'work_assignments': work_assignments})


def work_record_list(request):
    work_records = WorkRecordForm.objects.all()
    return render(request, 'work_record_list.html', {'work_records': work_records})


def infraction_list(request):
    infractions = InfractionForm.objects.all()
    return render(request, 'infraction_list.html', {'infractions': infractions})


def disciplinary_action_list(request):
    disciplinary_actions = DisciplinaryActionForm.objects.all()
    return render(request, 'disciplinary_action_list.html', {'disciplinary_actions': disciplinary_actions})


def medical_record_list(request):
    medical_records = MedicalRecordForm.objects.all()
    return render(request, 'medical_record_list.html', {'medical_records': medical_records})


def visitor_list(request):
    visitors = VisitorForm.objects.all()
    return render(request, 'visitor_list.html', {'visitors': visitors})


def incident_list(request):
    incidents = IncidentForm.objects.all()
    return render(request, 'incident_list.html', {'incidents': incidents})


def facility_list(request):
    facilities = FacilityForm.objects.all()
    return render(request, 'facility_list.html', {'facilities': facilities})


def legal_case_list(request):
    legal_cases = LegalCaseForm.objects.all()
    return render(request, 'legal_case_list.html', {'legal_cases': legal_cases})


def educational_program_list(request):
    educational_programs = EducationalProgramForm.objects.all()
    return render(request, 'educational_program_list.html', {'educational_programs': educational_programs})


def inmate_education_list(request):
    inmate_educations = InmateEducationForm.objects.all()
    return render(request, 'inmate_education_list.html', {'inmate_educations': inmate_educations})
