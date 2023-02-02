from django.db import models

class Contact(models.Model):
	full_name = models.CharField(max_length=60)
	phone_number = models.CharField(max_length=11, help_text="needs to be in this format 08100482341")
	message = models.TextField(blank=True, null=True)
