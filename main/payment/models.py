from django.db import models

# Create your models here.
class Payment(models.Model):
    booking = models.OneToOneField(Booking, related_name='payment', on_delete=models.CASCADE)
    amount = models.IntegerField()  # amount in kobo
    reference = models.CharField(max_length=200, unique=True)
    status = models.CharField(max_length=20, default="pending")  # pending, success, failed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking.customer} - {self.status}"
