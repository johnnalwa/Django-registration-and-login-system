from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_superuser_with_tasks(self, username, password=None, **extra_fields):
        user = self.create_superuser(username, password, **extra_fields)
        user.is_superuser_with_tasks = True
        user.save(using=self._db)
        return user