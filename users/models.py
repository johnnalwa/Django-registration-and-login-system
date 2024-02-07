from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agent_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.agent_code
    
# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)


class Inmate(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    admission_date = models.DateField()
    security_level = models.CharField(max_length=50)
    cell_number = models.CharField(max_length=20)
    height = models.FloatField()  # Height in meters
    weight = models.FloatField()  # Weight in kilograms
    hair_color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)
    tattoos = models.TextField(blank=True, null=True)
    scars = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='inmate_photos/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class ReleasePlan(models.Model):
    inmate = models.ForeignKey(Inmate, on_delete=models.CASCADE)
    release_date = models.DateField()
    release_reason = models.CharField(max_length=200)
    

class WorkAssignment(models.Model):
    inmate = models.ForeignKey(Inmate, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_assigned = models.DateField()
    # Other fields

class WorkRecord(models.Model):
    work_assignment = models.ForeignKey(WorkAssignment, on_delete=models.CASCADE)
    date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    # Other fields
    
class Infraction(models.Model):
    inmate = models.ForeignKey(Inmate, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # Other fields

class DisciplinaryAction(models.Model):
    infraction = models.ForeignKey(Infraction, on_delete=models.CASCADE)
    action_taken = models.TextField()
    disciplinary_officer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    # Other fields
    

class MedicalRecord(models.Model):
    inmate = models.ForeignKey(Inmate, on_delete=models.CASCADE)
    condition = models.CharField(max_length=200)
    treatment = models.TextField()
    doctor = models.CharField(max_length=100)
    date = models.DateField()
    
class Visitor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_visit = models.DateField()
    inmate_visited = models.ForeignKey(Inmate, on_delete=models.CASCADE)
    purpose = models.TextField()
    
    
class Incident(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_reported = models.DateTimeField(auto_now_add=True)
    
class Facility(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    
class LegalCase(models.Model):
    inmate = models.ForeignKey(Inmate, on_delete=models.CASCADE)
    case_number = models.CharField(max_length=100)
    court_date = models.DateField()
    case_description = models.TextField()
    
class EducationalProgram(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    
class InmateEducation(models.Model):
    inmate = models.ForeignKey(Inmate, on_delete=models.CASCADE)
    program = models.ForeignKey(EducationalProgram, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    completion_date = models.DateField(null=True, blank=True)