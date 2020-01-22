from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
	title		=
	description	=
	price		=
	summary		=
	featured	=

	def get_absolute_urls(self):
		return reverse("product:product-detail", kwargs={"id": self.id})