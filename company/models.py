############################## django ##############################
from django.db import models
from django.utils.translation import gettext_lazy as _

############################## common ##############################
from common.models import (
	BaseModel,
	LogModel,
)

####################################################################

class Company(BaseModel):
	image = models.ImageField(upload_to='images')
	website = models.URLField()
	location = models.TextField()

	class Meta:
		db_table = 'company'
		verbose_name = _('company')
		verbose_name_plural = _('companies')


class CompanyLog(LogModel):
	pass