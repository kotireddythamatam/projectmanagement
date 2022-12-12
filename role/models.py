############################## django ##############################
from django.db import models
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _


############################## common ##############################
from common.models import BaseModel

############################## company ##############################
from company.models import Company

####################################################################


class Role(BaseModel):
	"""
	Role of users.
	"""
	permissions = models.ManyToManyField(
		Permission,
		related_name="perm_role",
	)
	company = models.ForeignKey(
		Company,
		related_name='company_role',
		on_delete=models.CASCADE
	)

	class Meta(BaseModel.Meta):
		db_table = "role"
		verbose_name = _("role")
		verbose_name_plural = _("roles")

