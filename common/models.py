############################## django ##############################
from django.db import models
from django.conf import settings



class BaseModel(models.Model):
	name = models.CharField(max_length=255)
	desctiption = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	deleted_at = models.DateTimeField(null=True, blank=True)
	created_by = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name='%(app_label)s_%(class)s_created_by',
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)
	updated_by = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name='%(app_label)s_%(class)s_updated_by',
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)

	class Meta:
		abstract = True

	def __self__(self):
		return self.name


class LogModel(models.Model):
	LOG_CHOICES = (
		('created', 'Created'),
		('updated', 'Updated'),
		('deleted', 'Deleted'),
	)
	category = models.CharField(max_length=10, choices=LOG_CHOICES, default='created')
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name='%(app_label)s_%(class)s_created_by',
		on_delete=models.SET_NULL, null=True, blank=True
	)

	def __str__(self):
		return self.message

	class Meta:
		abstract = True











