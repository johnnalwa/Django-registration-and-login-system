from django.contrib import admin

from .models import (
    DisciplinaryAction,
    EducationalProgram,
    Facility,
    Incident,
    Infraction,
    Inmate,
    InmateEducation,
    LegalCase,
    MedicalRecord,
    Profile,
    ReleasePlan,
    Visitor,
    WorkAssignment,
    WorkRecord,
)

admin.site.site_header = 'Prison Managemennt System'
admin.site.site_title = 'Admin'
admin.site.index_title = 'prison Management system admins'


admin.site.register(Profile)

@admin.register(Inmate)
class InmateAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'gender', 'admission_date', 'security_level']
    search_fields = ['first_name', 'last_name']


@admin.register(ReleasePlan)
class ReleasePlanAdmin(admin.ModelAdmin):
    list_display = ['inmate', 'release_date', 'release_reason']
    search_fields = ['inmate__first_name', 'inmate__last_name']


@admin.register(WorkAssignment)
class WorkAssignmentAdmin(admin.ModelAdmin):
    list_display = ['inmate', 'task', 'assigned_by', 'date_assigned']
    search_fields = ['inmate__first_name', 'inmate__last_name']


@admin.register(WorkRecord)
class WorkRecordAdmin(admin.ModelAdmin):
    list_display = ['work_assignment', 'date', 'hours_worked']
    search_fields = ['work_assignment__inmate__first_name', 'work_assignment__inmate__last_name']


@admin.register(Infraction)
class InfractionAdmin(admin.ModelAdmin):
    list_display = ['inmate', 'description', 'date', 'reported_by']
    search_fields = ['inmate__first_name', 'inmate__last_name']


@admin.register(DisciplinaryAction)
class DisciplinaryActionAdmin(admin.ModelAdmin):
    list_display = ['infraction', 'action_taken', 'disciplinary_officer', 'date']
    search_fields = ['infraction__inmate__first_name', 'infraction__inmate__last_name']


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['inmate', 'condition', 'treatment', 'doctor', 'date']
    search_fields = ['inmate__first_name', 'inmate__last_name']


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_visit', 'inmate_visited']
    search_fields = ['inmate_visited__first_name', 'inmate_visited__last_name']


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ['type', 'description', 'reported_by', 'date_reported']
    search_fields = ['reported_by__username']


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'capacity']
    search_fields = ['name', 'location']


@admin.register(LegalCase)
class LegalCaseAdmin(admin.ModelAdmin):
    list_display = ['inmate', 'case_number', 'court_date', 'case_description']
    search_fields = ['inmate__first_name', 'inmate__last_name']


@admin.register(EducationalProgram)
class EducationalProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'instructor', 'start_date', 'end_date']


@admin.register(InmateEducation)
class InmateEducationAdmin(admin.ModelAdmin):
    list_display = ['inmate', 'program', 'enrollment_date', 'completion_date']

