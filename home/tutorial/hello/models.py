from django.db import models
from django.utils import timezone

# Create your models here.

class LogMessage(models.Model):
    message = models.CharField(max_length=100)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Return a string representation of the model."""
        date = timezone.localdate(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
        