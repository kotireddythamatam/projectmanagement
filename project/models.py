############################## django ##############################
from django.db import models
from django.utils.translation import gettext_lazy as _

############################## django ##############################
from company.models import Company

############################## common ##############################
from common.models import (
	BaseModel,
	LogModel,
)

####################################################################

class Project(BaseModel):
	image = models.ImageField(upload_to='project')
	location = models.TextField()
	company = models.ForeignKey(
		Company,
		related_name='company_project',
		on_delete=models.CASCADE
	)

	class Meta:
		db_table = 'project'
		verbose_name = _('project')
		verbose_name_plural = _('projects')


class ProjectLog(LogModel):
	pass

