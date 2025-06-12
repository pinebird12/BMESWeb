from django.contrib.auth import base_user
from django.contrib.auth.hashers import make_password


class MemberManager(base_user.BaseUserManager):
    """
    TODO: Really go over all of this.
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extras):
        if not email:
            raise ValueError('Email cannot be blank')
        email = self.normalize_email(email)
        user = self.model(email=email,**extras)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        return user
