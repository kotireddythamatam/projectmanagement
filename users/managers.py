############################## django ##############################
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
	"""
	Manager class for user.
	"""

	def _create_user(self, email, password, **kwargs):
		if not email:
			raise TypeError('Users must have an email address.')
		if not password:
			raise TypeError('Users must have a password.')
		email = self.normalize_email(email)
		user = self.model(email=email, **kwargs)
		user.set_password(password)
		user.save()
		return user

	def create_user(self, email, password, **kwargs):
		kwargs.setdefault('is_staff', False)
		kwargs.setdefault('is_superuser', False)
		return self._create_user(email, password, **kwargs)

	def create_superuser(self, email, password, **kwargs):
		kwargs.setdefault('is_staff', True)
		kwargs.setdefault('is_superuser', True)
		return self._create_user(email, password, **kwargs)