############################## django ##############################
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

############################## common ##############################
from common.models import (
	BaseModel,
	LogModel,
)

############################## common ##############################
from role.models import Role

############################## users ##############################
from .managers import UserManager


class User(AbstractUser, BaseModel):
	username = None
	name = None
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	email = models.EmailField(_('email address'), unique=True)
	role = models.ForeignKey(
		Role,
		null=True,
		blank=True,
		related_name="user_role",
		on_delete=models.SET_NULL
	)
	# verified_at = models.BooleanField(default=False)

	objects = UserManager()

	def __str__(self):
		return self.email

	class Meta(BaseModel.Meta):
		db_table = "user" 	# Database table name, default is app_label_model_name
		verbose_name = _("user")
		verbose_name_plural = _("users")
		indexes = [
			models.Index(fields=['email']),
			models.Index(fields=['is_active']),
			models.Index(fields=['deleted_at']),

		]
		# constraints = [
		# 	models.UniqueConstraint(fields=['email'], name='unique_email')
		# ]


	def get_full_name(self):
		"""
			If user has first_name and last_name then full_name = first_name + last_name
			if user has only first_name then full_name = first_name
			if user has only last_name then full_name = last_name
			otherwise fullname = email.split('@')
		"""
		full_name = None
		if self.first_name and self.last_name:
			 full_name = "%s %s" %(self.first_name, self.last_name)
		elif self.first_name:
			full_name = self.first_name
		elif self.last_name:
			full_name = self.last_name
		else:
			full_name = self.email.split("@")[0]
		return full_name


	def delete(self):
		self.deleted_at = timezone.now()
		self.save(updated_fields=['deleted_at'])

	def save(self, *args, **kwargs):
		logged_in_user = kwargs.get('user')
		if self.id:
			self.updated_by = logged_in_user
		else:
			self.created_by = logged_in_user
		super().save(*args, **kwargs)


class UserLog(LogModel):
	pass