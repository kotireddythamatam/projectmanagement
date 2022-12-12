from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.conf import settings


def current_site_details(request):
	return get_current_site(request).domain


def get_protocol_type(request):
	protocol_type = 'http://'
	if request.is_secure():
		protocol_type = 'https://'
	return protocol_type


def send_basic_mail(subject, body, to_email):
	mail = EmailMessage(
			subject=subject,
			body=body,
			from_email=settings.DEFAULT_FROM_EMAIL,
			to=to_email
		)
	mail.send()


