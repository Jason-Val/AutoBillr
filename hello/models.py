from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profiel(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)

class BillPayer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	percent = models.DecimalField(max_digits=2, decimal_places=2)

	PAID = 'pa'
	PROCESSING = 'pr'
	FAILED = 'fa'
	PAY_STATUS_CHOICES = ((PAID, "Payment Successful"), (PROCESSING, "Payment Processing"), (FAILED, "Payment Failed"))
	pay_status = models.CharField(max_length=2, choices=PAY_STATUS_CHOICES, default=PAID)

class Bill(models.Model):
	bill_name = models.CharField(max_length=50)
	category = models.CharField(max_length=50, null=True)
	transaction_id = models.CharField(max_length=50)
	leader = models.ForeignKey(BillPayer, on_delete=models.CASCADE)
	users = models.ManyToManyField(User, blank=True)
	balance = models.DecimalField(max_digits=6, decimal_places=2)
	due_date = models.DateField()