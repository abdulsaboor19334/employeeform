from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .base import UserManager

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_head = models.CharField(max_length=100)

class Budget(models.Model):
    department = models.ForeignKey(Department,models.CASCADE)
    budget_monthly = models.IntegerField()
    budget_yearly = models.IntegerField()


class User(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=100)
    user_number = models.IntegerField()
    user_email = models.EmailField(unique=True)
    user_salary = models.IntegerField()
    user_role = models.CharField(max_length=100)
    department = models.ForeignKey(Department, models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
    
class Expenses(models.Model):
    employee = models.ForeignKey(User,models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    hotel_rent = models.IntegerField()
    transport = models.IntegerField()
    meal = models.IntegerField()
    others = models.IntegerField()
    form_status = models.BooleanField()
    total_amount = models.IntegerField()
